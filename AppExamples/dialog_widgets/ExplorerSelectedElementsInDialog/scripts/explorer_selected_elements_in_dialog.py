# -*- coding: utf-8 -*-
#
# explorer_selected_elements_in_dialog.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
from ExampleProjects.setup_project import open_project


# Gets the names of all elements currently selected in "Actual Elements"
def get_selected_actual_names():
    # -------------------------------------------------------------------------
    actual_elements = gom.ElementSelection(
        {'category': ['key', 'elements', 'part', gom.app.project.parts['Training Object'], 'explorer_category', 'actual']})
    selected_actuals = [element.name for element in actual_elements if element.is_selected]
    # -------------------------------------------------------------------------
    return selected_actuals


# Setup dialog from file and apply handler function.
#
# The handler reads selected elements in the project and
# exemplarily shows the names of selected elements
def setup_dialog():
    DIALOG = gom.script.sys.create_user_defined_dialog(file='explorer_selected_elements_in_dialog.gdlg')

    def dialog_event_handler(widget):
        if str(widget) == 'system':
            return

        # Handling first start and clicking "Refresh" button
        if str(widget) == 'initialize' or widget == DIALOG.refresh:
            selected_actuals = get_selected_actual_names()
            DIALOG.text.text = "<br>".join(selected_actuals)
            return

    DIALOG.handler = dialog_event_handler
    return DIALOG


#
# Example execution
#
if __name__ == '__main__':
    open_project('zeiss_part_test_project')
    # -------------------------------------------------------------------------
    example_selection = [gom.app.project.actual_elements['Plane 1'],
                         gom.app.project.actual_elements['Plane X +0.00 mm']]
    gom.script.explorer.apply_selection(selection=example_selection)
    # -------------------------------------------------------------------------
    DIALOG = setup_dialog()
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
