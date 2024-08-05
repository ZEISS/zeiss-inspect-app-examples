# -*- coding: utf-8 -*-
#
# test_blackbox.py
#
# The test calls the function get_project_keywords() from the script (UUT) and checks the return value (actual) agains the expected result (EXPECTED)
#
# Carl Zeiss GOM Metrology GmbH, 2024
# 
# ---

import gom

# Name of the UUT script
import uut_project_keywords

def test_whitebox():
	'''Executing a UUT function'''
	EXPECTED = {'user_inspector': {'description': 'Inspector', 'value': 'Clouseau'}, 'user_project': {'description': 'Project Name', 'value': 'Test Project'}}

	actual = uut_project_keywords.get_project_keywords()
	assert actual == EXPECTED
