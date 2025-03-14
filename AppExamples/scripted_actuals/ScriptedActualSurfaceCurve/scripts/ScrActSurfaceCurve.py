# -*- coding: utf-8 -*-
#
# scr_act_surface_curve.py
#
# Example for creating a scripted surface curve element from a parametric curve function
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
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_surface_curve.gdlg')

    if 'r' in params:
        DIALOG.r.value = params['r']
    if 'theta' in params:
        DIALOG.theta.value = params['theta']
    if 'phi_min' in params:
        DIALOG.phi_min.value = params['phi_min']
    if 'phi_max' in params:
        DIALOG.phi_max.value = params['phi_max']

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
        params['r'] = DIALOG.r.value
        params['theta'] = DIALOG.theta.value
        params['phi_min'] = DIALOG.phi_min.value
        params['phi_max'] = DIALOG.phi_max.value

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
            # P(t) = ( r * cos(theta) * cos(phi), r * cos(theta) * sin (phi), r * sin(phi) )
            # with
            #   theta = const
            #   phi in [phi_min...phi_max], 1000 steps
            points = []
            normals = []
            for phi in np.arange(params['phi_min'], params['phi_max'], (params['phi_max'] - params['phi_min']) / 1000):

                p = (
                    params['r'] * math.cos(params['theta']) * math.cos(phi),
                    params['r'] * math.cos(params['theta']) * math.sin(phi),
                    params['r'] * math.sin(params['theta'])
                )
                points.append(p)
                normals.append(p)
            context.result[stage] = [{'points': points, 'normals': normals}]
            context.data[stage] = {"ude_mykey": "Scripted Surface Curve"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
