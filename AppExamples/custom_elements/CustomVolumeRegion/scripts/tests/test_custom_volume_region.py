"""
Test for custom volume region element
"""

import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume_region'
SERVICE_TIMEOUT = 10000

# Region of interest parameters — matching the dialog defaults
X0, Y0, Z0 = 29.0, 85.0, 106.0
DX, DY, DZ = 24.0, 5.0, 8.0


def test_actual_volume_region():
    """Test custom actual volume region element."""
    open_project('volume_test_project', force_reopen=True)

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Volume Region"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume_region',
        name=name,
        values={
            'volume_ele': gom.app.project.actual_elements['Linked volume 1'],
            'x0': X0, 'y0': Y0, 'z0': Z0,
            'dx': DX, 'dy': DY, 'dz': DZ
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check voxel data against reference
    actual_result_array = np.array(elem.data.voxel_data)
    array_test = ArrayDataTest('test_custom_volume_region_actual_results.dat')
    array_test.testArrayValues(actual_result_array)
    # Check custom element data tokens
    volume = gom.app.project.actual_elements['Linked volume 1']
    dx_vox = int(DX / volume.voxel_size.x)
    dy_vox = int(DY / volume.voxel_size.y)
    dz_vox = int(DZ / volume.voxel_size.z)
    assert elem.num_voxels == dx_vox * dy_vox * dz_vox
