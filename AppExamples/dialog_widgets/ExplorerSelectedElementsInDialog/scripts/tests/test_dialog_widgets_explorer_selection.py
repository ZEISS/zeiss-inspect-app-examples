# -*- coding: utf-8 -*-
#
# test_dialog_widgets_explorer_selection.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom

from ExampleProjects.setup_project import open_project

# Importing the example we want to test
import explorer_selected_elements_in_dialog as example


def test_explorer_selection():
    # Setup test project
    open_project('zeiss_part_test_project')
    test_element_names = ['Plane 1', 'Plane X +0.00 mm']
    test_selection = [gom.app.project.actual_elements[name] for name in test_element_names]
    gom.script.explorer.apply_selection(selection=test_selection)

    #
    # TEST
    #
    DIALOG = example.setup_dialog()
    actual_names = example.get_selected_actual_names()

    # Test if actual names function is correct
    assert actual_names == test_element_names

    # Test if dialog handler works correct
    DIALOG.handler("initialize")
    assert DIALOG.text.text == "<br>".join(actual_names)
