# -*- coding: utf-8 -*-
#
# msa_excel - Script for generating excel table sheets for Gauge R&R values
#
# Carl Zeiss GOM Metrology GmbH, 2025
#

import gom

import copy
import os
import os.path
import re
import shutil
import tempfile
import zipfile

import xml.etree.ElementTree as ET
#from defusedxml import minidom

import Tools.MeasurementSystemAnalysis.msa_config as cfg
import Tools.MeasurementSystemAnalysis.msa_gui as gui
import Tools.MeasurementSystemAnalysis.msa_lib as msa


TEMPLATE_FILE_NAME = os.path.join(gom.app.software_directory, 'config', 'msa', 'msa_template.xlsx')
DATA_SHEET_FILE_NAME = 'xl/worksheets/sheet1.xml'
CALCULATION_SHEET_FILE_NAME = 'xl/worksheets/sheet2.xml'
IMPORT_SHEET_FILE_NAME = 'xl/worksheets/sheet3.xml'
STRINGS_FILE_NAME = 'xl/sharedStrings.xml'

#
# Maximum number of cells reserved for the appraiser/part/trial properties (must match the template)
#
NUMBER_OF_APPRAISERS = 3
NUMBER_OF_TRIALS = 3
NUMBER_OF_PARTS = 25

#
# Value used in empty table cells
#
NONE = '#NV'

#
# Build configuration for the ANOVA-2 setup
#
config = gui.Configuration(cfg.EvaluationType.Anova_2)


########################################################################################
# CLASS SheetAccess
#
# Access class for manipulation of a single excel sheet. This class will access the
# sheet with (row, column) indexing counting from 1.
#
class SheetAccess:

    COLUMN_IDS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #
    # Constructor
    #
    # @param sheet   DOM of the sheet to modify
    # @param strings DOM of the string reference list
    #
    def __init__(self, sheet, strings):
        self.sheet = sheet
        self.strings = strings

        self.row = 1
        self.column = 1

        self.cells = {}
        self.texts = []

        for s in strings.iter('si'):
            self.texts.append(s.find('t'))

        for cell in sheet.iter('c'):
            self.cells[cell.get('r')] = cell

    #
    # Get value of single cell
    #
    def __getitem__(self, key):

        cell = self.cells[key]

        #
        # Cells with string content are not containing the string itself but a
        # reference id into the string database.
        #
        if 't' in cell.attrib and cell.get('t') == 's':
            return self.texts[int(cell.find('v').text) + 1].text

        return cell.find('v').text

    #
    # Set value of single cell
    #

    def __setitem__(self, key, value):

        cell = self.cells[key]

        #
        # Setting a string value results in a new entry in the string database. The sheet
        # cell will reference this entry instead of keeping the string itself. This way old string
        # database entries will still be kept while being deprecated, but a cleanup is not simple here.
        # EXCEL might care for this when loading/saving the document again.
        #
        # The exact purpose of the ids (37, 43) is unknown.
        #
        if isinstance(value, str):
            cell.attrib['t'] = 's'
            cell.attrib['s'] = str(43)

            si = ET.SubElement(self.strings, 'si')
            t = ET.SubElement(si, 't')
            t.text = value

            self.texts.append(si)

            cell.find('v').text = str(len(self.texts) - 1)

        else:
            cell.attrib.pop('t', None)
            cell.attrib['s'] = str(37)
            cell.find('v').text = str(value)

    #
    # Initialize sequential write at a given cell
    #
    def init(self, id):
        self.row = int(id[1])
        self.column = SheetAccess.COLUMN_IDS.index(id[0]) + 1

    #
    # Write at current cell in sequential write setup
    #
    def write(self, value):
        self[self.getCellId(self.row, self.column)] = value
        self.column += 1

    #
    # Advance sequential write to next row
    #
    def next_row(self):
        self.column = 1
        self.row += 1

    #
    # Return string id of a row/column addressed cell (like 'D23')
    #
    def getCellId(self, row, column):

        assert column >= 1 and column <= len(SheetAccess.COLUMN_IDS)
        assert row >= 1

        return '{column_id}{row_id}'.format(column_id=SheetAccess.COLUMN_IDS[column - 1], row_id=row)


#
# Fill import sheet with the data from a single element
#
def fill_import_sheet(access, element):

    def get_project_keyword(keyword):
        try:
            return str(gom.app.project.get(keyword))
        except:
            pass
        return ''

    #
    # Fill appraiser / trial / part lists up to the maximum number of supported items
    #
    appraisers = copy.copy(config.appraisers)
    appraisers.extend(max(0, (NUMBER_OF_APPRAISERS - len(appraisers))) * [NONE])

    trials = copy.copy(config.trials)
    trials.extend(max(0, (NUMBER_OF_TRIALS - len(trials))) * [NONE])

    parts = copy.copy(config.parts)
    parts.extend(max(0, (NUMBER_OF_PARTS - len(parts))) * [NONE])

    #
    # Row 1: General element information
    #
    type = msa.get_element_type(element)

    # Nominal value. This is always '0.0' because we are computing with deviations.
    access['B1'] = 0.0
    access['D1'] = element.get(msa.get_tolerance_types(type)[1])  # Upper tolerance limit
    access['E1'] = element.get(msa.get_tolerance_types(type)[0])  # Lower tolerance limit

    unit = element.get('format ({token}, "", show_unit=true)'.format(token=msa.get_result_type(type))).split(' ')
    access['G1'] = unit[-1] if len(unit) > 1 else ''

    access['J1'] = gom.app.project.inspection[cfg.sigma_tag].value

    #
    # Row 3: Appraiser names
    #
    access.init('B3')

    for appraiser in appraisers:
        for _ in trials:
            access.write(appraiser)

    #
    # Row 4: Trial names
    #
    access.init('A4')
    access.write(element.name)

    for _ in appraisers:
        for trial in trials:
            access.write(trial)

    #
    # Row 5...n: Part data
    #
    access.init('A5')

    for part in parts:

        access.write(part)

        for appraiser in appraisers:
            for trial in trials:
                if appraiser != NONE and trial != NONE and part != NONE:
                    access.write(element.get(msa.create_stage_access_expression(
                        config, appraiser, part, trial, msa.get_element_type(element))))
                else:
                    access.write(NONE)

        access.next_row()

    #
    # Project keywords
    #

    access['B31'] = get_project_keyword('user_system')
    access['B32'] = get_project_keyword('user_location')
    access['B33'] = ''  # Description
    access['B34'] = ''  # Number
    access['B35'] = get_project_keyword('user_date')
    access['B36'] = get_project_keyword('user_inspector')
    access['B37'] = ''  # Comment


#
# Scan through document and remove the value entries in fields which use formulas.
# Only this way, the sheet will be recomputed after loading if in EXCEL.
#
def remove_precomputed_values(root):

    for cell in root.iter('c'):
        if cell.find('f') is not None:

            value = cell.find('v')

            if value is not None:
                cell.remove(value)

#
# Extract the namespace defining 'worksheet' header from sheet document
#


def extract_worksheet_header(text):
    worksheet_header = re.search('<worksheet[^>]*>', text).group(0)
    text = re.sub('<worksheet[^>]*>', '<worksheet>', text)
    text = re.sub('(\w):(\w)', r'\1__NS__\2', text)

    return (worksheet_header, text)

#
# Re-insert the namespace defining 'worksheet' header into the sheet document
#


def insert_worksheet_header(text, worksheet_header):
    text = re.sub('(\w)__NS__(\w)', r'\1:\2', text)
    text = re.sub('<worksheet>', worksheet_header, text)

    return text


########################################################################
# MAIN
#
#
# Show configuration dialog
#
elements = None

CONFIGURATION_DIALOG = gom.script.sys.create_user_defined_dialog(content='<dialog>'
                                                                 ' <title>Export MSA As Excel Sheet</title>'
                                                                 ' <style></style>'
                                                                 ' <control id="OkCancel"/>'
                                                                 ' <position></position>'
                                                                 ' <embedding></embedding>'
                                                                 ' <sizemode></sizemode>'
                                                                 ' <size height="242" width="552"/>'
                                                                 ' <content rows="4" columns="2">'
                                                                 '  <widget column="0" row="0" rowspan="1" type="input::checkbox" columnspan="1">'
                                                                 '   <name>use_custom_template</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <value>false</value>'
                                                                 '   <title>Use custom template</title>'
                                                                 '  </widget>'
                                                                 '  <widget column="1" row="0" rowspan="1" type="input::file" columnspan="1">'
                                                                 '   <name>template</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <type>file</type>'
                                                                 '   <title>Choose Template File</title>'
                                                                 '   <default></default>'
                                                                 '   <limited>true</limited>'
                                                                 '   <file_types>'
                                                                 '    <file_type description="Excel template" name="*.xlsx"/>'
                                                                 '   </file_types>'
                                                                 '   <file_types_default>*.xlsx</file_types_default>'
                                                                 '  </widget>'
                                                                 '  <widget column="0" row="1" rowspan="1" type="label" columnspan="1">'
                                                                 '   <name>file_label</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <text>Export Target</text>'
                                                                 '   <word_wrap>false</word_wrap>'
                                                                 '  </widget>'
                                                                 '  <widget column="1" row="1" rowspan="1" type="input::file" columnspan="1">'
                                                                 '   <name>file</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <type>any</type>'
                                                                 '   <title>Choose Output File</title>'
                                                                 '   <default></default>'
                                                                 '   <limited>true</limited>'
                                                                 '   <file_types>'
                                                                 '    <file_type description="Excel template" name="*.xlsx"/>'
                                                                 '   </file_types>'
                                                                 '   <file_types_default>*.xlsx</file_types_default>'
                                                                 '  </widget>'
                                                                 '  <widget column="0" row="2" rowspan="1" type="label" columnspan="2">'
                                                                 '   <name>message</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <text>0 elements selected</text>'
                                                                 '   <word_wrap>false</word_wrap>'
                                                                 '  </widget>'
                                                                 '  <widget column="0" row="3" rowspan="1" type="spacer::vertical" columnspan="2">'
                                                                 '   <name>spacer</name>'
                                                                 '   <tooltip></tooltip>'
                                                                 '   <minimum_size>0</minimum_size>'
                                                                 '   <maximum_size>-1</maximum_size>'
                                                                 '  </widget>'
                                                                 ' </content>'
                                                                 '</dialog>')

CONFIGURATION_DIALOG.template.value = TEMPLATE_FILE_NAME
CONFIGURATION_DIALOG.file.value = os.path.join(
    gom.app.default_directory, os.path.split(TEMPLATE_FILE_NAME.replace('_template', ''))[1])


def update_dialog(widget):
    global elements

    elements = [element for element in gom.ElementSelection({'category': ['key', 'elements', 'explorer_category', 'inspection']})
                if element.is_selected]

    CONFIGURATION_DIALOG.message.text = '{number} element(s) will be exported'.format(number=len(elements))
    CONFIGURATION_DIALOG.control.status = 'No elements selected' if len(elements) == 0 else ''

    CONFIGURATION_DIALOG.template.enabled = CONFIGURATION_DIALOG.use_custom_template.value


CONFIGURATION_DIALOG.handler = update_dialog

update_dialog(None)

CONFIGURATION = gom.script.sys.show_user_defined_dialog(dialog=CONFIGURATION_DIALOG)

tempdir_gom_template = tempfile.mkdtemp()
assert tempdir_gom_template is not None

# In packages, the System Resources (like data/msa_template.xlsx) are only available in memory.
# If the user decided to use the builtin template, we copy it in a temp folder,
# making the rest of the script compatible.
templatefilename = ""
if not CONFIGURATION.use_custom_template:
    templatefilename = tempdir_gom_template + "/msa_template.xlsx"
    newFile = open(templatefilename, "wb")
    newFile.write(gom.app.resource["data/msa_template.xlsx"])
    newFile.close()
else:
    templatefilename = CONFIGURATION.template

#
# For each element a separate EXCEL sheet is created. If more than one element is present, a postfix is added.
#
for element in elements:

    tempdir = tempfile.mkdtemp()
    assert tempdir is not None

    filename = CONFIGURATION.file

    if len(elements) > 1:
        filename, ext = os.path.splitext(filename)
        filename = '{name}_{postfix}{extension}'.format(name=filename, postfix=element.name, extension=ext)

    try:
        #
        # Unzip XSLX file into the temp directory
        #
        with zipfile.ZipFile(templatefilename, 'r') as zip_file:
            zip_file.extractall(tempdir)

        #
        # Read import sheet XML representation.
        #
        # Because xml.etree does not get along well with namespaces, the namespace attributes
        # are removed manually and the original worksheet header is kept for adding it again
        # later.
        #
        with open(os.path.join(tempdir, IMPORT_SHEET_FILE_NAME), 'r') as file:
            worksheet_header, text = extract_worksheet_header(file.read())
            import_root = ET.fromstring(text)

        #
        # Read string reference XML represenration.
        #
        # The namespace problem is handled here, too, as described above. This file contains some
        # kind of string database which entries are referenced from the sheets cells.
        #
        with open(os.path.join(tempdir, STRINGS_FILE_NAME), 'r') as file:
            text = file.read()
            strings_header = re.search('<sst[^>]*>', text).group(0)
            text = re.sub('<sst[^>]*>', '<sst>', text)
            text = re.sub('(\w):(\w)', r'\1__NS__\2', text)

            strings_root = ET.fromstring(text)

        #
        # Fill import sheet with the element data
        #
        access = SheetAccess(import_root, strings_root)
        fill_import_sheet(access, element)

        #
        # Convert back into string representation and add the original worksheet header
        # containig the namespace definitions again.
        #
        with open(os.path.join(tempdir, IMPORT_SHEET_FILE_NAME), 'w') as file:
            file.write(insert_worksheet_header(str(ET.tostring(import_root), 'utf-8'), worksheet_header))

        #
        # Adapt data sheet
        #
        # The pre computed values have to be removed from the cells here to trigger a recomputation
        # when the generated document is imported into EXCEL.
        #
        with open(os.path.join(tempdir, DATA_SHEET_FILE_NAME), 'r') as file:
            worksheet_header, text = extract_worksheet_header(file.read())
            data_root = ET.fromstring(text)

        remove_precomputed_values(data_root)

        with open(os.path.join(tempdir, DATA_SHEET_FILE_NAME), 'w') as file:
            file.write(insert_worksheet_header(str(ET.tostring(data_root), 'utf-8'), worksheet_header))

        #
        # Adapt calculation sheet
        #
        with open(os.path.join(tempdir, CALCULATION_SHEET_FILE_NAME), 'r') as file:
            worksheet_header, text = extract_worksheet_header(file.read())
            calculation_root = ET.fromstring(text)

        remove_precomputed_values(calculation_root)

        with open(os.path.join(tempdir, CALCULATION_SHEET_FILE_NAME), 'w') as file:
            file.write(insert_worksheet_header(str(ET.tostring(calculation_root), 'utf-8'), worksheet_header))

        #
        # When writing the string reference, the headers attributes have to be adapted
        #
        with open(os.path.join(tempdir, STRINGS_FILE_NAME), 'w') as file:
            text = str(ET.tostring(strings_root), 'utf-8')
            text = re.sub('(\w)__NS__(\w)', r'\1:\2', text)

            strings_header = re.sub('count="\d*"', 'count="{size}"'.format(size=len(access.texts) + 5), strings_header)
            strings_header = re.sub('uniqueCount="\d*"',
                                    'uniqueCount="{size}"'.format(size=len(access.texts) + 5), strings_header)

            text = re.sub('<sst>', strings_header, text)

            #print (minidom.parseString (text).toprettyxml (indent='  '))

            file.write(text)

        #
        # Pack everything into a XSLX ZIP file again
        #
        if not filename.endswith('.xlsx'):
            filename += '.xlsx'

        if os.path.exists(filename):
            os.remove(filename)

        shutil.make_archive(filename, 'zip', tempdir)
        shutil.move(filename + '.zip', filename)

    finally:
        shutil.rmtree(tempdir)

shutil.rmtree(tempdir_gom_template)
