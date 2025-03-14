# -*- coding: utf-8 -*-
#
# scr_act_curve.py
#
# Example for creating a scripted curve element from a parametric curve function
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import math
import numpy as np


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_curve.gdlg')

    if 'x0' in params:
        DIALOG.x0.value = params['x0']
    if 'y0' in params:
        DIALOG.y0.value = params['y0']
    if 'z0' in params:
        DIALOG.z0.value = params['z0']
    if 'radius' in params:
        DIALOG.radius.value = params['radius']
    if 'j' in params:
        DIALOG.j.value = params['j']
    if 'k' in params:
        DIALOG.k.value = params['k']
    if 't_min' in params:
        DIALOG.t_min.value = params['t_min']
    if 't_max' in params:
        DIALOG.t_max.value = params['t_max']

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
        params['x0'] = DIALOG.x0.value
        params['y0'] = DIALOG.y0.value
        params['z0'] = DIALOG.z0.value
        params['radius'] = DIALOG.radius.value
        params['j'] = DIALOG.j.value
        params['k'] = DIALOG.k.value
        params['t_min'] = DIALOG.t_min.value
        params['t_max'] = DIALOG.t_max.value

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
            # Creating a list of points using a parametric curve function:
            # P(t) = ( x0 + (j * t + r) * cos(t), y0 + (j * t + r) * cos(t), z0 + k * t )
            # with t in [t_min...t_max], 1000 steps
            points = []
            for t in np.arange(params['t_min'], params['t_max'], (params['t_max'] - params['t_min']) / 1000):
                points.append((params['x0'] + (params['j'] * t + params['radius']) * math.cos(t),
                               params['y0'] + (params['j'] * t + params['radius']) * math.sin(t),
                               params['z0'] + params['k'] * t)
                              )
            context.result[stage] = [{'points': points}]
            context.data[stage] = {"ude_mykey": "Example 3"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
