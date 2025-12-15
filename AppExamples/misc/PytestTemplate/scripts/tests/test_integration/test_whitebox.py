""" Whitebox integration test example

The test calls the function get_project_keywords() from the script (UUT) and checks the return value (actual)
against the expected result (EXPECTED). Only items in expected_keywords are checked, i.e. any additional actual
keywords are ignored.

Carl Zeiss GOM Metrology GmbH, 2025
"""

import gom

# Name of the UUT (unit-under-test) script
import uut_project_keywords


def test_whitebox():
    gom.script.sys.close_project()
    gom.script.sys.create_project()
    
    '''Executing a UUT function'''
    expected_keywords = {'user_inspector': {'description': 'Inspector', 'value': 'Clouseau'},
                         'user_project': {'description': 'Project Name', 'value': 'Test Project'}}

    uut_project_keywords.main()
    actual = uut_project_keywords.get_project_keywords()
    
    # Check if all expected keys and their corresponding values match in actual
    for key in expected_keywords.keys():
        assert key in actual, f"Key '{key}' not found in actual keywords"
        assert actual[key] == expected_keywords[key], f"{key}: Expected {expected_keywords[key]}, but got {actual[key]}"
