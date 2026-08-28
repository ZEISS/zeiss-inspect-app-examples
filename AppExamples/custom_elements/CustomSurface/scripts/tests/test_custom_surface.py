"""
Test for custom surface element
"""

import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_surface'
SERVICE_TIMEOUT = 10000

VERTICES = {
    'v0_x': 10.0, 'v0_y': -10.0, 'v0_z': -10.0,
    'v1_x': 10.0, 'v1_y':  10.0, 'v1_z': -10.0,
    'v2_x': 10.0, 'v2_y':  10.0, 'v2_z':  10.0,
    'v3_x': 10.0, 'v3_y': -10.0, 'v3_z':  10.0,
    'v4_x': -10.0, 'v4_y': -10.0, 'v4_z': -10.0,
    'v5_x': -10.0, 'v5_y':  10.0, 'v5_z': -10.0,
    'v6_x': -10.0, 'v6_y':  10.0, 'v6_z':  10.0,
    'v7_x': -10.0, 'v7_y': -10.0, 'v7_z':  10.0,
}
NUM_VERTICES = 8


def test_actual_surface():
    """Test custom actual surface element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Surface"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_surface',
        name=name,
        values=VERTICES
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check surface coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_surface_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_vertices == NUM_VERTICES


def test_nominal_surface():
    """Test custom nominal surface element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Surface"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_surface',
        name=name,
        values=VERTICES
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check surface coordinate data against reference
    nominal_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_surface_nominal_results.dat')
    array_test.testArrayValues(nominal_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_vertices == NUM_VERTICES
