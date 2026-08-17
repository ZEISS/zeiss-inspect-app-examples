#
# test_scripted_surface_check.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np

from addon import ElementTest
from ExampleProjects.setup_project import open_project


def test_scripted_surface_check():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='scalar_surface',
        element_type='none',
        name='Training Object.ScrSrf',
        parameters={'abbreviation': 'ScrSrf',
                    'checked_element': gom.app.project.parts['Training Object'].actual,
    'coordinate_system': None,
    'tolerance': 'off',
    'unit': 'UNIT_NONE'},
        script_uuid='e453abcb-1b50-46cd-a3da-ae9e8ca7a859')
    #
    # TEST
    #
    element_test = ElementTest('test_data/scripted_surface_check.dat')
    element_test.testElementValues(
        test_element, ['scalar_value', 'computation_status', 'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()

def test_scripted_surface_check_cs():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='scalar_surface',
        element_type='none',
        name='Training Object CS.ScrSrf',
        parameters={'abbreviation': 'ScrSrf',
                    'checked_element': gom.app.project.parts['Training Object'].actual,
    'coordinate_system': gom.app.project.inspection['Cylinder 1|Plane 1|Origin'],
    'tolerance': 'off',
    'unit': 'UNIT_NONE'},
        script_uuid='e453abcb-1b50-46cd-a3da-ae9e8ca7a859')
    #
    # TEST
    #
    element_test = ElementTest('test_data/scripted_surface_check_cs.dat')
    element_test.testElementValues(
        test_element, ['scalar_value', 'computation_status', 'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()

