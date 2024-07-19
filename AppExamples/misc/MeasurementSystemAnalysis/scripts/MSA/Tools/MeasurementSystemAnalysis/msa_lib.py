# -*- coding: utf-8 -*-
#
# msa_lib - Common library functions for generating MSA / Gauge R&R setups
#

import gom
import os
import os.path
import re
import xml.etree
import xml.etree.ElementTree as ET
import xml.dom.minidom
import stringprep

import Tools.MeasurementSystemAnalysis.msa_config as cfg

# ----------------------------------------------------------------------------------
# Pre checking
# ----------------------------------------------------------------------------------

#
# Check various project properties to guarantee a smooth run
#


def check_project_setup():
    #
    # Temporal directory has to exists for table template writing/import
    #
    if not os.path.exists(gom.app.temp_directory):
        raise RuntimeError('Temporary directory "{0}" does not exist.'.format(gom.app.temp_directory))

    #
    # Project must be loaded
    #
    project_loaded = False

    try:
        gom.app.project.name
        project_loaded = True
    except:
        pass

    if not project_loaded:
        raise RuntimeError('No project found.')

    #
    # We need at least some stages
    #
    if len(gom.app.project.stages) == 0:
        raise RuntimeError('No stages are present at all.')


# ----------------------------------------------------------------------------------
# General auxillary functions
# ----------------------------------------------------------------------------------

#
# Check if an element has the 'automatically created' flag set
#
def is_automatically_created(element):
    result = False

    try:
        result = int(element.__getattr__('user_{0}'.format(cfg.automatically_created_tag))) == 1
    except:
        pass

    return result

#
# Tag element with 'automatically created' flag
#


def tag_as_automatically_created(element):
    gom.script.cad.edit_element_keywords(
        add_keys=[cfg.automatically_created_tag],
        description={cfg.automatically_created_tag: 'Automatically created by Gauge R&R script'},
        elements=[element],
        set_value={cfg.automatically_created_tag: '1'})

#
# Check if a stage range already exists
#


def stage_range_exists(name):
    exists = True

    try:
        gom.app.project.stage_markers[name]
    except:
        exists = False

    return exists


#
# Create stage range for a set matching an appraiser/part/trial triple and mark it as automatically created
#
# @param appraiser Name of the appraiser or 'None' if the range should cover all appraisers
# @param part      Name of the part or 'None' if the range should cover all parts
# @param trial     Name of the trial or 'None' if the range should cover all trials
# @return Created stage range
#
def create_stage_range(appraiser, part, trial):
    checks = []

    inputs = {}

    if appraiser != None:
        checks.append('APPRAISER.actual.value == "{0}"'.format(appraiser))
        inputs['APPRAISER'] = gom.app.project.actual_elements[cfg.appraiser_tag]
    if part != None:
        checks.append('PART.actual.value == "{0}"'.format(part))
        inputs['PART'] = gom.app.project.actual_elements[cfg.part_tag]
    if trial != None:
        checks.append('TRIAL.actual.value == "{0}"'.format(trial))
        inputs['TRIAL'] = gom.app.project.actual_elements[cfg.trial_tag]

    stage_range = None
    name = get_stage_range_name(appraiser, part, trial)
    expression = ' and '.join(checks)

    if not stage_range_exists(name):
        stage_range = gom.script.sys.create_stage_range_by_expression(
            expression=expression,
            inputs=inputs,
            is_visible_in_diagram=True,
            name=name)

        gom.script.cad.hide_element(elements=[stage_range])

        tag_as_automatically_created(stage_range)

    elif gom.app.project.stage_markers[name].expression.strip() != expression:
        raise RuntimeError('Stage range "{0}" already exists but has different expression'.format(name))

    return stage_range


#
# Create stage ranges common for all evaluations
#
def create_common_stage_ranges(data, use_appraiser=True):

    def make_string_list(list):
        return ','.join("'{0}'".format(x) for x in list)

    #
    # Create stage range covering all stages
    #
    inputs = {}
    if use_appraiser:
        inputs['APPRAISER'] = gom.app.project.actual_elements[cfg.appraiser_tag]
    inputs['PART'] = gom.app.project.actual_elements[cfg.part_tag]
    inputs['TRIAL'] = gom.app.project.actual_elements[cfg.trial_tag]

    all_stages_range_expression = ''
    if use_appraiser:
        all_stages_range_expression += "APPRAISER.actual.value in [{appraiser_list}] and "

    all_stages_range_expression += "PART.actual.value in [{part_list}] and TRIAL.actual.value in [{trial_list}]"
    if use_appraiser:
        all_stages_range_expression = all_stages_range_expression.format(appraiser_list=make_string_list(data.appraisers),
                                                                         part_list=make_string_list(data.parts),
                                                                         trial_list=make_string_list(data.trials))
    else:
        all_stages_range_expression = all_stages_range_expression.format(part_list=make_string_list(data.parts),
                                                                         trial_list=make_string_list(data.trials))

    try:
        if (is_automatically_created(gom.app.project.stage_markers[cfg.all_stages_range_name])):
            gom.script.cad.delete_element(elements=[gom.app.project.stage_markers[cfg.all_stages_range_name]])
    except:
        pass

    if not stage_range_exists(cfg.all_stages_range_name):

        range = gom.script.sys.create_stage_range_by_expression(
            expression=all_stages_range_expression,
            inputs=inputs,
            is_visible_in_diagram=False,
            name=cfg.all_stages_range_name)

        gom.script.cad.hide_element(elements=[range])

        tag_as_automatically_created(range)

    else:
        range = gom.app.project.stage_markers[cfg.all_stages_range_name]

        if range.expression.strip() != all_stages_range_expression.strip():
            gom.script.sys.edit_creation_parameters(
                auto_apply=True,
                element=range,
                expression=all_stages_range_expression)

#
# Quote expression so that it can be used in a table template cell
#


def quote(expression):
    return '$' + expression + '$'

#
# Add token replacement comment to expression
#


def create_comment(text, expression):
    return '#@ {0}\n{1}'.format(text, expression)


#
# Add table template via XML import
#
# @param content Table content in XML format
#
def import_table_template(content, uuid_template):

    template_file_name = os.path.join(gom.app.temp_directory, 'msa_table_template.xml')

    with open(template_file_name, 'wb') as file:
        file.write(content.encode('UTF-8'))
        file.close()

    gom.script.table.import_table_template(file=template_file_name,
                                           uuid=uuid_template)

#
# Construct stage name from a appraiser/part/trial triple
#


def get_stage_name(data, appraiser, part, trial):

    assert appraiser != None
    assert part != None
    assert trial != None

    return data.stages[(appraiser, part, trial)].name

#
# Construct name for stage range addressing an appraiser/part/trail combination
#


def get_stage_range_name(appraiser, part, trial):
    if appraiser != None and part == None and trial == None:
        return 'Appraiser {0}'.format(appraiser)
    if appraiser == None and part != None and trial == None:
        return 'Part {0}'.format(part)
    if appraiser == None and part == None and trial != None:
        return 'Trial {0}'.format(trial)
    if appraiser == None and part != None and trial != None:
        return 'Part {0} / Trial {1}'.format(part, trial)
    if appraiser != None and part == None and trial != None:
        return 'Appraiser {0} / Trial {1}'.format(appraiser, trial)
    if appraiser != None and part != None and trial == None:
        return 'Appraiser {0} / Part {1}'.format(appraiser, part)

    return '{0}.{1}.{2}'.format(appraiser if appraiser != None else 'x',
                                part if part != None else 'x',
                                trial if trial != None else 'x')


def create_item_filter(keyword_name, value):
    return 'gom.app.project.actual_elements["{0}"].input_value == "{1}"'.format(keyword_name, value)


def create_stage_filter(appraiser, part, trial):
    parts = []
    if appraiser:
        parts.append(create_item_filter(cfg.appraiser_tag, appraiser))
    if part:
        parts.append(create_item_filter(cfg.part_tag, part))
    if trial:
        parts.append(create_item_filter(cfg.trial_tag, trial))
    return " and ".join(parts)


# -------------------------------------------------------------------------
# Table template creation functions
# -------------------------------------------------------------------------

#
# Create single cell table template entry
#
# @param parent  Parent XML element
# @param index   Column index in the current row
# @param text    Cell text in a quoted format
# @param span    Column span
# @return Index of the next column in the current row
#
def create_cell_raw(parent, index, text, span):
    cell = ET.SubElement(parent, 'cell')
    cell.attrib['index'] = str(index)
    cell.attrib['background_mode'] = 'none'
    cell.attrib['row_span'] = '1'
    cell.attrib['column_span'] = str(span)

    content = ET.SubElement(cell, 'content')
    content.attrib['alignment'] = 'left'
    content.text = text

    return index + 1

#
# Create single cell table template entry containing an expression
#


def create_cell(parent, index, comment, text, span):
    return create_cell_raw(parent, index, quote(create_comment(comment, text)), span)

#
# Add column header to XML table definition
#
# @param parent Parent XML element
# @param index  Index of the cell in the current column
# @param text   Header text / cell content in a quoted format
#


def create_column_header(parent, index, text):
    header = ET.SubElement(parent, 'column_header')
    header.attrib['index'] = str(index)

    content = ET.SubElement(header, 'content')
    content.attrib['alignment'] = 'left'
    content.text = text

#
# Create HTML format string representing a subscript name
#
# @param name  Variable name
# @param index Variable index
#


def var_name(name, index):
    return '{0}<sub>{1}</sub>'.format(name, index) if index != None else name


def italic(text):
    return '<i>{0}</i>'.format(text)

#
# Create HTML format string representing an overlined name
#
# @param name  Variable name
# @param index Variable index
#


def overlined_var_name(name, index):
    text = '<span style="text-decoration: overline;">{0}</span>'.format(name)
    if index != None:
        text += '<sub>{0}</sub> = '.format(index)
    else:
        text += ' = '
    return text


# -------------------------------------------------------------------------
# Expression creation functions
# -------------------------------------------------------------------------

#
# Return element type classification
#
def get_element_type(element):

    if element.object_family == 'gdat':
        return cfg.Type_GDAT

    return cfg.Type_Inspection


#
# Generate result token access matching the given type
#
def get_result_token(type):
    if type == cfg.Type_Inspection:
        return 'result_dimension.deviation'
    elif type == cfg.Type_GDAT:
        return 'result_gdat_size.deviation'

    raise AssertionError('Unknown element family type')


def get_tolerance_tokens(type):
    if type == cfg.Type_GDAT:
        return ('result_gdat_size.lower_tolerance_limit', 'result_gdat_size.upper_tolerance_limit')

    return ('result_dimension.lower_tolerance_limit', 'result_dimension.upper_tolerance_limit')

#
# Generate tolerance accessing expression
#


def get_tolerance_expression(type):
    if type == cfg.Type_Inspection:
        return 'abs (result_dimension.upper_tolerance_limit - result_dimension.lower_tolerance_limit)'
    elif type == cfg.Type_GDAT:
        return 'abs (result_gdat_size.upper_tolerance_limit - result_gdat_size.lower_tolerance_limit)'

    raise AssertionError('Unknown element family type')

#
# Generate tolerance checking token
#


def get_tolerance_used_token(type):
    if type == cfg.Type_Inspection:
        return 'result_dimension.is_tolerance_used'
    elif type == cfg.Type_GDAT:
        return 'result_gdat_size.is_tolerance_used'

    raise AssertionError('Unknown element family type')

#
# Create expression for accessing the value of a single stage
#


def create_stage_access_expression(config, appraiser, part, trial, type):
    return 'avg ({0}, index=gom.app.project.stage_markers["{1}"], condition={2})'.format(get_result_token(type), cfg.all_stages_range_name, create_stage_filter(appraiser, part, trial))

#
# Create average over multiple expressions
#


def create_average_expression(params):

    return 'avg ({0})'.format(', '.join(params))

#
# Create range over multiple expressions
#


def create_range_expression(params):

    return 'max ({0}) - min ({0})'.format(', '.join(params))

#
# Create expression for computing the average value restricted to a single stage range
#


def create_restricted_avg_expression(config, appraiser, part, trial, type):
    token = get_result_token(type)

    #
    # Case 1: Stage range covering all stages. Using 'index="stages"' here instead does not work because
    #         in that case the content would be dependent of the currently activated stage range.
    #
    if appraiser == None and part == None and trial == None:
        return 'avg ({0}, index=gom.app.project.stage_markers["{1}"])'.format(token, cfg.all_stages_range_name)

    #
    # Case 2: A dedicated set of stages
    #
    else:
        return 'avg ({0}, index=gom.app.project.stage_markers["{1}"], condition={2})'.format(get_result_token(type), cfg.all_stages_range_name, create_stage_filter(appraiser, part, trial))

#
# Create expression for computing the range (max - min) value restricted to a single stage range
#


def create_restricted_range_expression(data, appraiser, part, trial, type):
    return 'max ({0}, index=gom.app.project.stage_markers["{1}"], condition={2}) - min ({0}, index=gom.app.project.stage_markers["{1}"], condition={2})' \
        .format(get_result_token(type), cfg.all_stages_range_name, create_stage_filter(appraiser, part, trial))


#
# Create expression for computing the value in percent of the tolerance
#
def create_percent_expression(type, variable, prefix_function=None):
    expression = '{0} ? 100.0 * {1} / {2} : "No tol."'.format(
        get_tolerance_used_token(type), variable, get_tolerance_expression(type))

    if prefix_function:
        expression = prefix_function + ' (' + expression + ')'

    return 'return ' + expression + '\n'
