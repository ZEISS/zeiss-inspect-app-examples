# -*- coding: utf-8 -*-
#
# ScrActDistance.py
#
# Example for creating a scripted distance element from two points
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_distance.gdlg')

    if 'p1_x' in params:
        DIALOG.p1_x.value = params['p1_x']
    if 'p1_y' in params:
        DIALOG.p1_y.value = params['p1_y']
    if 'p1_z' in params:
        DIALOG.p1_z.value = params['p1_z']
    if 'p2_x' in params:
        DIALOG.p2_x.value = params['p2_x']
    if 'p2_y' in params:
        DIALOG.p2_y.value = params['p2_y']
    if 'p2_z' in params:
        DIALOG.p2_z.value = params['p2_z']

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
        if str(widget) == 'initialize':
            gom.script.view.show_view_frustum_draft(enable=True)
            gom.script.view.auto_zoom(enable=True)

        # All other changes in the dialog --> calculate preview
        params['p1_x'] = DIALOG.p1_x.value
        params['p1_y'] = DIALOG.p1_y.value
        params['p1_z'] = DIALOG.p1_z.value
        params['p2_x'] = DIALOG.p2_x.value
        params['p2_y'] = DIALOG.p2_y.value
        params['p2_z'] = DIALOG.p2_z.value

        context.name = DIALOG.name.value
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params

# -------------------------------------------------------------------------


def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'point1': (params['p1_x'], params['p1_y'], params['p1_z']),
                'point2': (params['p2_x'], params['p2_y'], params['p2_z'])
            }
            context.data[stage] = {"ude_mykey": "Scripted Distance"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
