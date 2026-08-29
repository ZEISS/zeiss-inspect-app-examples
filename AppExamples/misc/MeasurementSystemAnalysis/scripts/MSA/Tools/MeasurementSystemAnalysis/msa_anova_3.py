# -*- coding: utf-8 -*-
#
# msa_anova_3 - Script for generating an MSA ANOVA-3 evaluation
#
# This script generates a table template the ANOVA Type-3 values needed for MSA / Gauge R&R
# evaluations.
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
import msa_lib as msa
import msa_gui as gui
import msa_config as cfg


# ----------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------

#
# Display name of the table template for ARM evaluations
#
TABLE_TEMPLATE_NAME_ANOVA_3 = 'MSA (ANOVA type 3)'


# ---------------------------------------------------------------------------------------
# Functions needed for ANOVA Type-3 expression and template building
# ---------------------------------------------------------------------------------------

#
# Build stage ranges matching the project setup
#
def create_anova_3_stage_ranges(config):

    for part in config.parts:
        msa.create_stage_range(None, part, None)
        for trial in config.trials:
            msa.create_stage_range(None, part, trial)

#
# Create ANOVA 3 expression variable name
#
def create_anova_3_var_name(appraiser, part, trial):
    return 'X_{0}_{1}'.format(part + 1 if part != None else 'x',
                              trial + 1 if trial != None else 'x')

#
# Create expression to compute sum (E)
#
def create_anova_3_sum_e_expression(config, type):

    text = ''
    text += 'E = 0\n'

    count_p = 0
    for part in config.parts:

        Xxpx = create_anova_3_var_name(None, count_p, None)
        text += '{0} = {1}\n'.format(Xxpx, msa.create_restricted_avg_expression(config, None, part, None, type))

        count_t = 0
        for trial in config.trials:

            Xxpt = create_anova_3_var_name(None, count_p, count_t)
            text += '{0} = {1}\n'.format(Xxpt, msa.create_restricted_avg_expression(config, None, part, trial, type))

            term = '({0} - {1})'.format(Xxpt, Xxpx)
            text += 'E = E + {0} * {0}\n'.format(term, term)

            count_t += 1

        count_p += 1

    return text

#
# Create expression to compute ANOVA Type-3 R&R value
#
# This function generates the complete expression for a table cell necessary to
# compute the final R&R value
#
def create_anova_3_rr_expression(type, config):
    text = """
bypart = {{}}
bytrial = {{}}
byPandT = {{}}

par_element = gom.app.project.actual_elements['{part}']
tri_element = gom.app.project.actual_elements['{trial}']
sigma_element = gom.app.project.inspection['{sigma}']

for stage in gom.app.project.stage_markers['All stages'].used_stages:

    part  = with_context (stage=stage, par_element.value)
    trial = with_context (stage=stage, tri_element.value)

    if part not in bypart:
        t = []
    else:
        t = bypart[part]
    t.append (stage)
    bypart[part] = t

    if trial not in bytrial:
        t = []
    else:
        t = bytrial[trial]
    t.append (stage)
    bytrial[trial] = t

    if part not in byPandT:
        byPandT.insert (part,{{}})
    submap = byPandT[part]
    if trial not in submap:
        t = []
    else:
        t = submap[trial]
    t.append (stage)  
    submap[trial] = t    
    byPandT[part] = submap

t = len (bypart)
w = len (bytrial)  
sigma_factor = sigma_element.value 

E = 0
for _part in bypart:
    part_avg = avg ({result}, index = bypart[_part])
    for _trial in bytrial:
            pt_avg = avg ({result}, index = byPandT[_part][_trial])
            term = pt_avg - part_avg
            E = E + (term * term)

f = t * (w - 1)

s2e = E / f
EV = sigma_factor * sqr (s2e)
RR = EV 
"""
    return text.format(
        result=msa.get_result_type(type),
        sigma=cfg.sigma_tag,
        appraiser=cfg.appraiser_tag,
        part=cfg.part_tag,
        trial=cfg.trial_tag)


#
# Generate table template matching the current element setup
#
def create_anova_3_table_template(template_name, config):

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
    header_texts = ['Element', 'EV', 'RR', 'Sigma', 'EV [%]', 'RR [%]', 'Tol.']
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
        template.attrib['rows'] = '1'
        template.attrib['element_type'] = type

        row = ET.SubElement(template, 'row')
        row.attrib['index'] = '0'

        #
        # Fill entry columns. The number of cells here must match the number of header texts above.
        #
        gauge_rr_expression = create_anova_3_rr_expression(type, config)

        col_index = 0
        col_index = msa.create_cell_raw(row, col_index, '$icon (explorer_type_and_state)$ <b>$name$</b>', 1)
        col_index = msa.create_cell(row, col_index, 'EV', gauge_rr_expression + "return sqr (s2e)\n", 1)
        col_index = msa.create_cell(row, col_index, 'RR', gauge_rr_expression, 1)
        col_index = msa.create_cell(row, col_index, 'Sigma',
                                    'gom.app.project.inspection[\'{element}\'].value'.format(element=cfg.sigma_tag), 1)
        col_index = msa.create_cell(
            row, col_index, 'EV [%]', gauge_rr_expression + msa.create_percent_expression(type, 'sqr (s2e)'), 1)
        col_index = msa.create_cell(
            row, col_index, 'RR [%]', gauge_rr_expression + msa.create_percent_expression(type, 'RR'), 1)
        col_index = msa.create_cell(row, col_index, 'Tol.', msa.get_tolerance_expression(type), 1)

    return minidom.parseString(ET.tostring(root)).toprettyxml()


# ----------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------

msa.check_project_setup()

#
# Hiding the table widget will speed the script up dramatically
#
gom.script.view.set_tab_visible(view='table', visible=False)

try:
    gom.script.sys.close_stage_range()
except:
    pass

#
# Setup configuration
#
config = gui.Configuration(cfg.EvaluationType.Anova_3)
config.edit(show_sigma_input=True)

msa.create_common_stage_ranges(config, use_appraiser=False)
create_anova_3_stage_ranges(config)
template_content = create_anova_3_table_template(TABLE_TEMPLATE_NAME_ANOVA_3, config)
msa.import_table_template(template_content, 'e95e1e2d-075b-4b9d-bc00-6abddd13af89')

gom.script.view.set_tab_visible(view='table', visible=True)

gom.script.table.switch_template(name=TABLE_TEMPLATE_NAME_ANOVA_3)
