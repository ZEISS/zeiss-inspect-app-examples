# -*- coding: utf-8 -*-
#
# test_dialog_widgets_dropdown_widget.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom

# Importing, what we want to test
import dropdown_widget as example

# Setup test project
# -- This test does not need a project

#
# TEST
#


def test_dropdown_widget():
    DIALOG = example.setup_dialog()

    # Test if the widgets are initialized without unit
    assert DIALOG.list.items == [' yes', 'we', 'can']
