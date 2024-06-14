# -*- coding: utf-8 -*-
#
# test_scripted_checks.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np

from addon import ElementTest
from ExampleProjects.setup_project import open_project


def test_scripted_check_scalar():
    # Setup test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Creating a scripted element
    test_element = gom.script.sys.create_element_by_script(
        check_type='scalar',
        element_type='none',
        name='Cylinder 1.ScrSca',
        parameters={'abbreviation': 'ScrSca',
                    'checked_element': gom.app.project.inspection['Cylinder 1'], 'tolerance': 'off', 'unit': 'UNIT_NONE'},
        script_uuid='d77d2a1e-bb74-447a-84af-a1cb1f8e49a6')
    #
    # TEST
    #
    element_test = ElementTest('test_data/scripted_checks_scalar.dat')
    element_test.testElementValues(
        test_element, ['scalar_value', 'computation_status', 'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()
