"""
Test for custom probe measured curve element
"""

import math
import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_probe_measured_curve'
SERVICE_TIMEOUT = 10000

CYLINDER_RADIUS = 20.0
HEIGHT = 50.0
N_TURNS = 3.0
PROBE_RADIUS = 1.5
NUM_POINTS = 500
HELIX_PITCH = HEIGHT / N_TURNS  # 50.0 / 3.0 ≈ 16.666...


def test_actual_probe_measured_curve():
    """Test custom actual probe measured curve element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Probe Measured Curve"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_probe_measured_curve',
        name=name,
        values={
            'cylinder_radius': CYLINDER_RADIUS,
            'height': HEIGHT,
            'n_turns': N_TURNS,
            'probe_radius': PROBE_RADIUS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check probe measured curve coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_probe_measured_curve_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens
    assert elem.num_points == NUM_POINTS
    assert math.isclose(elem.helix_pitch, HELIX_PITCH)
