"""
Test for custom section element
"""

import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_section'
SERVICE_TIMEOUT = 10000

INPUT_SECTION = 'Plane Y +16.000 mm'
FILTER_MODE = 'Max. Length'


def test_actual_section():
    """Test custom actual section element."""
    open_project('zeiss_part_test_project', force_reopen=True)

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Section"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_section',
        name=name,
        values={
            'i_elem': gom.app.project.actual_elements[INPUT_SECTION],
            'i_mode': FILTER_MODE
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check section coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_section_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points > 0
    assert elem.section_length > 0


def test_nominal_section():
    """Test custom nominal section element."""
    open_project('zeiss_part_test_project', force_reopen=True)

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Section"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_section',
        name=name,
        values={
            'i_elem': gom.app.project.actual_elements[INPUT_SECTION],
            'i_mode': FILTER_MODE
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check section coordinate data against reference
    nominal_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_section_nominal_results.dat')
    array_test.testArrayValues(nominal_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points > 0
    assert elem.section_length > 0

