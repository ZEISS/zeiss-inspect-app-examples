# -*- coding: utf-8 -*-
#
# msa_solara_mp - Script for generating an MSA setup for exports
#
# This script generates table templates displaying the MSA relevant values in a way that
# the content can be copy/pasted easily into third party statistics tools for further evaluations.
#
# The table cells will contain a parametric computation for the values in question.
# This means the values will adapt whenever preconditions are changing *except* the
# number or names of the appraisers, parts and trials. So the script must be executed
# again if, e.g., stages are added or an appraiser is renamed. It does not need to
# be executed again if the checks or stages are edited in any other way.
#
# Carl Zeiss GOM Metrology GmbH, 2025
#

import gom
import xml.etree.ElementTree as ET
from defusedxml import minidom

import Tools.MeasurementSystemAnalysis.msa_lib as msa
import Tools.MeasurementSystemAnalysis.msa_config as cfg
import Tools.MeasurementSystemAnalysis.msa_gui as gui


# ----------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------

#
# Display name of the table template for exports
#
TABLE_TEMPLATE_NAME_EXPORT = 'MSA (export)'


# ----------------------------------------------------------------------------------
# Functions needed to generate an export template
# ----------------------------------------------------------------------------------

#
# Generate table template matching the current element setup
#
def create_export_table_template(template_name, config):

    #
    # Generate root node
    #
    root = ET.Element('tabletemplates')
    root.attrib['dynamic_stage_support'] = 'none'
    root.attrib['view_mode'] = 'report_template'
    root.attrib['expanding_column'] = '0'
    root.attrib['name'] = template_name
    root.attrib['dynamic_column_for_stages'] = '-1'
    root.attrib['version'] = '2'

    #
    # Generate table headers
    #
    # The number of headers must match the number of columns. So if cells are added below, the
    # header texts must be expanded appropriately.
    #
    header_texts = ['Part']
    for appraiser in config.appraisers:
        for trial in config.trials:
            header_texts.append('Appraiser / Trial')

    root.attrib['columns'] = str(len(header_texts))

    headers = ET.SubElement(root, 'headers')

    count = 0
    for text in header_texts:
        msa.create_column_header(headers, count, text)
        count += 1

    #
    # Generate one entry for each element type
    #
    for type in config.types:
        template = ET.SubElement(root, 'template')
        template.attrib['dynamic_row_for_stages'] = '-1'
        template.attrib['rows'] = str(1 + len(config.parts))
        template.attrib['element_type'] = type

        #
        # Top row: Element name and entry description
        #
        row_index = 0
        row = ET.SubElement(template, 'row')
        row.attrib['index'] = str(row_index)

        col_index = msa.create_cell_raw(row, 0, '$icon (explorer_type_and_state)$ <b>$name$</b>', 1)

        for appraiser in config.appraisers:
            for trial in config.trials:
                col_index = msa.create_cell_raw(row, col_index, '{0} / {1}'.format(appraiser, trial), 1)

        row_index += 1

        #
        # One row per part
        #
        for part in config.parts:

            row = ET.SubElement(template, 'row')
            row.attrib['index'] = str(row_index)

            #
            # Every appraiser / trial combination leads to a cell
            #
            col_index = msa.create_cell(row, 0, 'Part', 'return "{0}"\n'.format(part), 1)

            for appraiser in config.appraisers:
                for trial in config.trials:
                    description = '{0}.{1}.{2}'.format(appraiser, part, trial)
                    col_index = msa.create_cell(row, col_index, description, msa.create_stage_access_expression(
                        config, appraiser, part, trial, type), 1)

            row_index += 1

    return minidom.parseString(ET.tostring(root)).toprettyxml()


# ----------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------

msa.check_project_setup()

#
# Hiding the table widget will speed the script up dramatically
#
gom.script.view.set_tab_visible(view='table', visible=False)

#
# Setup configuration
#
config = gui.Configuration(cfg.EvaluationType.Export
                           )
config.edit(show_sigma_input=False)

template_content = create_export_table_template(TABLE_TEMPLATE_NAME_EXPORT, config)
msa.import_table_template(template_content, '5d7198c6-31a0-4118-9110-e6eafb084501')

gom.script.view.set_tab_visible(view='table', visible=True)

gom.script.table.switch_template(name=TABLE_TEMPLATE_NAME_EXPORT)
