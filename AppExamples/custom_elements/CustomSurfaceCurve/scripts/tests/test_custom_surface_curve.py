"""
Test for custom surface curve element
"""

import math
import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_surface_curve'
SERVICE_TIMEOUT = 10000

R = 20.0
THETA = math.pi / 6
PHI_MIN = math.pi * 0.5
PHI_MAX = math.pi * 1.5
NUM_POINTS = 1000
PHI_RANGE = math.pi  # PHI_MAX - PHI_MIN


def test_actual_surface_curve():
    """Test custom actual surface curve element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Surface Curve"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_surface_curve',
        name=name,
        values={'r': R, 'theta': THETA, 'phi_min': PHI_MIN, 'phi_max': PHI_MAX}
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check surface curve coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_surface_curve_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens
    assert elem.num_points == NUM_POINTS
    assert math.isclose(elem.phi_range, PHI_RANGE)


def test_nominal_surface_curve():
    """Test custom nominal surface curve element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Surface Curve"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_surface_curve',
        name=name,
        values={'r': R, 'theta': THETA, 'phi_min': PHI_MIN, 'phi_max': PHI_MAX}
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check surface curve coordinate data against reference
    nominal_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_surface_curve_nominal_results.dat')
    array_test.testArrayValues(nominal_result_array)
    # Check custom element data tokens
    assert elem.num_points == NUM_POINTS
    assert math.isclose(elem.phi_range, PHI_RANGE)
