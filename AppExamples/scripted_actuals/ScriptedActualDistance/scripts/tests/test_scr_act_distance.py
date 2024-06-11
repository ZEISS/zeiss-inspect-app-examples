# -*- coding: utf-8 -*-
#
# test_scr_act_distance.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys


def test_scr_act_distance():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    p1_x = 1.0
    p1_y = 2.0
    p1_z = 3.0
    p2_x = -1.0
    p2_y = -2.0
    p2_z = -3.0

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='distance',
        name='Test Distance 1',
        parameters={
            'p1_x': p1_x, 'p1_y': p1_y, 'p1_z': p1_z, 'p2_x': p2_x, 'p2_y': p2_y, 'p2_z': p2_z
        },
        script_uuid='bf597507-04cc-4b36-b482-f586240d359b'
    )

    #
    # TEST
    #
    p1_actual = (
        gom.app.project.actual_elements['Test Distance 1'].coordinate1.x,
        gom.app.project.actual_elements['Test Distance 1'].coordinate1.y,
        gom.app.project.actual_elements['Test Distance 1'].coordinate1.z
    )
    p2_actual = (
        gom.app.project.actual_elements['Test Distance 1'].coordinate2.x,
        gom.app.project.actual_elements['Test Distance 1'].coordinate2.y,
        gom.app.project.actual_elements['Test Distance 1'].coordinate2.z
    )

    expected_user_token = "Scripted Distance"
    actual_user_token = test_element.ude_mykey

    assert (p1_x, p1_y, p1_z) == p1_actual
    assert (p2_x, p2_y, p2_z) == p2_actual
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_distance()
