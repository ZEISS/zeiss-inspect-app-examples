# -*- coding: utf-8 -*-
#
# msa_arm - Script for generating an MSA (ARM) evaluation
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

import gom
import xml.etree
import xml.etree.ElementTree as ET
import xml.dom.minidom

import Tools.MeasurementSystemAnalysis.msa_config as cfg
import Tools.MeasurementSystemAnalysis.msa_lib as msa
import Tools.MeasurementSystemAnalysis.msa_gui as gui


# ----------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------

#
# Display name of the table template for ARM evaluations
#
TABLE_TEMPLATE_NAME_ARM = 'MSA (ARM)'

#
# UTF-8 symbol for a black circle
#
EMPTY_SYMBOL = '&#x25CF;'

# ---------------------------------------------------------------------------------------
# Functions needed for ARM expression and template building
# ---------------------------------------------------------------------------------------

#
# Build stage ranges matching the project setup
#


def create_arm_stage_ranges(config):

    #
    # Stage range set 1: Stage ranges for appraiser/part combinations
    #
    for appraiser in config.appraisers:
        for part in config.parts:
            msa.create_stage_range(appraiser, part, None)

    #
    # Stage range set 2: Stage ranges for appraiser/trial combinations
    #
    for appraiser in config.appraisers:
        for trial in config.trials:
            msa.create_stage_range(appraiser, None, trial)

    #
    # Stage range set 3: Stage range covering all stages associated with a single appraiser
    #
    for appraiser in config.appraisers:
        msa.create_stage_range(appraiser, None, None)

    #
    # Stage range set 4: Stage ranges covering all stages associated with a single part
    #
    for part in config.parts:
        msa.create_stage_range(None, part, None)


#
# Generate table template matching the current element setup
#
def create_arm_table_template(template_name, config):

    #
    # Root node
    #
    root = ET.Element('tabletemplates')
    root.attrib['dynamic_stage_support'] = 'none'
    root.attrib['view_mode'] = 'report_template'
    root.attrib['expanding_column'] = '0'
    root.attrib['name'] = template_name
    root.attrib['dynamic_column_for_stages'] = '-1'
    root.attrib['version'] = '2'

    #
    # Table headers
    #
    header_texts = ['Appraiser', 'Trial']
    header_texts.extend(map(lambda part: 'Part {0}'.format(part), config.parts))
    header_texts.append('Avg.')
    root.attrib['columns'] = str(len(header_texts))

    headers = ET.SubElement(root, 'headers')

    count = 0
    for text in header_texts:
        msa.create_column_header(headers, count, text)
        count += 1

    #
    # Entries for the single element types
    #
    for type in config.types:
        template = ET.SubElement(root, 'template')
        template.attrib['dynamic_row_for_stages'] = '-1'
        template.attrib['rows'] = str(1 + len(config.appraisers) * (len(config.trials) + 2) + 1 + 1 + 1)
        template.attrib['element_type'] = type

        row_index = 0

        #
        # Header row
        #
        element_header = ET.SubElement(template, 'row')
        element_header.attrib['index'] = str(row_index)
        row_index += 1

        msa.create_cell_raw(element_header, 0, '$icon (explorer_type_and_state)$ <b>$name$</b>',
                            str(3 + len(config.parts)))

        #
        # One block per appraiser
        #
        appraiser_avg_exp = []
        appraiser_range_exp = []

        for appraiser in config.appraisers:

            #
            # One row per trail
            #
            for trial in config.trials:
                row = ET.SubElement(template, 'row')
                row.attrib['index'] = str(row_index)
                row_index += 1

                #
                # First columns containing appraiser/trial information
                #
                col_index = 0
                col_index = msa.create_cell_raw(row, col_index, appraiser, 1)
                col_index = msa.create_cell_raw(row, col_index, trial, 1)

                #
                # Inner part matrix
                #
                for part in config.parts:
                    col_index = msa.create_cell(row, col_index, 'Stage value', msa.create_stage_access_expression(
                        config, appraiser, part, trial, type), 1)

                #
                # Last column containing the average sums
                #
                col_index = msa.create_cell(row, col_index, 'Avg.', msa.create_restricted_avg_expression(
                    config, appraiser, None, trial, type), 1)

            avg_summary = ET.SubElement(template, 'row')
            avg_summary.attrib['index'] = str(row_index)
            row_index += 1

            col_index = 0
            col_index = msa.create_cell_raw(avg_summary, col_index, msa.italic('Average'), 1)
            col_index = msa.create_cell_raw(avg_summary, col_index, '', 1)

            exp = []
            for part in config.parts:
                exp.append(msa.create_restricted_avg_expression(config, appraiser, part, None, type))
                col_index = msa.create_cell_raw(avg_summary, col_index,
                                                msa.italic(msa.overlined_var_name('X', '{0}.{1}.{2}'.format(appraiser, part, EMPTY_SYMBOL)) +
                                                           msa.quote(exp[-1])), 1)

            col_index = msa.create_cell_raw(avg_summary, col_index,
                                            msa.italic(msa.overlined_var_name('X', '{0}.{1}.{2}'.format(appraiser, EMPTY_SYMBOL, EMPTY_SYMBOL)) +
                                                       msa.quote(msa.create_average_expression(exp))), 1)

            appraiser_avg_exp.append(exp)

            range_summary = ET.SubElement(template, 'row')
            range_summary.attrib['index'] = str(row_index)
            row_index += 1

            col_index = 0
            col_index = msa.create_cell_raw(range_summary, col_index, msa.italic('Range'), 1)
            col_index = msa.create_cell_raw(range_summary, col_index, '', 1)

            exp = []
            for part in config.parts:
                exp.append(msa.create_restricted_range_expression(config, appraiser, part, None, type))
                col_index = msa.create_cell_raw(range_summary, col_index,
                                                msa.italic(msa.overlined_var_name('R', '{0}.{1}.{2}'.format(appraiser, part, EMPTY_SYMBOL)) +
                                                           msa.quote(exp[-1])), 1)

            col_index = msa.create_cell_raw(range_summary, col_index,
                                            msa.italic(msa.overlined_var_name('R', '{0}.{1}.{2}'.format(appraiser, EMPTY_SYMBOL, EMPTY_SYMBOL)) +
                                                       msa.quote(msa.create_range_expression(exp))), 1)

            appraiser_range_exp.append(exp)

        part_summary = ET.SubElement(template, 'row')
        part_summary.attrib['index'] = str(row_index)
        row_index += 1

        col_index = 0
        col_index = msa.create_cell_raw(part_summary, col_index, msa.italic('Part avg.'), 1)
        col_index = msa.create_cell_raw(part_summary, col_index, '', 1)

        exp = []

        for part in config.parts:
            exp.append(msa.create_restricted_avg_expression(config, None, part, None, type))
            col_index = msa.create_cell_raw(part_summary, col_index,
                                            msa.italic(msa.overlined_var_name('X', '{0}.{1}.{2}'.format(EMPTY_SYMBOL, part, EMPTY_SYMBOL)) +
                                                       msa.quote(exp[-1])), 1)

        col_index = msa.create_cell_raw(part_summary, col_index,
                                        msa.italic(msa.overlined_var_name('X', '{0}.{1}.{2}'.format(EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL)) +
                                                   msa.quote(msa.create_average_expression(exp))), 1)

        #
        # Compute overall average value
        #
        summary_x = ET.SubElement(template, 'row')
        summary_x.attrib['index'] = str(row_index)
        row_index += 1

        col_index = 0
        col_index = msa.create_cell_raw(summary_x, col_index, msa.italic('Summary'), 1)
        col_index = msa.create_cell_raw(summary_x, col_index, '', 1)

        for part in config.parts:
            col_index = msa.create_cell_raw(summary_x, col_index, '', 1)

        x_avg_exp = ''
        separator = ''
        for exp in appraiser_avg_exp:
            x_avg_exp = x_avg_exp + separator + msa.create_average_expression(exp)
            separator = ', '

        x_avg_exp = 'max ({0}) - min ({1})'.format(x_avg_exp, x_avg_exp)

        col_index = msa.create_cell_raw(summary_x, col_index,
                                        msa.italic(msa.overlined_var_name('X', 'diff')) +
                                        msa.quote(x_avg_exp), 1)

        #
        # Compute overall range value
        #
        summary_r = ET.SubElement(template, 'row')
        summary_r.attrib['index'] = str(row_index)
        row_index += 1

        col_index = 0
        col_index = msa.create_cell_raw(summary_r, col_index, '', 1)
        col_index = msa.create_cell_raw(summary_r, col_index, '', 1)

        for part in config.parts:
            col_index = msa.create_cell_raw(summary_r, col_index, '', 1)

        r_sum_exp = ''
        separator = ''
        for exp in appraiser_range_exp:
            r_sum_exp = r_sum_exp + separator + msa.create_range_expression(exp)
            separator = ' + '

        r_sum_exp = '({0}) / {1}'.format(r_sum_exp, len(appraiser_range_exp))

        col_index = msa.create_cell_raw(summary_r, col_index,
                                        msa.italic(msa.overlined_var_name('R', 'all')) +
                                        msa.quote(r_sum_exp), 1)

    return xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()


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
config = gui.Configuration(cfg.EvaluationType.Arm)
config.edit(show_sigma_input=False)

msa.create_common_stage_ranges(config)
create_arm_stage_ranges(config)
template_content = create_arm_table_template(TABLE_TEMPLATE_NAME_ARM, config)
msa.import_table_template(template_content, '01a35fd4-1a98-4752-b1be-d21a3e6446ef')

gom.script.view.set_tab_visible(view='table', visible=True)

gom.script.table.switch_template(name=TABLE_TEMPLATE_NAME_ARM)
