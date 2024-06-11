# -*- coding: utf-8 -*-
#
# test_scr_act_surface_curve.py
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
import math
from addon import ArrayDataTest


def test_scr_act_surface_curve():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    r = 20
    theta = math.pi / 6
    phi_min = math.pi * 0.5
    phi_max = math.pi * 1.5

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='surface_curve',
        name='Test Surface Curve 1',
        parameters={
            'r': r, 'theta': theta,
            'phi_min': phi_min, 'phi_max': phi_max
        },
        script_uuid='2404f3c0-bbcc-47f8-9508-9b5021514c33'
    )

    test_data_path = 'test_scr_act_surface_curve_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Surface Curve 1'].data.coordinate)
    array_test = ArrayDataTest(test_data_path)

    array_test.testArrayValues(actual_result_array)


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_surface_curve()
