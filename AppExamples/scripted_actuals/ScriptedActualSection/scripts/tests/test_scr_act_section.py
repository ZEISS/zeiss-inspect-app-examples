# -*- coding: utf-8 -*-
#
# test_scr_act_section.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import os
import sys
import numpy as np
from addon import ArrayDataTest

from ExampleProjects.setup_project import open_project


def test_scr_act_section():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='section',
        name='Test Section 1',
        parameters={
            'i_elem': gom.app.project.actual_elements['Plane Y +16.000 mm'],
            'i_mode': 'Max. Length'
        },
        script_uuid='06d1fc77-5d6a-48a1-9f01-cc4cb07466c9'
    )

    test_data_path = 'test_scr_act_section.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Section 1'].data.coordinate)
    array_test = ArrayDataTest(test_data_path)

    expected_user_token = "Scripted Section"
    actual_user_token = test_element.ude_mykey

    array_test.testArrayValues(actual_result_array)
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_section()
