"""
Test for CustomSurfaceInspection element.

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.services

from addon import ElementTest
from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_surface_inspection'
SERVICE_TIMEOUT = 10000


def test_custom_surface_inspection():
    """Test the custom surface inspection element on the training object mesh."""
    # Setup: open the standard optical test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Ensure the custom element service is running
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    # The training object mesh is surface-checkable and has enough vertices to
    # produce a meaningful per-vertex y-deviation map.
    checked_element = gom.app.project.parts['Training Object'].actual
    tolerance = {'lower': -10.0, 'upper': 10.0}
    name = 'Zeiss training object (extracted) 1.red Material 1.CusSrf'

    # -------------------------------------------------------------------------
    # Create the custom surface inspection element without a dialog by supplying
    # all required values programmatically.
    gom.script.customelements.create_inspection(
        contribution='examples.custom_surface_inspection',
        name=name,
        values={'checked_element': checked_element},
        tolerance=tolerance
    )
    # -------------------------------------------------------------------------

    #
    # TEST
    #
    elem = gom.app.project.inspection[name]

    # -------------------------------------------------------------------------
    # Compare element properties against reference data.
    # On the first run the .dat file is generated; subsequent runs compare
    # against it. This mirrors the ScriptedSurfaceCheck test pattern.
    element_test = ElementTest('custom_surface_inspection.dat')
    element_test.testElementValues(
        elem,
        ['scalar_value', 'computation_status',
         'result_dimension.measured_value', 'result_dimension.deviation'])
    element_test.callTest()
    # -------------------------------------------------------------------------

    assert elem.computation_status == 'computed', \
        f"Expected computation_status 'computed', got '{elem.computation_status}'"

    assert elem.checked_element_name == checked_element.name, \
        f"Expected checked_element_name '{checked_element.name}', got '{elem.checked_element_name}'"

    assert elem.num_points > 0, \
        f"Expected num_points > 0, got {elem.num_points}"
