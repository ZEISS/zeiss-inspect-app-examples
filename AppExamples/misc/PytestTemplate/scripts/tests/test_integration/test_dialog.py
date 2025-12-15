""" Integration test example for user-definded dialogs

See App Development Documentation: Testing Apps -- Testing Apps with dialogs

Carl Zeiss GOM Metrology GmbH, 2025
"""


# Import unit-under-test (UUT)
import uut_project_keywords
from gom_test_helpers.dialogs.AutoDialogContext import AutoDialogContext

def dialog_callback(dialog):
    '''Callback function for simulating interaction with user-defined dialog'''
    if 'Project Keywords' in dialog.title:
        dialog.project.value = 'Pytest Project'
        dialog.inspector.value = 'Pytest'
        return 'ok'

def test_dialog():
    '''Automatically executing the dialog with callback'''
    with AutoDialogContext(dialog_callback):
        result = uut_project_keywords.edit_project_keywords()
        assert result.project == 'Pytest Project'
        assert result.inspector == 'Pytest'
