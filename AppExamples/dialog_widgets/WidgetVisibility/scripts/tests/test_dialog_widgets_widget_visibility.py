# -*- coding: utf-8 -*-
#
# test_dialog_widgets_widget_visibility.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom

# Importing, what we want to test
import widget_visibility as example

# Setup test project
# -- This test does not need a project

#
# TEST
#


def test_widget_visibility():
    DIALOG = example.setup_dialog()
    gom.script.sys.open_user_defined_dialog(dialog=DIALOG)

    # Test if the widgets are initialized correctly
    assert DIALOG.label_bottom.visible == False

    # Generating some events to test the event_handler
    button_widget = DIALOG.button

    # Test if the event_handler toggles correctly
    DIALOG.handler(button_widget)
    assert DIALOG.label_bottom.visible == True
    DIALOG.handler(button_widget)
    assert DIALOG.label_bottom.visible == False

    gom.script.sys.close_user_defined_dialog(dialog=DIALOG)
