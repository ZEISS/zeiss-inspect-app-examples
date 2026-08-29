# -*- coding: utf-8 -*-
#
# msa_lib - Common library functions for generating MSA / Gauge R&R setups
#
# Carl Zeiss GOM Metrology GmbH, 2025
#

import gom
import os
import os.path
import re
import xml.etree
import xml.etree.ElementTree as ET
import xml.dom.minidom
import stringprep

import msa_config as cfg

# ----------------------------------------------------------------------------------
# Local functions
# ----------------------------------------------------------------------------------

#
# Make container content unique and sort it (if possible)
#


def make_unique_and_sort(container):
    def convert(x): return int(x) if x.isdigit() else x.lower()
    return sorted(list(set(container)), key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)])


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
# CLASS Configuration
# ----------------------------------------------------------------------------------

#
# Class keeping / editing the configuration
#
class Configuration:

    def __init__(self, type):

        self.type = type

        self.types = [cfg.Type_Inspection, cfg.Type_GDAT]

        self.appraisers = set()
        self.parts = set()
        self.trials = set()
        self.stages = {}

        self.appraiser_element = Configuration.get_actual_value_element(cfg.appraiser_tag)
        self.trial_element = Configuration.get_actual_value_element(cfg.trial_tag)
        self.part_element = Configuration.get_actual_value_element(cfg.part_tag)
        self.sigma_element = Configuration.get_nominal_value_element(cfg.sigma_tag)

        self.collect_data()

    @staticmethod
    def get_actual_value_element(name):

        element = None

        try:
            element = gom.app.project.actual_elements[name]
        except:
            element = gom.script.inspection.create_value_element(name=name, type='string', stage_values={})
            gom.script.cad.hide_element(elements=[element])

        return element

    @staticmethod
    def get_nominal_value_element(name):

        element = None

        try:
            element = gom.app.project.inspection[name]
        except:
            element = gom.script.inspection.create_constant_value_element(
                description=name,
                name=name,
                type='float',
                unit='UNIT_NONE',
                value=0.0)
            gom.script.inspection.measure_by_no_measuring_principle(elements=[element])
            gom.script.cad.hide_element(elements=[element])

        return element

    #
    # Build appraisers/parts/trials sets
    #

    def collect_data(self):

        def sanitize(string):
            if string and len(string) > 0:
                return string
            return None

        self.appraisers = set()
        self.parts = set()
        self.trials = set()

        for stage in gom.app.project.stages:

            if stage.is_active:
                stage_item = 'gom.app.project.stages[\'{name}\']'.format(name=stage.name)

                appraiser = sanitize(self.appraiser_element.get(
                    'with_context (stage={stage}, value)'.format(stage=stage_item)))
                if appraiser:
                    self.appraisers.add(appraiser)

                part = sanitize(self.part_element.get('with_context (stage={stage}, value)'.format(stage=stage_item)))
                if part:
                    self.parts.add(part)

                trial = sanitize(self.trial_element.get('with_context (stage={stage}, value)'.format(stage=stage_item)))
                if trial:
                    self.trials.add(trial)

                self.stages[stage.name] = (appraiser, part, trial)

        self.appraisers = make_unique_and_sort(self.appraisers)
        self.parts = make_unique_and_sort(self.parts)
        self.trials = make_unique_and_sort(self.trials)

    #
    # Edit configuration via dialog
    #

    def edit(self, show_sigma_input):
        MAIN_DIALOG = gom.script.sys.create_user_defined_dialog(content='<dialog>'
                                                                ' <title>Generate ' + self.type.value + ' table templates</title>'
                                                                ' <style></style>'
                                                                ' <control id="OkCancel"/>'
                                                                ' <position></position>'
                                                                ' <embedding></embedding>'
                                                                ' <sizemode></sizemode>'
                                                                ' <size width="628" height="397"/>'
                                                                ' <content rows="7" columns="3">'
                                                                '  <widget type="display::text" columnspan="3" column="0" row="0" rowspan="1">'
                                                                '   <name>text</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'
                                                                '&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">'
                                                                'p, li { white-space: pre-wrap; }'
                                                                '&lt;/style>&lt;/head>&lt;body style="    ">'
                                                                '&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:12pt; font-weight:600;">Generate MSA (' +
                                                                self.type.value + ' table templates)&lt;/span>&lt;/p>'
                                                                '&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>'
                                                                '&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> This script generates a ' +
                                                                self.type.value + ' table template displaying the MSA variant.&lt;/li>'
                                                                '&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> The generated templates are matching the number of appraisers, parts and trials found in the project.&lt;/li>'
                                                                '&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> The script has to be executed again if stages are added or removed.&lt;/li>&lt;/ul>'
                                                                '&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>&lt;/body>&lt;/html></text>'
                                                                '   <wordwrap>false</wordwrap>'
                                                                '  </widget>'
                                                                '  <widget type="label" columnspan="1" column="0" row="1" rowspan="1">'
                                                                '   <name>appraisers_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Appraisers</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget type="input::string" columnspan="2" column="1" row="1" rowspan="1">'
                                                                '   <name>appraisers</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>true</read_only>'
                                                                '  </widget>'
                                                                '  <widget type="label" columnspan="1" column="0" row="2" rowspan="1">'
                                                                '   <name>parts_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Parts</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget type="input::string" columnspan="2" column="1" row="2" rowspan="1">'
                                                                '   <name>parts</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>true</read_only>'
                                                                '  </widget>'
                                                                '  <widget type="label" columnspan="1" column="0" row="3" rowspan="1">'
                                                                '   <name>trials_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Trials</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget type="input::string" columnspan="2" column="1" row="3" rowspan="1">'
                                                                '   <name>trials</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>true</read_only>'
                                                                '  </widget>'
                                                                '  <widget type="label" columnspan="1" column="0" row="4" rowspan="1">'
                                                                '   <name>sigma_value_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Sigma value</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget type="input::number" columnspan="2" column="1" row="4" rowspan="1">'
                                                                '   <name>sigma_value</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value>5.15</value>'
                                                                '   <minimum>0</minimum>'
                                                                '   <maximum>1000</maximum>'
                                                                '   <precision>2</precision>'
                                                                '   <background_style></background_style>'
                                                                '  </widget>'
                                                                '  <widget type="spacer::horizontal" columnspan="1" column="0" row="5" rowspan="1">'
                                                                '   <name>spacer</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <minimum_size>0</minimum_size>'
                                                                '   <maximum_size>10</maximum_size>'
                                                                '  </widget>'
                                                                '  <widget type="spacer::horizontal" columnspan="1" column="1" row="5" rowspan="1">'
                                                                '   <name>spacer_1</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <minimum_size>0</minimum_size>'
                                                                '   <maximum_size>-1</maximum_size>'
                                                                '  </widget>'
                                                                '  <widget type="button::pushbutton" columnspan="1" column="2" row="5" rowspan="1">'
                                                                '   <name>edit_stages</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Edit stages</text>'
                                                                '   <type>push</type>'
                                                                '   <icon_type>none</icon_type>'
                                                                '   <icon_size>icon</icon_size>'
                                                                '   <icon_system_type>ok</icon_system_type>'
                                                                '   <icon_system_size>default</icon_system_size>'
                                                                '  </widget>'
                                                                '  <widget type="separator" columnspan="3" column="0" row="6" rowspan="1">'
                                                                '   <name>separator</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <title></title>'
                                                                '  </widget>'
                                                                ' </content>'
                                                                '</dialog>')

        has_appraisers = self.type != cfg.EvaluationType.Anova_3

        if not has_appraisers:
            MAIN_DIALOG.appraisers.visible = False
            MAIN_DIALOG.appraisers_label.visible = False

        MAIN_DIALOG.appraisers.value = ', '.join(self.appraisers)
        MAIN_DIALOG.parts.value = ', '.join(self.parts)
        MAIN_DIALOG.trials.value = ', '.join(self.trials)
        MAIN_DIALOG.sigma_value.value = cfg.default_sigma_factor

        MAIN_DIALOG.sigma_value.visible = show_sigma_input
        MAIN_DIALOG.sigma_value_label.visible = show_sigma_input
        MAIN_DIALOG.sigma_value.focus = show_sigma_input

        def adapt_main_dialog_status():

            number_of_stages = 0
            for stage in gom.app.project.stages:
                if stage.is_active:
                    number_of_stages += 1

            if len(self.parts) == 0 or len(self.trials) == 0:
                MAIN_DIALOG.control.status = 'Stages must be tagged appropriately.'
                MAIN_DIALOG.control.ok.enabled = False

            elif has_appraisers and len(self.appraisers) * len(self.parts) * len(self.trials) != number_of_stages:
                MAIN_DIALOG.control.status = 'Number of appraisers ({0}), parts ({1}) and trials ({2}) does not match number of stages ({3}).' \
                    .format(len(self.appraisers), len(self.parts), len(self.trials), number_of_stages)
                MAIN_DIALOG.control.ok.enabled = False

            elif not has_appraisers and len(self.parts) * len(self.trials) != number_of_stages:
                MAIN_DIALOG.control.status = 'Number of parts ({0}) and trials ({1}) does not match number of stages ({2}).' \
                    .format(len(self.parts), len(self.trials), number_of_stages)
                MAIN_DIALOG.control.ok.enabled = False

            elif has_appraisers and len(self.appraisers) > 0 and number_of_stages % len(self.appraisers) != 0:
                MAIN_DIALOG.control.status = 'Number of stages ({0}) / number of appraisers ({1}) does have a remainder.' \
                    .format(len(gom.app.project.stages), len(self.appraisers))

            elif len(self.parts) > 0 and number_of_stages % len(self.parts) != 0:
                MAIN_DIALOG.control.status = 'Number of stages ({0}) / number of parts ({1}) does have a remainder.' \
                    .format(len(gom.app.project.stages), len(self.parts))

            elif len(self.trials) > 0 and number_of_stages % len(self.trials) != 0:
                MAIN_DIALOG.control.status = 'Number of stages ({0}) / number of trials ({1}) does have a remainder.' \
                    .format(len(gom.app.project.stages), len(self.trials))

            else:
                MAIN_DIALOG.control.status = ''

            MAIN_DIALOG.control.ok.enabled = MAIN_DIALOG.control.status == ''

        def main_dialog_handler(widget):

            if widget == MAIN_DIALOG.edit_stages:
                self.edit_stages()
                self.collect_data()
                adapt_main_dialog_status()

            MAIN_DIALOG.appraisers.value = ', '.join(self.appraisers)
            MAIN_DIALOG.parts.value = ', '.join(self.parts)
            MAIN_DIALOG.trials.value = ', '.join(self.trials)

        MAIN_DIALOG.handler = main_dialog_handler
        adapt_main_dialog_status()

        gom.script.sys.show_user_defined_dialog(dialog=MAIN_DIALOG)

        gom.script.sys.edit_creation_parameters(
            auto_apply=True,
            element=self.sigma_element,
            value=MAIN_DIALOG.sigma_value.value)

    def filter_map(self, n):
        for key, tuple in self.stages.items():
            yield key, tuple[n]

    def write_back_values(self):

        gom.script.sys.edit_creation_parameters(
            element=self.appraiser_element,
            type='string',
            stage_values=dict(self.filter_map(0)),
            auto_apply=True
        )

        gom.script.sys.edit_creation_parameters(
            element=self.part_element,
            type='string',
            stage_values=dict(self.filter_map(1)),
            auto_apply=True
        )

        gom.script.sys.edit_creation_parameters(
            element=self.trial_element,
            type='string',
            stage_values=dict(self.filter_map(2)),
            auto_apply=True
        )

        #
        # For some strange reason we need a recalc here
        #
        gom.script.sys.recalculate_visible_elements_in_all_stages(enable=True)
        gom.script.sys.recalculate_project(with_reports=False)

    #
    # Assign appraiser/part/trial tags from the stage name pattern
    #

    def assign_from_stage_name_pattern(self, pattern):

        split_pattern = '[._\-/]+'
        template_parts = re.split(split_pattern, pattern)
        error = None

        if len(template_parts) == 3:
            current_stage = gom.app.project.stages[gom.app.project.stage]

            appraiser_index = template_parts.index('appraiser')
            part_index = template_parts.index('part')
            trial_index = template_parts.index('trial')

            if appraiser_index >= 0 and part_index >= 0 and trial_index >= 0:

                for stage in gom.app.project.stages:
                    if stage.is_active:
                        gom.script.sys.show_stage(stage=stage)

                        stage_name = gom.app.project.stage

                        parts = re.split(split_pattern, stage_name)
                        if len(parts) != 3:
                            error = 'Name of stage {0} does not match pattern'.format(stage_name)
                            break

                        self.stages[stage_name] = (
                            parts[appraiser_index].strip(),
                            parts[part_index].strip(),
                            parts[trial_index].strip()
                        )

                if current_stage != None:
                    gom.script.sys.show_stage(stage=current_stage)
            else:
                error = 'Wrong pattern format {0}'.format(pattern)
        else:
            error = 'Error parsing the pattern definition'

        if not error:
            self.write_back_values()

    #
    # Open dialog for letting the user check/edit the appraiser/part/trial keywords of each stage
    #

    def edit_stages(self):

        EDIT_DIALOG = gom.script.sys.create_user_defined_dialog(content='<dialog>'
                                                                ' <title>Edit stages</title>'
                                                                ' <style></style>'
                                                                ' <control id="Close"/>'
                                                                ' <position></position>'
                                                                ' <embedding></embedding>'
                                                                ' <sizemode>automatic</sizemode>'
                                                                ' <size height="305" width="346"/>'
                                                                ' <content rows="8" columns="4">'
                                                                '  <widget row="0" columnspan="1" rowspan="1" type="label" column="0">'
                                                                '   <name>stage_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Stage</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget row="0" columnspan="3" rowspan="1" type="input::string" column="1">'
                                                                '   <name>stage</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>true</read_only>'
                                                                '  </widget>'
                                                                '  <widget row="1" columnspan="4" rowspan="1" type="separator" column="0">'
                                                                '   <name>separator_1</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <title></title>'
                                                                '  </widget>'
                                                                '  <widget row="2" columnspan="1" rowspan="1" type="label" column="0">'
                                                                '   <name>appraiser_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Appraiser</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget row="2" columnspan="3" rowspan="1" type="input::string" column="1">'
                                                                '   <name>appraiser</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>false</read_only>'
                                                                '  </widget>'
                                                                '  <widget row="3" columnspan="1" rowspan="1" type="label" column="0">'
                                                                '   <name>part_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Part</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget row="3" columnspan="3" rowspan="1" type="input::string" column="1">'
                                                                '   <name>part</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>false</read_only>'
                                                                '  </widget>'
                                                                '  <widget row="4" columnspan="1" rowspan="1" type="label" column="0">'
                                                                '   <name>trial_label</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>Trial</text>'
                                                                '   <word_wrap>false</word_wrap>'
                                                                '  </widget>'
                                                                '  <widget row="4" columnspan="3" rowspan="1" type="input::string" column="1">'
                                                                '   <name>trial</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <value></value>'
                                                                '   <read_only>false</read_only>'
                                                                '  </widget>'
                                                                '  <widget row="5" columnspan="1" rowspan="1" type="spacer::horizontal" column="0">'
                                                                '   <name>spacer</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <minimum_size>0</minimum_size>'
                                                                '   <maximum_size>10</maximum_size>'
                                                                '  </widget>'
                                                                '  <widget row="5" columnspan="1" rowspan="1" type="spacer::horizontal" column="1">'
                                                                '   <name>spacer_1</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <minimum_size>150</minimum_size>'
                                                                '   <maximum_size>-1</maximum_size>'
                                                                '  </widget>'
                                                                '  <widget row="5" columnspan="1" rowspan="1" type="button::pushbutton" column="2">'
                                                                '   <name>prev_stage</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>&lt;</text>'
                                                                '   <type>push</type>'
                                                                '   <icon_type>none</icon_type>'
                                                                '   <icon_size>icon</icon_size>'
                                                                '   <icon_system_type>ok</icon_system_type>'
                                                                '   <icon_system_size>default</icon_system_size>'
                                                                '  </widget>'
                                                                '  <widget row="5" columnspan="1" rowspan="1" type="button::pushbutton" column="3">'
                                                                '   <name>next_stage</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <text>></text>'
                                                                '   <type>push</type>'
                                                                '   <icon_type>none</icon_type>'
                                                                '   <icon_size>icon</icon_size>'
                                                                '   <icon_system_type>ok</icon_system_type>'
                                                                '   <icon_system_size>default</icon_system_size>'
                                                                '  </widget>'
                                                                '  <widget row="6" columnspan="4" rowspan="1" type="spacer::vertical" column="0">'
                                                                '   <name>spacer_2</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <minimum_size>0</minimum_size>'
                                                                '   <maximum_size>-1</maximum_size>'
                                                                '  </widget>'
                                                                '  <widget row="7" columnspan="4" rowspan="1" type="separator" column="0">'
                                                                '   <name>separator_2</name>'
                                                                '   <tooltip></tooltip>'
                                                                '   <title></title>'
                                                                '  </widget>'
                                                                ' </content>'
                                                                '</dialog>')

        has_appraisers = self.type != cfg.EvaluationType.Anova_3

        if not has_appraisers:
            EDIT_DIALOG.appraiser.visible = False
            EDIT_DIALOG.appraiser_label.visible = False

        def update_edit_stages_dialog():
            stage_name = gom.app.project.get('stage.name')

            EDIT_DIALOG.stage.value = stage_name
            (appraiser, part, trial) = self.stages[stage_name]

            EDIT_DIALOG.appraiser = appraiser if appraiser != None else ''
            EDIT_DIALOG.part = part if part != None else ''
            EDIT_DIALOG.trial = trial if trial != None else ''

        def apply_changes():
            self.stages[EDIT_DIALOG.stage.value] = (
                EDIT_DIALOG.appraiser.value.strip(),
                EDIT_DIALOG.part.value.strip(),
                EDIT_DIALOG.trial.value.strip()
            )

        def handler(widget):

            if widget == EDIT_DIALOG.next_stage:
                apply_changes()
                gom.script.sys.show_next_stage()
                update_edit_stages_dialog()

                if has_appraisers:
                    EDIT_DIALOG.appraiser.focus = True
                else:
                    EDIT_DIALOG.part.focus = True

            elif widget == EDIT_DIALOG.prev_stage:
                apply_changes()
                gom.script.sys.show_previous_stage()
                update_edit_stages_dialog()

            elif widget == EDIT_DIALOG.appraiser or widget == EDIT_DIALOG.part or widget == EDIT_DIALOG.trial:
                apply_changes()

            elif widget == 'system':
                update_edit_stages_dialog()

            EDIT_DIALOG.next_stage.enabled = gom.app.project.get("stage.name") != gom.app.project.stages[-1].name
            EDIT_DIALOG.prev_stage.enabled = gom.app.project.get("stage.name") != gom.app.project.stages[0].name

        update_edit_stages_dialog()
        EDIT_DIALOG.handler = handler

        gom.script.sys.show_user_defined_dialog(dialog=EDIT_DIALOG)
        apply_changes()
        self.write_back_values()


# --------------------------------------------------------------------------------------------------
# CLASS CheckboxConfiguration
#
# Display checkbox grid dialog for assigning appraiser/part/trial configuration to stages
#
class CheckboxConfiguration (Configuration):

    def __init__(self, type):

        Configuration.__init__(self, type)

        header_code = '''
        <dialog>
        <title>Configure stages</title>
        <style></style>
        <control id="OkCancel"/>
        <position></position>
        <embedding></embedding> 
        <sizemode></sizemode> 
        <content columns="{columns}" rows="{rows}"> 
        '''

        label_code = '''
            <widget rowspan="1" type="label" row="{row}" columnspan="{span}" column="{column}"> 
                <name>label_{row}_{column}</name> 
                <tooltip></tooltip> 
                <text>{text}</text> 
                <word_wrap>false</word_wrap> 
            </widget> 
        '''

        checkbox_code = '''
            <widget rowspan="1" type="input::checkbox" row="{row}" columnspan="1" column="{column}"> 
                <name>checkbox_{row}_{column}</name> 
                <tooltip></tooltip> 
                <value>{checked}</value> 
                <title></title> 
            </widget> 
        '''

        self.content = header_code.format(rows=2 + len(self.stages.keys()), columns=1 +
                                          len(self.appraisers) + len(self.parts) + len(self.trials))

        row_count = 0
        column_count = 0

        #
        # Row 0
        #
        self.content += label_code.format(row=row_count, column=column_count, text='', span=1)
        column_count += 1

        self.content += label_code.format(row=row_count, column=column_count,
                                          text='Appraisers', span=len(self.appraisers))
        column_count += len(self.appraisers)

        self.content += label_code.format(row=row_count, column=column_count, text='Parts', span=len(self.parts))
        column_count += len(self.parts)

        self.content += label_code.format(row=row_count, column=column_count, text='Trials', span=len(self.trials))
        column_count += len(self.trials)

        row_count += 1
        column_count = 0

        #
        # Row 1
        #
        self.content += label_code.format(row=row_count, column=column_count, text='', span=1)
        column_count += 1

        for appraiser in self.appraisers:
            self.content += label_code.format(row=row_count, column=column_count, text=appraiser, span=1)
            column_count += 1

        for part in self.parts:
            self.content += label_code.format(row=row_count, column=column_count, text=part, span=1)
            column_count += 1

        for trial in self.trials:
            self.content += label_code.format(row=row_count, column=column_count, text=trial, span=1)
            column_count += 1

        row_count += 1
        column_count = 0

        #
        # Row 2...n
        #
        for stage in gom.app.project.stages:
            key = stage.name
            self.content += label_code.format(row=row_count, column=column_count, text=key, span=1)
            column_count += 1

            for appraiser in self.appraisers:
                checked = 'true' if appraiser == self.stages[key][0] else 'false'
                self.content += checkbox_code.format(row=row_count, column=column_count, checked=checked)
                column_count += 1

            for part in self.parts:
                checked = 'true' if part == self.stages[key][1] else 'false'
                self.content += checkbox_code.format(row=row_count, column=column_count, checked=checked)
                column_count += 1

            for trial in self.trials:
                checked = 'true' if trial == self.stages[key][2] else 'false'
                self.content += checkbox_code.format(row=row_count, column=column_count, checked=checked)
                column_count += 1

            row_count += 1
            column_count = 0

        self.content += '</content></dialog>'

    def edit(self):

        DIALOG = gom.script.sys.create_user_defined_dialog(content=self.content)
        RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)


# --------------------------------------------------------------------------------------------------
# MAIN
#
if __name__ == '__main__':
    config = CheckboxConfiguration(cfg.EvaluationType.Anova_2)
    config.edit()
