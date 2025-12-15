# -*- coding: utf-8 -*-
#
# msa_anova_2 - Script for generating a ANOVA-2 MSA setup
#
# This script generates table templates displaying the ARM values needed for
# MSA / Gauge R&R evaluations. The generated template contains an entry for each
# inspection element type present at script evaluation time.
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
import Tools.MeasurementSystemAnalysis.msa_config as cfg
import Tools.MeasurementSystemAnalysis.msa_lib as msa
import Tools.MeasurementSystemAnalysis.msa_gui as gui


# ----------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------

#
# Display name of the table template for ANOVA Type-2 evaluations
#
TABLE_TEMPLATE_NAME_ANOVA_2 = 'MSA (ANOVA type 2)'


# ---------------------------------------------------------------------------------------
# Functions needed for ANOVA Type-2 expression and template building
# ---------------------------------------------------------------------------------------

#
# Build stage ranges matching the project setup
#
def create_anova_2_stage_ranges(config):

    for appraiser in config.appraisers:
        for part in config.parts:
            msa.create_stage_range(appraiser, part, None)

    for appraiser in config.appraisers:
        msa.create_stage_range(appraiser, None, None)

    for part in config.parts:
        msa.create_stage_range(None, part, None)


#
# Create ANOVA 2 expression variable name
#
def create_anova_2_rr_expression(type, data):
    text = """
byappraiser = {{}}
bypart = {{}}
bytrial = {{}}
byAandP = {{}}

app_element = gom.app.project.actual_elements['{appraiser}']
par_element = gom.app.project.actual_elements['{part}']
tri_element = gom.app.project.actual_elements['{trial}']
sigma_element = gom.app.project.inspection['{sigma}']
all_stages = gom.app.project.stage_markers['All stages']

for stage in all_stages.used_stages:
	appraiser = with_context (stage=stage, app_element.value)
	if appraiser not in byappraiser:
		t = []
	else:
		t = byappraiser[appraiser]
	t.append (stage)
	byappraiser[appraiser] = t
		
	part = with_context (stage=stage, par_element.value)
	if part not in bypart:
		t = []
	else:
		t = bypart[part]
	t.append (stage)
	bypart[part] = t
	
	trial = with_context (stage=stage, tri_element.value)
	if trial not in bytrial:
		t = []
	else:
		t = bytrial[trial]
	t.append (stage)
	bytrial[trial] = t
	
	if appraiser not in byAandP:
		byAandP.insert (appraiser,{{}})
	submap = byAandP[appraiser]
	if part not in submap:
		t = []
	else:
		t = submap[part]
	t.append (stage)  
	submap[part] = t    
	byAandP[appraiser] = submap
	
p = len(byappraiser)
t = len(bypart)
w = len(bytrial)  
sigma_factor = sigma_element.value
 
total_avg = avg({result}, index=all_stages)

P = 0
for _appraiser in byappraiser:
	term = avg ({result}, index = byappraiser[_appraiser]) - total_avg
	P = P + (term * term) 
P = t * w * P

T = 0
for _part in bypart:
	term = avg ({result}, index = bypart[_part]) - total_avg
	T = T + (term * term)
T = p * w * T

PT = 0
for _appraiser in byappraiser:
	for _part in bypart:
		term = avg ({result}, index = byAandP[_appraiser][_part]) - avg ({result}, index = byappraiser[_appraiser]) - avg({result}, index = bypart[_part]) + total_avg
		PT = PT + (term * term)
PT = w * PT

E = 0
for _stage in gom.app.project.stage_markers['All stages'].used_stages:
	appraiser = with_context (stage=_stage, app_element.value)
	part = with_context (stage=_stage, par_element.value)
	term = with_context (stage=_stage, {result}) - avg ({result}, index = byAandP[appraiser][part])
	E = E + (term *  term)

f1 = p * t * (w - 1)
f2 = (p - 1) * (t - 1)
f3 = t - 1
f4 = p - 1

s2p = P / f4
s2t = T / f3
s2pt = PT / f2
s2e = E / f1
s2add = (E + PT) / (f1 + f2)

f_limit = f_table_value(f1,f2,0.05)
interaction = s2pt / s2e > f_limit

VE = not interaction ? s2add : s2e
VW = max ((s2pt - s2e) / w, 0)
VP = max (not interaction ? (s2p - s2add) / (t * w) : (s2p - s2pt) / (t * w), 0)
VT = max (not interaction ? (s2t - s2add) / (p * w) : (s2t - s2pt) / (p * w), 0)

EV = sigma_factor * sqr (VE)
AV = sigma_factor * sqr (VP)
IA = sigma_factor * sqr (VW)
PV = sigma_factor * sqr (VT)

RR  = not interaction ? sqr (EV * EV + AV * AV) : sqr (EV * EV + AV * AV + IA * IA)
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


def create_anova_2_table_template(template_name, config):

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
    header_texts = ['Element', 'PV', 'EV', 'AV', 'IA', 'RR', 'Sigma',
                    'PV [%]', 'EV [%]', 'AV [%]', 'IA [%]', 'RR [%]', 'Tol.']
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
        gauge_rr_expression = create_anova_2_rr_expression(type, config)

        col_index = 0
        col_index = msa.create_cell_raw(row, col_index, '$icon (explorer_type_and_state)$ <b>$name$</b>', 1)
        col_index = msa.create_cell(row, col_index, 'PV', gauge_rr_expression + "return sqr (VT)\n", 1)
        col_index = msa.create_cell(row, col_index, 'EV', gauge_rr_expression + "return sqr (VE)\n", 1)
        col_index = msa.create_cell(row, col_index, 'AV', gauge_rr_expression + "return sqr (VP)\n", 1)
        col_index = msa.create_cell(row, col_index, 'IA', gauge_rr_expression +
                                    "return not interaction ? 'pooled' : sqr (VW)\n", 1)
        col_index = msa.create_cell(row, col_index, 'RR', gauge_rr_expression +
                                    "return not interaction ? sqr (VE + VT) : sqr (VE * VT + VW)\n", 1)
        col_index = msa.create_cell(row, col_index, 'Sigma',
                                    'gom.app.project.inspection[\'{element}\'].value'.format(element=cfg.sigma_tag), 1)
        col_index = msa.create_cell(
            row, col_index, 'PV [%]', gauge_rr_expression + msa.create_percent_expression(type, "sqr (VT)"), 1)
        col_index = msa.create_cell(row, col_index, 'EV [%)', gauge_rr_expression +
                                    msa.create_percent_expression(type, "sqr (VE)"), 1)
        col_index = msa.create_cell(
            row, col_index, 'AV [%]', gauge_rr_expression + msa.create_percent_expression(type, "sqr (VP)"), 1)
        col_index = msa.create_cell(row, col_index, 'IA [%]', gauge_rr_expression +
                                    msa.create_percent_expression(type, "sqr (VW)", "not interaction ? '' :"), 1)
        col_index = msa.create_cell(
            row, col_index, 'GRR [%]', gauge_rr_expression + msa.create_percent_expression(type, "RR"), 1)
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
config = gui.Configuration(cfg.EvaluationType.Anova_2)
config.edit(show_sigma_input=True)

msa.create_common_stage_ranges(config)
create_anova_2_stage_ranges(config)

template_content = create_anova_2_table_template(TABLE_TEMPLATE_NAME_ANOVA_2, config)
msa.import_table_template(template_content, 'd2e09184-3bd0-4cf2-abdb-e935464593cb')

gom.script.view.set_tab_visible(view='table', visible=True)

gom.script.table.switch_template(name=TABLE_TEMPLATE_NAME_ANOVA_2)
