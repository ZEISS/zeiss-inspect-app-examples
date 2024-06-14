# -*- coding: utf-8 -*-
#
# test_scr_act_circle.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys


def test_scr_act_circle():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    center_x = 1.0
    center_y = 2.0
    center_z = 3.0
    dir_x = 4.0
    dir_y = 5.0
    dir_z = 6.0
    radius = 42.0

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='circle',
        name='Test Circle 1',
        parameters={
            'center_x': center_x, 'center_y': center_y, 'center_z': center_z,
            'dir_x': dir_x, 'dir_y': dir_y, 'dir_z': dir_z, 'radius': radius
        },
        script_uuid='66cca9a5-abb7-4866-b5eb-d8aac67a4a3f'
    )

    #
    # TEST
    #
    center_actual = (
        gom.app.project.actual_elements['Test Circle 1'].center_coordinate.x,
        gom.app.project.actual_elements['Test Circle 1'].center_coordinate.y,
        gom.app.project.actual_elements['Test Circle 1'].center_coordinate.z
    )
    dir_actual = (
        gom.app.project.actual_elements['Test Circle 1'].normal.x,
        gom.app.project.actual_elements['Test Circle 1'].normal.y,
        gom.app.project.actual_elements['Test Circle 1'].normal.z
    )

    expected_user_token = "Scripted Circle"
    actual_user_token = test_element.ude_mykey

    assert (center_x, center_y, center_z) == center_actual
    assert (dir_x, dir_y, dir_z) == dir_actual
    assert radius == gom.app.project.actual_elements['Test Circle 1'].diameter / 2.0
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_circle()
