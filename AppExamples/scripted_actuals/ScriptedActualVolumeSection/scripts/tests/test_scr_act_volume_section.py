# -*- coding: utf-8 -*-
#
# test_scr_act_volume_section.py
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


def test_scr_act_volume_section():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    rx = 10.0
    ry = 22.5
    rz = 45.0

    dx = 10.0
    dy = 20.0
    dz = 30.0

    #file = ":ScriptedActualVolumeSection/tests/Grayscale_8bits_palette.png"
    file = ":Grayscale_8bits_palette.png"

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='volume_section',
        name='Test Volume Section 1',
        parameters={
            'file': file,
            'rx': rx, 'ry': ry, 'rz': rz,
            'dx': dx, 'dy': dy, 'dz': dz
        },
        script_uuid='a1b9b0ba-42d0-4bd9-bdbb-f2ac285df7cb'
    )

    test_data_path = 'test_scr_act_volume_section_results'

    #
    # TEST
    #
    expected_user_token = "Scripted Volume Section"
    actual_user_token = test_element.ude_mykey

    path = test_data_path + '_raw.dat'
    actual_result_array = np.array(gom.app.project.actual_elements['Test Volume Section 1'].data.raw)
    array_test = ArrayDataTest(path)
    assert actual_user_token == expected_user_token
    array_test.testArrayValues(actual_result_array)

    path = test_data_path + '_coordinate.dat'
    actual_result_array = np.array(gom.app.project.actual_elements['Test Volume Section 1'].data.coordinate)
    array_test = ArrayDataTest(path)
    array_test.testArrayValues(actual_result_array)


    path = test_data_path + '_normal.dat'
    actual_result_array = np.array(gom.app.project.actual_elements['Test Volume Section 1'].data.normal)
    array_test = ArrayDataTest(path)
    array_test.testArrayValues(actual_result_array)


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_volume_section()
