#
# test_scripted_curve_check.py
#
# Carl Zeiss GOM Metrology GmbH, 2026
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2027/python_examples/
# ---

import gom
import numpy as np

from addon import ElementTest
from ExampleProjects.setup_project import open_project


def test_scripted_curve_check():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='scalar_curve',
        element_type='none',
        name='Plane X +0.00 mm.ScrCrv',
        parameters={'abbreviation': 'ScrCrv',
                    'checked_element': gom.app.project.actual_elements['Plane X +0.00 mm'],
                    'coordinate_system': None,
                    'tolerance': 'off',
                    'unit': 'UNIT_NONE'},
        script_uuid='fe923c4f-9184-4e09-b5fb-1be04900ff61')
    #
    # TEST
    #
    element_test = ElementTest('test_data/scripted_curve_check.dat')
    element_test.testElementValues(
        test_element, ['scalar_value', 'computation_status', 'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()

def test_scripted_curve_check_cs():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='scalar_curve',
        element_type='none',
        name='Plane X +0.00 mm.ScrCrv',
        parameters={'abbreviation': 'ScrCrv',
                    'checked_element': gom.app.project.actual_elements['Plane X +0.00 mm'],
                    'coordinate_system': gom.app.project.inspection['Cylinder 1|Plane 1|Origin'],
                    'tolerance': 'off',
                    'unit': 'UNIT_NONE'},
        script_uuid='fe923c4f-9184-4e09-b5fb-1be04900ff61')
    #
    # TEST
    #
    element_test = ElementTest('test_data/scripted_curve_check_cs.dat')
    element_test.testElementValues(
        test_element, ['scalar_value', 'computation_status', 'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()

