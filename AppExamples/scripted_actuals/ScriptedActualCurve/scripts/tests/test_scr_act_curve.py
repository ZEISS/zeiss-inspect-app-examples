
# -*- coding: utf-8 -*-
#
# test_scr_act_curve.py
#
# Carl Zeiss GOM Metrology GmbH, 2023
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import os
import sys
import numpy as np
from addon import ArrayDataTest


def test_ex03_curve():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    r = 1.0
    j = 0.05
    k = 0.1
    t_min = 0
    t_max = 62.840

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='curve',
        name='Test Curve 1',
        parameters={
            'x0': x0, 'y0': y0, 'z0': z0, 'radius': r,
            'j': j, 'k': k, 't_min': t_min, 't_max': t_max
        },
        script_uuid='4ab57011-ead1-4a66-9681-8d61e3fb971c'
    )

    test_data_path = 'test_scr_act_curve_results.dat'

    #
    # TEST
    #
    actual_result_array = np.array(gom.app.project.actual_elements['Test Curve 1'].data.coordinate)
    array_test = ArrayDataTest(test_data_path)

    array_test.testArrayValues(actual_result_array)


#
# Test execution
#
if __name__ == '__main__':
    test_ex03_curve()
