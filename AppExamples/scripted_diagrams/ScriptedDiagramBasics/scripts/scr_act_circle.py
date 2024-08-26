# -*- coding: utf-8 -*-
#
# scr_act_circle.py
#
# Example for creating a scripted circle element from center, direction and radius.
# Select the Scripted Diagram's Service in the element creation dialog.
# The radius is passed to the Scripted Diagram's Service.
#
# Carl Zeiss GOM Metrology GmbH, 2023
#
# This test is part of the "Python API Examples" Add-on.
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2023/python_examples/
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
    if 'service' in params:
        DIALOG.service_list.value = params['service']

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
        params['service'] = DIALOG.service_list.value

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
            context.data[stage] = {
                "ude_diagram_custom": 1,
                "ude_diagram_type": "SVGDiagram",
                # "gom.api.diagram.radius_plot" or "gom.api.statistics.radius_histogram"
                "ude_diagram_service" : params['service'],
                "ude_diagram_radius": params['radius'],
                "ude_diagram_center": gom.Vec3d(params['center_x'], params['center_y'], params['center_z'])
            }
            print(f'{context.data[stage]}')
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
