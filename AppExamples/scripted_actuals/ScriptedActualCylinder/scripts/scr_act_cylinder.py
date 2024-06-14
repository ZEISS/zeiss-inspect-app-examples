# -*- coding: utf-8 -*-
#
# ex05_cylinder.py
#
# Example for creating a scripted cylinder element from point, direction, radius and inner (flag)
#
# Carl Zeiss GOM Metrology GmbH, 2023
#
# This test is part of the "Python API Examples" Add-on.
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_cylinder.gdlg')

    if 'point_x' in params:
        DIALOG.point_x.value = params['point_x']
    if 'point_y' in params:
        DIALOG.point_y.value = params['point_y']
    if 'point_z' in params:
        DIALOG.point_z.value = params['point_z']
    if 'dir_x' in params:
        DIALOG.dir_x.value = params['dir_x']
    if 'dir_y' in params:
        DIALOG.dir_y.value = params['dir_y']
    if 'dir_z' in params:
        DIALOG.dir_z.value = params['dir_z']
    if 'radius' in params:
        DIALOG.radius.value = params['radius']
    if 'inner' in params:
        DIALOG.radius.value = params['inner']

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
        params['point_x'] = DIALOG.point_x.value
        params['point_y'] = DIALOG.point_y.value
        params['point_z'] = DIALOG.point_z.value
        params['dir_x'] = DIALOG.dir_x.value
        params['dir_y'] = DIALOG.dir_y.value
        params['dir_z'] = DIALOG.dir_z.value
        params['radius'] = DIALOG.radius.value
        params['inner'] = DIALOG.inner.value

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
            # point = gom.Vec3d(params['point_x'], params['point_y'], params['point_z'])
            # direction = gom.Vec3d(params['dir_x'], params['dir_y'], params['dir_z'])
            context.result[stage] = {'default': {
                'point': gom.Vec3d(params['point_x'], params['point_y'], params['point_z']),
                'radius': params['radius'],
                'direction': gom.Vec3d(params['dir_x'], params['dir_y'], params['dir_z']),
                'inner': params['inner']
            }}
            context.data[stage] = {"ude_mykey": "Scripted Cylinder"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
