# -*- coding: utf-8 -*-
#
# test_scr_act_surface.py
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


def test_scr_act_surface():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    v0_x = 10.0
    v0_y = -10.0
    v0_z = -10.0

    v1_x = 10.0
    v1_y = 10.0
    v1_z = -10.0

    v2_x = 10.0
    v2_y = 10.0
    v2_z = 10.0

    v3_x = 10.0
    v3_y = -10.0
    v3_z = 10.0

    v4_x = -10.0
    v4_y = -10.0
    v4_z = -10.0

    v5_x = -10.0
    v5_y = 10.0
    v5_z = -10.0

    v6_x = -10.0
    v6_y = 10.0
    v6_z = 10.0

    v7_x = -10.0
    v7_y = -10.0
    v7_z = 10.0

    # Creating a scripted element
    # Note:
    # The triangles are fixed and not available as parameters
    # in the example script.
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='surface',
        name='Test Surface 1',
        parameters={
            'v0_x': v0_x, 'v0_y': v0_y, 'v0_z': v0_z,
            'v1_x': v1_x, 'v1_y': v1_y, 'v1_z': v1_z,
            'v2_x': v2_x, 'v2_y': v2_y, 'v2_z': v2_z,
            'v3_x': v3_x, 'v3_y': v3_y, 'v3_z': v3_z,
            'v4_x': v4_x, 'v4_y': v4_y, 'v4_z': v4_z,
            'v5_x': v5_x, 'v5_y': v5_y, 'v5_z': v5_z,
            'v6_x': v6_x, 'v6_y': v6_y, 'v6_z': v6_z,
            'v7_x': v7_x, 'v7_y': v7_y, 'v7_z': v7_z
        },
        script_uuid='d22db76e-4f9e-49c4-9d57-9a4bd0756422'
    )

    test_data_path = 'test_scr_act_surface_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Surface 1'].data.coordinate)
    array_test = ArrayDataTest(test_data_path)

    expected_user_token = "Scripted Surface"
    actual_user_token = test_element.ude_mykey

    array_test.testArrayValues(actual_result_array)
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_surface()
