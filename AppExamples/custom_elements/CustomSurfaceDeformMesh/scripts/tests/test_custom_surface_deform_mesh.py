"""Integration test for the custom surface deformation element."""

import gom
import gom.api.services
import numpy as np

from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_surface_deform_mesh'
SERVICE_TIMEOUT = 10000


def test_actual_surface_deform_mesh():
    """Create a deformed actual surface from the example project mesh."""
    open_project('zeiss_part_test_project', force_reopen=True)

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if service.get_status() != 'RUNNING':
        assert service.start_and_wait(timeout=SERVICE_TIMEOUT)

    source = gom.app.project.parts['Training Object'].actual
    name = 'Deformed Mesh'
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_surface_deform_mesh',
        name=name,
        values={'selected_element': source, 'deformation_value': 0.2}
    )

    result = gom.app.project.actual_elements[name]
    coordinates = np.array(result.data.coordinate)
    triangles = np.array(result.data.triangle)
    assert coordinates.size > 0
    assert triangles.size > 0
    assert triangles.min() >= 0
    assert triangles.max() < coordinates.shape[-2]
