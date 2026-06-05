"""
Custom actual VolumeRegion Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray and a project with volume data
      and a linked volume element.

Mirrors the functionality of the ScriptedActualVolumeRegion example:
a rectangular region of interest (ROI) extracted from a linked volume,
defined by an offset (in mm, voxel coordinate system) and voxel dimensions.
"""

import gom
import gom.api.dialog
import gom.api.extensions
import gom.api.extensions.actuals
import numpy as np

from gom import apicontribution


def _create_volume_region(values):
    """
    Build the volume region voxel mask from the dialog parameters.

    The offset (x0, y0, z0) is given in mm in the voxel coordinate system.
    The dimensions (dx, dy, dz) are given in mm and converted to voxel counts
    using the voxel size of the referenced linked volume.

    :param values: dict with keys volume_ele, x0, y0, z0, dx, dy, dz
    :returns: dict with 'volume_element', 'offset', and 'voxel_data'
    :raises ValueError: if no volume element is selected
    """
    if values['volume_ele'] is None:
        raise ValueError('No volume element selected.')

    volume = values['volume_ele']
    x0 = values['x0']
    y0 = values['y0']
    z0 = values['z0']

    # -------------------------------------------------------------------------
    # Convert mm dimensions to voxel counts using the volume's voxel size
    dx = int(values['dx'] / volume.voxel_size.x)
    dy = int(values['dy'] / volume.voxel_size.y)
    dz = int(values['dz'] / volume.voxel_size.z)

    return {
        'volume_element': volume,
        'offset': gom.Vec3d(x0, y0, z0),
        'voxel_data': np.ones((dx, dy, dz), dtype=np.uint8),
        'data': {
            'num_voxels': dx * dy * dz
        }
    }
    # -------------------------------------------------------------------------


@apicontribution
class ActualVolumeRegion(gom.api.extensions.actuals.VolumeRegion):
    """
    Custom actual volume region element.

    Features:
    - Rectangular region of interest extracted from a linked volume
    - Offset in mm (voxel coordinate system) via x0, y0, z0
    - Dimensions in mm converted to voxel counts via dx, dy, dz
    - Element selector with type filter restricting selection to linked volumes
    """

    def __init__(self):
        """Register the custom actual volume region contribution."""
        super().__init__(
            id='examples.custom_actual_volume_region',
            description='Custom Actual Volume Region'
        )

    def element_filter(self, element):
        """Accept only linked volume elements in the element selector."""
        try:
            if element.type == 'linked_volume':
                return True
        except (AttributeError, TypeError):
            pass
        return False

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        # Use gom.api.dialog directly to attach the element filter before showing
        dlg = gom.api.dialog.create(context, '/Custom_VolumeRegion.gdlg')
        dlg.volume_ele.filter = self.element_filter
        self.initialize_dialog(context, dlg, args)
        return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))

    def compute_stage(self, _context, values):
        """Compute the actual volume region element."""
        return _create_volume_region(values)


gom.run_api()
