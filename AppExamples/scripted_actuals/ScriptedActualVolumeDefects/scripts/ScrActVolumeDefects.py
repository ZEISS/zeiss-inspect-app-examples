# -*- coding: utf-8 -*-
#
# scr_act_volume_defect.py
#
# Example for creating a scripted volume element from a tetrahedron defined by four vertices.
# The vertices are provided as parameters, the triangles connecting the vertices are fixed.
#
# NOTE: This example requires ZEISS INSPECT X-Ray
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_volume_defects.gdlg')

    if 'v0_x' in params:
        DIALOG.v0_x.value = params['v0_x']
    if 'v0_y' in params:
        DIALOG.v0_y.value = params['v0_y']
    if 'v0_z' in params:
        DIALOG.v0_z.value = params['v0_z']

    if 'v1_x' in params:
        DIALOG.v1_x.value = params['v1_x']
    if 'v1_y' in params:
        DIALOG.v1_y.value = params['v1_y']
    if 'v1_z' in params:
        DIALOG.v1_z.value = params['v1_z']

    if 'v2_x' in params:
        DIALOG.v2_x.value = params['v2_x']
    if 'v2_y' in params:
        DIALOG.v2_y.value = params['v2_y']
    if 'v2_z' in params:
        DIALOG.v2_z.value = params['v2_z']

    if 'v3_x' in params:
        DIALOG.v3_x.value = params['v3_x']
    if 'v3_y' in params:
        DIALOG.v3_y.value = params['v3_y']
    if 'v3_z' in params:
        DIALOG.v3_z.value = params['v3_z']

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
        params['v0_x'] = DIALOG.v0_x.value
        params['v0_y'] = DIALOG.v0_y.value
        params['v0_z'] = DIALOG.v0_z.value
        params['v1_x'] = DIALOG.v1_x.value
        params['v1_y'] = DIALOG.v1_y.value
        params['v1_z'] = DIALOG.v1_z.value
        params['v2_x'] = DIALOG.v2_x.value
        params['v2_y'] = DIALOG.v2_y.value
        params['v2_z'] = DIALOG.v2_z.value
        params['v3_x'] = DIALOG.v3_x.value
        params['v3_y'] = DIALOG.v3_y.value
        params['v3_z'] = DIALOG.v3_z.value

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
    v0 = (params['v0_x'], params['v0_y'], params['v0_z'])
    v1 = (params['v1_x'], params['v1_y'], params['v1_z'])
    v2 = (params['v2_x'], params['v2_y'], params['v2_z'])
    v3 = (params['v3_x'], params['v3_y'], params['v3_z'])

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'vertices': [np.array([v0, v1, v2, v3])],
                # Note:
                # Triangles are defined by indices into the array of vertices.
                # The vertices defining a triangle must be specified in counter-clockwise
                # order, otherwise the resulting surface would be inverted, i.e. invisible!
                'triangles': [np.array([(0, 1, 2), (1, 0, 3), (0, 2, 3), (2, 1, 3)])]
            }
            context.data[stage] = {"ude_mykey": "Scripted Volume Defects"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
