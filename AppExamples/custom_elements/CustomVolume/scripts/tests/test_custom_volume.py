"""
Test for custom volume element
"""

import math
import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume'
SERVICE_TIMEOUT = 10000

GV_BACKGROUND = 0x1000   # 4096
GV_MAT1 = 0xC000          # 49152
GV_MAT2 = 0x9000          # 36864
DX = 1.0
DY = 2.0
DZ = 3.0
RX = math.pi / 8
RY = math.pi / 4
RZ = math.pi / 2

# Total voxels: core (70) + 2×padding (30) on each axis → 130^3
NUM_VOXELS = 130 * 130 * 130

MINIMUM_GRAY_VALUE = GV_BACKGROUND
MAXIMUM_GRAY_VALUE = max(GV_MAT1, GV_MAT2)


def test_actual_volume():
    """Test custom actual volume element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Volume"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume',
        name=name,
        values={
            'gv_background': GV_BACKGROUND,
            'gv_mat1': GV_MAT1,
            'gv_mat2': GV_MAT2,
            'dx': DX, 'dy': DY, 'dz': DZ,
            'rx': RX, 'ry': RY, 'rz': RZ
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check volume voxel data against reference
    actual_result_array = np.array(elem.data.voxel_data)
    array_test = ArrayDataTest('test_custom_volume_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check software-computed gray value range
    assert MINIMUM_GRAY_VALUE == elem.minimum_gray_value
    assert MAXIMUM_GRAY_VALUE == elem.maximum_gray_value
    # Check custom element data token
    assert elem.num_voxels == NUM_VOXELS
