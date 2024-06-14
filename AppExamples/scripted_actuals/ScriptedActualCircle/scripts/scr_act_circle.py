# -*- coding: utf-8 -*-
#
# scr_act_circle.py
#
# Example for creating a scripted circle element from center, direction and radius
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_circle.gdlg')

    if 'center_x' in params:
        DIALOG.center_x.value = params['center_x']
    if 'center_y' in params:
        DIALOG.center_y.value = params['center_y']
    if 'center_z' in params:
        DIALOG.center_z.value = params['center_z']
    if 'dir_x' in params:
        DIALOG.dir_x.value = params['dir_x']
    if 'dir_y' in params:
        DIALOG.dir_y.value = params['dir_y']
    if 'dir_z' in params:
        DIALOG.dir_z.value = params['dir_z']
    if 'radius' in params:
        DIALOG.radius.value = params['radius']

    # Get previous element name, when started from "Edit creation"
    if len(params) > 0:
        DIALOG.name.value = context.name

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        # No treatment of system events
        if str(widget) == 'system':
            return
        # If preview calculation returned with error
        if str(widget) == 'error':
            DIALOG.control.status = context.error
            return
        # If preview calculation was successful
        if str(widget) == 'calculated':
            DIALOG.control.status = ''
            DIALOG.control.ok.enabled = True
            return

        # All other changes in the dialog --> calculate preview
        params['center_x'] = DIALOG.center_x.value
        params['center_y'] = DIALOG.center_y.value
        params['center_z'] = DIALOG.center_z.value
        params['dir_x'] = DIALOG.dir_x.value
        params['dir_y'] = DIALOG.dir_y.value
        params['dir_z'] = DIALOG.dir_z.value
        params['radius'] = DIALOG.radius.value

        context.name = DIALOG.name.value
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params

# -------------------------------------------------------------------------


def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'center': (params['center_x'], params['center_y'], params['center_z']),
                'direction': (params['dir_x'], params['dir_y'], params['dir_z']),
                'radius': params['radius']
            }
            context.data[stage] = {"ude_mykey": "Scripted Circle"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
