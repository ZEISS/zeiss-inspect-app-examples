# -*- coding: utf-8 -*-
#
# test_data_interfaces_check_results.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom

from ExampleProjects.setup_project import open_project
from addon import ArrayDataTest

# Importing the example we want to test
import check_results_data_array as example


def test_check_results():
    # Setup test project
    open_project('zeiss_part_test_project')
    test_element = gom.app.project.inspection['Surface comparison 1']
    #
    # TEST
    #
    expected_single_value = -0.1673445701599121
    assert expected_single_value == example.get_single_result_value(test_element)

    actual_result_array = example.get_result_values_array(test_element)
    test = ArrayDataTest('test_data/data_interfaces_check_results.dat')
    test.testArrayValues(actual_result_array)
