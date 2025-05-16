# -*- coding: utf-8 -*-
#
# test_scr_act_volume_region.py
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

def test_scr_act_volume_region():
    # Setup test project
    open_project('volume_test_project', force_reopen=True)

    x0 = 29.0
    y0 = 85.0
    z0 = 106.0

    dx = 24.0
    dy = 5.0
    dz = 8.0

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='volume_region',
        name='Test Volume Region 1',
        parameters={
            'volume_ele': gom.app.project.actual_elements['Linked volume 1'],
            'x0': x0, 'y0': y0, 'z0': z0,
            'dx': dx, 'dy': dy, 'dz': dz
        },
        script_uuid='de9e475c-6502-4fde-9a1a-b133507dfbac'
    )

    test_data_path = 'test_scr_act_volume_region_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Volume Region 1'].data.voxel_data)
    array_test = ArrayDataTest(test_data_path)

    expected_user_token = "Scripted Volume Region"
    actual_user_token = test_element.ude_mykey

    array_test.testArrayValues(actual_result_array)
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_volume_region()
