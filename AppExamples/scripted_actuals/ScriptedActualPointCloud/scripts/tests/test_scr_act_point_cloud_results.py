# -*- coding: utf-8 -*-
#
# test_scr_act_point_cloud.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys
import numpy as np
from addon import ArrayDataTest


def test_scr_act_point_cloud():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    R = 35.0
    r = 16.0
    u_min = 0.0
    u_max = 3.1416
    u_steps = 600
    v_min = 0.0
    v_max = 3.1416
    v_steps = 300

    # Creating a scripted element
    # Note:
# The triangles are fixed and not available as parameters
# in the example script.
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='point_cloud',
        name='Test Point Cloud 1',
        parameters={
            'R': R, 'r': r,
            'u_min': u_min, 'u_max': u_max, 'u_steps': u_steps,
            'v_min': v_min, 'v_max': v_max, 'v_steps': v_steps
        },
        script_uuid='3457e91a-4a17-47a9-9f5b-045ba2423c70'
    )

    test_data_path = 'test_scr_act_point_cloud_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Point Cloud 1'].data.coordinate)
    array_test = ArrayDataTest(test_data_path)

    expected_user_token = "Scripted Point Cloud"
    actual_user_token = test_element.ude_mykey

    array_test.testArrayValues(actual_result_array)
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_point_cloud()
