"""
Test for custom volume section element
"""

import gom
import gom.api.services
import numpy as np
from addon import ArrayDataTest

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume_section'
SERVICE_TIMEOUT = 10000

RX = 10.0
RY = 22.5
RZ = 45.0
DX = 10.0
DY = 20.0
DZ = 30.0

# App resource path to the test image (avoids dependency on an external file)
TEST_IMAGE = ':Grayscale_8bits_palette.png'


def test_actual_volume_section():
    """Test custom actual volume section element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Volume Section"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume_section',
        name=name,
        values={
            'file': TEST_IMAGE,
            'rx': RX, 'ry': RY, 'rz': RZ,
            'dx': DX, 'dy': DY, 'dz': DZ
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]

    # Check raw pixel data against reference
    array_test = ArrayDataTest('test_custom_volume_section_raw.dat')
    array_test.testArrayValues(np.array(elem.data.raw))

    # Check 3D coordinates of section pixels against reference
    array_test = ArrayDataTest('test_custom_volume_section_coordinate.dat')
    array_test.testArrayValues(np.array(elem.data.coordinate))

    # Check section pixel normals against reference
    array_test = ArrayDataTest('test_custom_volume_section_normal.dat')
    array_test.testArrayValues(np.array(elem.data.normal))

    # Check custom data tokens
    assert elem.image_file == TEST_IMAGE
