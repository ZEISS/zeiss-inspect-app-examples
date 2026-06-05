"""
Test for custom volume defects element
"""

import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume_defects'
SERVICE_TIMEOUT = 10000

# Tetrahedron vertices — matching the dialog defaults, proper non-coplanar geometry
V0 = ( 0.0,  0.0, 10.0)
V1 = ( 5.0,  0.0,  0.0)
V2 = (-5.0, -5.0,  0.0)
V3 = (-5.0,  5.0,  0.0)


def test_actual_volume_defects():
    """Test custom actual volume defects element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Volume Defects"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume_defects',
        name=name,
        values={
            'v0_x': V0[0], 'v0_y': V0[1], 'v0_z': V0[2],
            'v1_x': V1[0], 'v1_y': V1[1], 'v1_z': V1[2],
            'v2_x': V2[0], 'v2_y': V2[1], 'v2_z': V2[2],
            'v3_x': V3[0], 'v3_y': V3[1], 'v3_z': V3[2]
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check volume defect coordinate data against reference
    actual_result_array = np.array(elem.data.coordinate)
    array_test = ArrayDataTest('test_custom_volume_defects_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens
    assert elem.num_vertices == 4
    assert elem.num_triangles == 4
