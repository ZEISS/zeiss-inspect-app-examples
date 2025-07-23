# -*- coding: utf-8 -*-
#
# test_blackbox.py
#
# The test calls the function get_project_keywords() from the script (UUT) and checks the return value (actual) against the expected result (EXPECTED)
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# ---

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
    assert actual == expected_keywords
