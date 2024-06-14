# -*- coding: utf-8 -*-
#
# test_scr_act_cone.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys


def test_scr_act_cone():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    # Note:
    # Currently the relation of radius_1 / radius_2 has an impact on the
    # assignment of coordinates between script and actual element, i.e.
    # the actual elements' coordinates are swapped if radius_1 > radius_2.
    # See https://jira.gom.com/browse/SW2024-2241

    p1_x = 1.0
    p1_y = 2.0
    p1_z = 3.0
    p2_x = 40.0
    p2_y = 50.0
    p2_z = 60.0
    radius_1 = 4.2
    radius_2 = 42.0

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='cone',
        name='Test Cone 1',
        parameters={
            'p1_x': p1_x, 'p1_y': p1_y, 'p1_z': p1_z,
            'p2_x': p2_x, 'p2_y': p2_y, 'p2_z': p2_z,
            'radius_1': radius_1, 'radius_2': radius_2
        },
        script_uuid='3ef80e13-625c-4beb-8743-951c3b09710b'
    )

    #
    # TEST
    #
    p1_actual = (
        gom.app.project.actual_elements['Test Cone 1'].coordinate1.x,
        gom.app.project.actual_elements['Test Cone 1'].coordinate1.y,
        gom.app.project.actual_elements['Test Cone 1'].coordinate1.z
    )
    p2_actual = (
        gom.app.project.actual_elements['Test Cone 1'].coordinate2.x,
        gom.app.project.actual_elements['Test Cone 1'].coordinate2.y,
        gom.app.project.actual_elements['Test Cone 1'].coordinate2.z
    )

    print(f'point1: {p1_actual}')
    print(f'point2: {p2_actual}')

    expected_user_token = "Scripted Cone"
    actual_user_token = test_element.ude_mykey

    assert (p1_x, p1_y, p1_z) == p1_actual
    assert (p2_x, p2_y, p2_z) == p2_actual
    assert radius_1 == gom.app.project.actual_elements['Test Cone 1'].diameter1 / 2.0
    assert radius_2 == gom.app.project.actual_elements['Test Cone 1'].diameter2 / 2.0
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_cone()
