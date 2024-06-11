# -*- coding: utf-8 -*-
#
# test_dialog_widgets_unit_dialog.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom

# Importing, what we want to test
import unit_dialog_event_handler as example

# Setup test project
# -- This test does not need a project

#
# TEST
#


def test_unit_dialog():
    DIALOG = example.setup_dialog()

    # Test if the widgets are initialized without unit
    assert DIALOG.input.unit == "UNIT_NONE"
    assert DIALOG.tolerances.unit == "UNIT_NONE"

    # Generating some events to test the event_handler
    unit_widget = DIALOG.unit
    unit_widget.value = "FORCE"

    # Test if the event_handler correctly links widget values
    DIALOG.handler(unit_widget)
    assert DIALOG.input.unit == "FORCE"
    assert DIALOG.tolerances.unit == "FORCE"
