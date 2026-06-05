"""
Test for custom point cloud element
"""

import gom
import gom.api.services
import math
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_point_cloud'
SERVICE_TIMEOUT = 10000

R = 35.0
r = 16.0
U_MIN = 0.0
U_MAX = 3.1416
U_STEPS = 600
V_MIN = 0.0
V_MAX = 3.1416
V_STEPS = 300
NUM_POINTS = U_STEPS * V_STEPS
U_RANGE = U_MAX - U_MIN


def test_actual_point_cloud():
    """Test custom actual point cloud element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Point Cloud"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_point_cloud',
        name=name,
        values={
            'R': R, 'r': r,
            'u_min': U_MIN, 'u_max': U_MAX, 'u_steps': U_STEPS,
            'v_min': V_MIN, 'v_max': V_MAX, 'v_steps': V_STEPS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check point cloud coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_point_cloud_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points == NUM_POINTS
    assert math.isclose(elem.u_range, U_RANGE)


def test_nominal_point_cloud():
    """Test custom nominal point cloud element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Point Cloud"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_point_cloud',
        name=name,
        values={
            'R': R, 'r': r,
            'u_min': U_MIN, 'u_max': U_MAX, 'u_steps': U_STEPS,
            'v_min': V_MIN, 'v_max': V_MAX, 'v_steps': V_STEPS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check point cloud coordinate data against reference
    nominal_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_point_cloud_nominal_results.dat')
    array_test.testArrayValues(nominal_result_array)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.num_points == NUM_POINTS
    assert math.isclose(elem.u_range, U_RANGE)
