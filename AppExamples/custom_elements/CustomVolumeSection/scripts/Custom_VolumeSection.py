"""
Custom actual VolumeSection Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray.

Mirrors the functionality of the ScriptedActualVolumeSection example:
a grayscale image loaded from disk (or an App resource for testing) is
placed in 3D space via a full 4x4 rotation + translation matrix.
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import numpy as np
from math import sin, cos
from io import BytesIO

from PIL import Image

from gom import apicontribution

# Allowed image formats (security: restrict formats to prevent decompression bombs
# and other image-based attacks; see ZEISS/zeiss-inspect-app-examples/security/dependabot/3)
ALLOWED_FORMATS = ['JPEG', 'PNG', 'GIF', 'TIFF']


def _create_volume_section(values):
    """
    Build a volume section from a grayscale image and a placement transformation.

    The image file is converted to a grayscale float32 array that serves as
    the section's pixel data. The placement is defined by rotation angles
    (rx, ry, rz) and translation (dx, dy, dz) assembled into a gom.Mat4x4.

    If the filename starts with ':', it is treated as an App resource path
    (used internally for automated testing without an external file).

    :param values: dict with keys file, rx, ry, rz, dx, dy, dz
    :returns: dict with 'pixel_data' and 'transformation'
    :raises ValueError: if no valid image file is provided
    """
    file = values['file']

    # -------------------------------------------------------------------------
    # Support App resource paths (e.g. ':CustomVolumeSection/Grayscale_8bits_palette.png')
    if file and file[0] == ':':
        resource = gom.Resource(file)
        file = BytesIO(resource.open().read())

    try:
        # Restrict allowed image formats as proposed in
        # https://github.com/ZEISS/zeiss-inspect-app-examples/security/dependabot/3
        image = Image.open(file, formats=ALLOWED_FORMATS)
    except (AttributeError, TypeError) as exc:
        raise ValueError('No valid image file provided.') from exc

    # Convert to grayscale float32
    image = image.convert('L')
    img_array = np.array(image, dtype=np.float32)
    # -------------------------------------------------------------------------

    rx = values['rx']
    ry = values['ry']
    rz = values['rz']
    dx = values['dx']
    dy = values['dy']
    dz = values['dz']

    transformation = gom.Mat4x4([
        cos(rz) * cos(ry),
        cos(rz) * sin(ry) * sin(rx) - sin(rz) * cos(rx),
        cos(rz) * sin(ry) * cos(rx) + sin(rz) * sin(rx),
        dx,
        sin(rz) * cos(ry),
        sin(rz) * sin(ry) * sin(rx) + cos(rz) * cos(rx),
        sin(rz) * sin(ry) * sin(rx) - cos(rz) * sin(rx),
        dy,
        -sin(ry),
        cos(ry) * sin(rx),
        cos(ry) * cos(rx),
        dz,
        0, 0, 0, 1
    ])

    return {
        'pixel_data': img_array,
        'transformation': transformation,
        'data': {
            'image_file': values['file']
        }
    }


@apicontribution
class ActualVolumeSection(gom.api.extensions.actuals.VolumeSection):
    """
    Custom actual volume section element.

    Features:
    - Grayscale image (JPG, PNG, GIF, TIFF) placed in 3D via a ZYX Euler rotation + translation
    - Image converted to float32 and used as pixel_data
    - Restricted image format list to prevent decompression-bomb attacks
    """

    def __init__(self):
        """Register the custom actual volume section contribution."""
        super().__init__(
            id='examples.custom_actual_volume_section',
            description='Custom Actual Volume Section'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_VolumeSection.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual volume section element."""
        return _create_volume_section(values)


gom.run_api()
