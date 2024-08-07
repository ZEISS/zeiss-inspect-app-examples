# -*- coding: utf-8 -*-
#
# scripted_scalar_check.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import gom.api.scripted_checks_util

#
# Dialog function
#
# This function will show the creation / editing dialog
#


def dialog(context, params):
    #
    # Create user defined dialog. The dialog layout is loaded from file.
    #
    DIALOG = gom.script.sys.create_user_defined_dialog(file='check_scalar_dialog.gdlg')

    def dialog_event_handler(event):
        if str(event) == 'system':
            return
        if event == DIALOG.slct_element or str(event) == 'initialize':
            DIALOG.elementname.element = DIALOG.slct_element.value
        if event == DIALOG.unit:
            DIALOG.tolerances.unit = DIALOG.unit.value

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    DIALOG.slct_element.filter = gom.api.scripted_checks_util.is_scalar_checkable
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
    # -------------------------------------------------------------------------
    params['tolerance'] = DIALOG.tolerances.value
    params['unit'] = DIALOG.unit.value
    params['abbreviation'] = 'ScrSca'
    # -------------------------------------------------------------------------
    return params

#
# Calculation function
#
# This function is executed when an element should be created from a parameter
# set. The parameters can either originate from a recorded command, from a triggered
# preview computation or simply from a dialog which is ok'ed.
#


def calculation(context, params):

    # Getting a handle to the element chosen in the dialog
    element = params['checked_element']

    # Iterating over all stages
    for s in context.stages:

        # ----------------------------------------------------
        # --- insert your calculation  here ------------------
        # ----------------------------------------------------
        actual_result = 1.0
        nominal_result = 2.0
        # ----------------------------------------------------

        # Setting result
        context.result[s] = {"nominal": nominal_result,
                             "actual": actual_result,
                             "reference": element}
    return True
