"""
Custom actual Volume Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray.

Mirrors the functionality of the ScriptedActualVolume example:
a 70x70x70 voxel block (dice dot pattern) padded with background,
placed via a full 4x4 transformation matrix.
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
from math import sin, cos
import numpy as np

from gom import apicontribution

# Core voxel grid size (before background padding)
CORE_SIZE = 70
# Padding added on each side with the background gray value
PADDING = 30
# Extend (half-size) of each dot marker
EXTENT = 4


def _set_voxeldata(voxels, gv, e):
    """Set the gray value of voxels forming the dot positions of a die face.

    :param voxels: np.array of shape (CORE_SIZE, CORE_SIZE, CORE_SIZE)
    :param gv: gray value to assign
    :param e: half-extent of each dot marker
    """
    # (1) front face — one dot
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[35 + x, e + y, 35 + z] = gv

    # (6) back face — six dots
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 69 - e + y, 15 + z] = gv
                voxels[15 + x, 69 - e + y, 35 + z] = gv
                voxels[15 + x, 69 - e + y, 55 + z] = gv
                voxels[55 + x, 69 - e + y, 15 + z] = gv
                voxels[55 + x, 69 - e + y, 35 + z] = gv
                voxels[55 + x, 69 - e + y, 55 + z] = gv

    # (3) top face — three dots
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 15 + y, 69 - e + z] = gv
                voxels[35 + x, 35 + y, 69 - e + z] = gv
                voxels[55 + x, 55 + y, 69 - e + z] = gv

    # (4) bottom face — four dots
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 15 + y, e + z] = gv
                voxels[15 + x, 55 + y, e + z] = gv
                voxels[55 + x, 55 + y, e + z] = gv
                voxels[55 + x, 15 + y, e + z] = gv

    # (2) left face — two dots
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[x, 15 + y, 15 + z] = gv
                voxels[x, 55 + y, 55 + z] = gv

    # (5) right face — five dots
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[69 - e + x, 15 + y, 15 + z] = gv
                voxels[69 - e + x, 15 + y, 55 + z] = gv
                voxels[69 - e + x, 55 + y, 55 + z] = gv
                voxels[69 - e + x, 55 + y, 15 + z] = gv
                voxels[69 - e + x, 35 + y, 35 + z] = gv


def _build_volume(values):
    """Build voxel array and transformation matrix from dialog values."""
    gv0 = int(values['gv_background'])
    gv1 = int(values['gv_mat1'])
    gv2 = int(values['gv_mat2'])

    # Build 70×70×70 core filled with material 1, then stamp dot markers
    voxels = np.full((CORE_SIZE, CORE_SIZE, CORE_SIZE), gv1, dtype=np.uint16)
    _set_voxeldata(voxels, gv2, EXTENT)

    # Pad with background gray value on all sides
    voxels = np.pad(voxels, PADDING, 'constant', constant_values=gv0)

    # Build 4×4 transformation matrix: rotation (rx, ry, rz) + translation (dx, dy, dz)
    rx = float(values['rx'])
    ry = float(values['ry'])
    rz = float(values['rz'])
    dx = float(values['dx'])
    dy = float(values['dy'])
    dz = float(values['dz'])

    offset = CORE_SIZE // 2 + PADDING  # = 65 (centre of the padded grid)
    transformation = gom.Mat4x4([
        cos(rz) * cos(ry),
        cos(rz) * sin(ry) * sin(rx) - sin(rz) * cos(rx),
        cos(rz) * sin(ry) * cos(rx) + sin(rz) * sin(rx),
        dx - offset,
        sin(rz) * cos(ry),
        sin(rz) * sin(ry) * sin(rx) + cos(rz) * cos(rx),
        sin(rz) * sin(ry) * sin(rx) - cos(rz) * sin(rx),
        dy - offset,
        -sin(ry), cos(ry) * sin(rx), cos(ry) * cos(rx), dz - offset,
        0, 0, 0, 1
    ])

    total_voxels = voxels.size  # (CORE_SIZE + 2*PADDING)^3
    return voxels, transformation, total_voxels


@apicontribution
class ActualVolume(gom.api.extensions.actuals.Volume):
    """
    Custom actual volume element.

    Features:
    - 70x70x70 voxel core (uint16) filled with material 1 gray value
    - Dot markers (faces 1-6 of a die) stamped with material 2 gray value
    - Core padded on all sides with background gray value to 130x130x130
    - Placed in space via a full 4x4 rotation + translation matrix
    - Stores total voxel count as custom element data token
    """

    def __init__(self):
        """Register the custom actual volume contribution."""
        super().__init__(
            id='examples.custom_actual_volume',
            description='Custom Actual Volume'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Volume.gdlg')

    def compute(self, _context, values):
        """Compute the actual volume element."""
        # -------------------------------------------------------------------------
        voxels, transformation, total_voxels = _build_volume(values)
        return {
            'voxel_data': voxels,
            'transformation': transformation,
            'data': {'num_voxels': total_voxels}
        }
        # -------------------------------------------------------------------------


gom.run_api()
