# -*- coding: utf-8 -*-
#
# test_scr_act_volume.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys
import math
import numpy as np
from addon import ArrayDataTest


def test_scr_act_volume():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    gv_background = 0x1000
    gv_mat1 = 0xC000
    gv_mat2 = 0x9000
    minimum_gray_value = gv_background
    maximum_gray_value = max(gv_mat1, gv_mat2)
    dx = 1
    dy = 2
    dz = 3
    rx = math.pi / 8
    ry = math.pi / 4
    rz = math.pi / 2

    # Creating a scripted element
    # Note:
    # The parameters currently only define the position of the volume,
    # not its shape/voxel data.
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='volume',
        name='Test Volume 1',
        parameters={
            'gv_background': gv_background, 'gv_mat1': gv_mat1, 'gv_mat2': gv_mat2,
            'dx': dx, 'dy': dy, 'dz': dz,
            'rx': rx, 'ry': ry, 'rz': rz
        },
        script_uuid='5c0e7e3f-cf8c-4acd-8526-85b895b3f902'
    )

    test_data_path = 'test_scr_act_volume_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Volume 1'].data.voxel_data)
    array_test = ArrayDataTest(test_data_path)

    expected_user_token = "Scripted Volume"
    actual_user_token = test_element.ude_mykey

    array_test.testArrayValues(actual_result_array)
    assert minimum_gray_value == gom.app.project.actual_elements['Test Volume 1'].minimum_gray_value
    assert maximum_gray_value == gom.app.project.actual_elements['Test Volume 1'].maximum_gray_value
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_volume()
