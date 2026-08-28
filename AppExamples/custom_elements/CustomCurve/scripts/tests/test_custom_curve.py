"""
Test for custom curve element
"""

import gom
import gom.api.services
import math
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_curve'
SERVICE_TIMEOUT = 10000

X0 = 0.0
Y0 = 0.0
Z0 = 0.0
RADIUS = 1.0
J = 0.05
K = 0.1
T_MIN = 0.0
T_MAX = 62.840
NUM_STEPS = 1000
T_RANGE = T_MAX - T_MIN


def test_actual_curve():
    """Test custom actual curve element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Curve"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_curve',
        name=name,
        values={
            'x0': X0, 'y0': Y0, 'z0': Z0,
            'radius': RADIUS, 'j': J, 'k': K,
            't_min': T_MIN, 't_max': T_MAX
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check curve coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_curve_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points == NUM_STEPS
    assert math.isclose(elem.t_range, T_RANGE)


def test_nominal_curve():
    """Test custom nominal curve element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Curve"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_curve',
        name=name,
        values={
            'x0': X0, 'y0': Y0, 'z0': Z0,
            'radius': RADIUS, 'j': J, 'k': K,
            't_min': T_MIN, 't_max': T_MAX
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check curve coordinate data against reference
    nominal_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_curve_nominal_results.dat')
    array_test.testArrayValues(nominal_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points == NUM_STEPS
    assert math.isclose(elem.t_range, T_RANGE)
