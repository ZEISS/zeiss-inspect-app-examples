# -*- coding: utf-8 -*-
#
# ScriptedCurveCheck.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---


import gom
import gom.api.scripted_checks_util
import numpy as np


def dialog(context, params):
    """Dialog function

    This function will show the creation / editing dialog
    """
    #
    # Create user defined dialog. The dialog layout is loaded from the file 'CheckCurveDialog.gdlg'.
    #
    DIALOG = gom.script.sys.create_user_defined_dialog(file='CheckCurveDialog.gdlg')

    def dialog_event_handler(event):
        if str(event) == 'system':
            return
        if event == DIALOG.slct_element or str(event) == 'initialize':
            DIALOG.elementname.element = DIALOG.slct_element.value
        if event == DIALOG.unit:
            DIALOG.tolerances.unit = DIALOG.unit.value

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    DIALOG.slct_element.filter = gom.api.scripted_checks_util.is_curve_checkable
    # -------------------------------------------------------------------------

    #
    # EDIT CREATION
    #
    if context.is_new_element and len(params) > 0:
        DIALOG.elementname.value = context.name
    if 'checked_element' in params:
        DIALOG.slct_element.value = params['checked_element']
    if 'tolerance' in params:
        DIALOG.tolerances.value = params['tolerance']
    if 'unit' in params:
        DIALOG.unit.value = params['unit']
        DIALOG.tolerances.unit = params['unit']
    if 'coordinate_system' in params:
        DIALOG.cs.value = params['coordinate_system']

    #
    # Execute dialog
    #
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)

    # Setting name of result element in GOM context
    context.name = DIALOG.elementname.value

    #
    # Setup the creation parameters from the dialog. They will be
    # stored for computation and are also available at recalculation
    # from "Edit creation parameters"
    #
    params['checked_element'] = DIALOG.slct_element.value
    params['tolerance'] = DIALOG.tolerances.value
    params['unit'] = DIALOG.unit.value
    # -------------------------------------------------------------------------
    params['coordinate_system'] = DIALOG.cs.value
    if params['coordinate_system'] is None:
        params['coordinate_system'] = gom.app.project.view_csys
    # -------------------------------------------------------------------------
    params['abbreviation'] = 'ScrCrv'
    return params


def calculation(context, params):
    """Calculation function

    This function is executed when an element should be created from a parameter
    set. The parameters can either originate from a recorded command, from a triggered
    preview computation or simply from a dialog which is ok'ed.
    """
    # Getting a handle to the element chosen in the dialog
    element = params['checked_element']

    # -------------------------------------------------------------------------
    # Get coordinate transformation for local coordinate system
    trafo_matrices = None
    if params["coordinate_system"] is not None:
        trafo_matrices = np.array(gom.api.scripted_checks_util.get_cs_transformation_4x4(
            params["coordinate_system"]
        ))
    # -------------------------------------------------------------------------

    # Iterating over all stages
    for s in context.stages:
        # The vertices of the selected mesh
        stage_vertices = np.array(element.data.coordinate[s])

        # -------------------------------------------------------------------------
        # Apply coordinate transformation to all vertices if necessary
        if trafo_matrices is not None:
            stage_trafo = trafo_matrices[s]
            stage_vertices = (np.dot(stage_trafo[0:3, 0:3], stage_vertices.T) + stage_trafo[:3, 3:]).T
        # -------------------------------------------------------------------------

        # The result of this stage to be filled
        actual_result = np.zeros(stage_vertices.shape[0])
        nominal_result = np.random.rand(stage_vertices.shape[0])

        for i in range(stage_vertices.shape[0]):
            point = gom.Vec3d(stage_vertices[i][0], stage_vertices[i][1], stage_vertices[i][2])

            # ----------------------------------------------------
            # --- insert your calculation for each vertex here ---
            # ----------------------------------------------------
            actual_result[i] = point.y
            # ----------------------------------------------------

        result = {"actual_values": actual_result, "reference": element, 'nominal_values': nominal_result}
        context.result[s] = result

    return True
