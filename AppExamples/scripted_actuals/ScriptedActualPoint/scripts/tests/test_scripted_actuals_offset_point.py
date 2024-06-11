# -*- coding: utf-8 -*-
#
# test_scripted_actuals_simple_offset_point.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This test is part of the "Python API Examples" Add-on. For documentation, see:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np

from addon import ElementTest
from ExampleProjects.setup_project import open_project


def test_simple_offset_point():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='point',
        name='My scripted point',
        parameters={'base': gom.app.project.inspection['Cylinder 1|Plane 1|Origin'], 'x': 6.0},
        script_uuid='dda4f4d3-b9e8-4dc8-9f7c-355c92299022')
    #
    # TEST
    #
    element_test = ElementTest('scripted_actuals_simple_point.dat')
    element_test.testElementValues(test_element, ['center_coordinate', 'computation_status'])
    element_test.callTest()


def test_offset_point_v2():
    # Setup test project
    open_project('zeiss_part_test_project')

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='none',
        element_type='point',
        name='Offset point 1',
        parameters={'base': gom.app.project.inspection['Cylinder 1|Plane 1|Origin'], 'x': 5.0, 'y': 0.0, 'z': 16.0},
        script_uuid='43aa2e6e-b79e-4861-9645-1af8c6a398f7')

    #
    # TEST
    #
    element_test = ElementTest('scripted_actuals_point_v2.dat')
    element_test.testElementValues(test_element, ['center_coordinate', 'computation_status', 'ude_mykey'])
    element_test.callTest()
    
#
# Test execution
#
if __name__ == '__main__':
     test_simple_offset_point()
     test_offset_point_v2()
