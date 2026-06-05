"""
Test for custom volume segmentation element
"""

import gom
import gom.api.services
import numpy as np

from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume_segmentation'
SERVICE_TIMEOUT = 10000


def test_actual_volume_segmentation():
    """Test custom actual volume segmentation element."""
    open_project('volume_test_project', force_reopen=True)

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    # -------------------------------------------------------------------------
    # Find segmentation thresholds from the volume's own data:
    # - gv_mat1: Otsu threshold — natural valley between background and material
    # - gv_mat2: 90th percentile of material voxels — marks the densest 10%
    # This avoids arbitrary cuts through the main material peak (noise) and
    # works correctly regardless of the project's actual grayscale range.
    linked_vol = gom.app.project.actual_elements['Linked volume 1']
    vol_data = np.array(linked_vol.linked_volume.data.voxel_data).ravel()

    hist, bin_edges = np.histogram(vol_data, bins=256)
    hist_norm = hist.astype(float) / hist.sum()
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    cum_hist = np.cumsum(hist_norm)
    cum_mean = np.cumsum(hist_norm * bin_centers)
    total_mean = cum_mean[-1]
    w1 = cum_hist
    w2 = 1.0 - cum_hist
    m1 = np.where(w1 > 0, cum_mean / w1, 0.0)
    m2 = np.where(w2 > 0, (total_mean - cum_mean) / w2, 0.0)
    gv_mat1 = int(bin_edges[np.argmax(w1 * w2 * (m1 - m2) ** 2) + 1])
    material_voxels = vol_data[vol_data > gv_mat1]
    gv_mat2 = int(np.percentile(material_voxels, 90)) if len(material_voxels) else gv_mat1 + 5000
    # -------------------------------------------------------------------------

    name = "Actual Volume Segmentation"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume_segmentation',
        name=name,
        values={
            'selected_element': linked_vol,
            'gv_mat1': gv_mat1,
            'gv_mat2': gv_mat2
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]

    # Custom data tokens: per-label voxel counts
    assert elem.voxel_count_0 >= 0
    assert elem.voxel_count_1 >= 0
    assert elem.voxel_count_2 >= 0
    # The three labels partition every voxel, so their sum must be positive
    assert elem.voxel_count_0 + elem.voxel_count_1 + elem.voxel_count_2 > 0
