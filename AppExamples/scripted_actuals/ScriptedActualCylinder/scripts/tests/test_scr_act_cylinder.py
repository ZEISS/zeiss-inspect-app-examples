# -*- coding: utf-8 -*-
#
# test_scr_act_cylinder.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os
import sys


def test_scr_act_cylinder():
    # Setup test project
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    point_x = 1.0
    point_y = 2.0
    point_z = 3.0
    dir_x = 4.0
    dir_y = 5.0
    dir_z = 6.0
    radius = 42.0
    inner = False

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='cylinder',
        name='Test Cylinder 1',
        parameters={
            'point_x': point_x, 'point_y': point_y, 'point_z': point_z,
            'dir_x': dir_x, 'dir_y': dir_y, 'dir_z': dir_z, 'radius': radius,
            'inner': inner
        },
        script_uuid='0007d9a7-160b-4bdd-b69a-92c399d8a36d'
    )

    #
    # TEST
    #
    point_actual = (
        gom.app.project.actual_elements['Test Cylinder 1'].coordinate1.x,
        gom.app.project.actual_elements['Test Cylinder 1'].coordinate1.y,
        gom.app.project.actual_elements['Test Cylinder 1'].coordinate1.z
    )
    dir_actual = (
        gom.app.project.actual_elements['Test Cylinder 1'].direction.x,
        gom.app.project.actual_elements['Test Cylinder 1'].direction.y,
        gom.app.project.actual_elements['Test Cylinder 1'].direction.z
    )

    expected_user_token = "Scripted Cylinder"
    actual_user_token = test_element.ude_mykey

    assert (point_x, point_y, point_z) == point_actual
    assert (dir_x, dir_y, dir_z) == dir_actual
    assert radius == gom.app.project.actual_elements['Test Cylinder 1'].diameter / 2.0
    assert inner == gom.app.project.actual_elements['Test Cylinder 1'].is_inner_surface
    assert expected_user_token == actual_user_token


#
# Test execution
#
if __name__ == '__main__':
    test_scr_act_cylinder()
