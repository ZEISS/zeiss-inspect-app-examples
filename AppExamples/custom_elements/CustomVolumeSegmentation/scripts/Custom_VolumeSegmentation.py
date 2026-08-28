"""
Custom actual VolumeSegmentation Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray and a project with volume data
      and a linked volume element.

Mirrors the functionality of the ScriptedActualVolumeSegmentation example:
voxels of a linked volume are classified into three segments (0 = background,
1 = material 1, 2 = material 2) using two user-supplied grayscale thresholds.
"""

import gom
import gom.api.dialog
import gom.api.extensions
import gom.api.extensions.actuals
import numpy as np

from gom import apicontribution


def _create_volume_segmentation(values):
    """
    Segment the voxel data of a linked volume into three material classes.

    Voxels are classified using two grayscale thresholds:
    - label 0 (background): voxel value <= gv_mat1
    - label 1 (material 1): gv_mat1 < voxel value <= gv_mat2
    - label 2 (material 2): voxel value > gv_mat2

    Custom data tokens expose the per-label voxel counts so the user can
    assess material fractions without additional scripting.

    :param values: dict with keys selected_element, gv_mat1, gv_mat2
    :returns: dict with 'segmentation_labels', 'number_of_segments',
              'volume_element', and 'data' containing voxel counts
    :raises ValueError: if no volume element is selected
    """
    if values['selected_element'] is None:
        raise ValueError('No volume element selected.')

    # -------------------------------------------------------------------------
    original_array = np.array(values['selected_element'].linked_volume.data.voxel_data)
    segmentation_array = original_array.copy()

    segmentation_array = np.where(
        segmentation_array > values['gv_mat2'], 2,
        np.where(segmentation_array > values['gv_mat1'], 1, 0)
    )
    segmentation_array = segmentation_array.astype(np.uint8)

    # Count voxels in each segment for the custom data tokens
    labels = segmentation_array[0]
    voxel_count_0 = int(np.sum(labels == 0))
    voxel_count_1 = int(np.sum(labels == 1))
    voxel_count_2 = int(np.sum(labels == 2))
    # -------------------------------------------------------------------------

    return {
        'segmentation_labels': labels,
        'number_of_segments': 3,
        'volume_element': values['selected_element'],
        'data': {
            'voxel_count_0': voxel_count_0,
            'voxel_count_1': voxel_count_1,
            'voxel_count_2': voxel_count_2
        }
    }


@apicontribution
class ActualVolumeSegmentation(gom.api.extensions.actuals.VolumeSegmentation):
    """
    Custom actual volume segmentation element.

    Features:
    - Classifies voxels into three segments using two grayscale thresholds
    - Element selector with type filter restricting selection to linked volumes
    - Data tokens: voxel_count_0, voxel_count_1, voxel_count_2
    """

    def __init__(self):
        """Register the custom actual volume segmentation contribution."""
        super().__init__(
            id='examples.custom_actual_volume_segmentation',
            description='Custom Actual Volume Segmentation'
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
        dlg = gom.api.dialog.create(context, '/Custom_VolumeSegmentation.gdlg')
        dlg.selected_element.filter = self.element_filter
        self.initialize_dialog(context, dlg, args)
        return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))

    def compute(self, _context, values):
        """Compute the actual volume segmentation element."""
        return _create_volume_segmentation(values)


gom.run_api()
