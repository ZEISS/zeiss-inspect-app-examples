# -*- coding: utf-8 -*-
#
# scr_act_surface.py
#
# Example for creating a scripted surface element from 8 corner coordinates of a cuboid
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_surface.gdlg')

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

    if 'v4_x' in params:
        DIALOG.v4_x.value = params['v4_x']
    if 'v4_y' in params:
        DIALOG.v4_y.value = params['v4_y']
    if 'v4_z' in params:
        DIALOG.v4_z.value = params['v4_z']

    if 'v5_x' in params:
        DIALOG.v5_x.value = params['v5_x']
    if 'v5_y' in params:
        DIALOG.v5_y.value = params['v5_y']
    if 'v5_z' in params:
        DIALOG.v5_z.value = params['v5_z']

    if 'v6_x' in params:
        DIALOG.v6_x.value = params['v6_x']
    if 'v6_y' in params:
        DIALOG.v6_y.value = params['v6_y']
    if 'v6_z' in params:
        DIALOG.v6_z.value = params['v6_z']

    if 'v7_x' in params:
        DIALOG.v7_x.value = params['v7_x']
    if 'v7_y' in params:
        DIALOG.v7_y.value = params['v7_y']
    if 'v7_z' in params:
        DIALOG.v7_z.value = params['v7_z']

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
        params['v4_x'] = DIALOG.v4_x.value
        params['v4_y'] = DIALOG.v4_y.value
        params['v4_z'] = DIALOG.v4_z.value
        params['v5_x'] = DIALOG.v5_x.value
        params['v5_y'] = DIALOG.v5_y.value
        params['v5_z'] = DIALOG.v5_z.value
        params['v6_x'] = DIALOG.v6_x.value
        params['v6_y'] = DIALOG.v6_y.value
        params['v6_z'] = DIALOG.v6_z.value
        params['v7_x'] = DIALOG.v7_x.value
        params['v7_y'] = DIALOG.v7_y.value
        params['v7_z'] = DIALOG.v7_z.value

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
    v0 = gom.Vec3d(params['v0_x'], params['v0_y'], params['v0_z'])
    v1 = gom.Vec3d(params['v1_x'], params['v1_y'], params['v1_z'])
    v2 = gom.Vec3d(params['v2_x'], params['v2_y'], params['v2_z'])
    v3 = gom.Vec3d(params['v3_x'], params['v3_y'], params['v3_z'])
    v4 = gom.Vec3d(params['v4_x'], params['v4_y'], params['v4_z'])
    v5 = gom.Vec3d(params['v5_x'], params['v5_y'], params['v5_z'])
    v6 = gom.Vec3d(params['v6_x'], params['v6_y'], params['v6_z'])
    v7 = gom.Vec3d(params['v7_x'], params['v7_y'], params['v7_z'])

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'vertices': [v0, v1, v2, v3, v4, v5, v6, v7],
                # two triangles per side of the cuboid
                # ----- front ------ , ----- right ------- , ----- top ----------
                'triangles': [(0, 1, 2), (0, 2, 3), (1, 5, 6), (1, 6, 2), (3, 2, 6), (3, 6, 7),
                              # ----- bottom ----- , ----- back -------- , ----- left ---------
                              (0, 1, 5), (0, 5, 4), (4, 5, 6), (4, 6, 7), (0, 4, 7), (0, 7, 3)]
            }
            context.data[stage] = {"ude_mykey": "Scripted Surface"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
