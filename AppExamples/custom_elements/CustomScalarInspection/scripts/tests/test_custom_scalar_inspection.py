"""
Test for CustomScalarInspection element.

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.services

from ExampleProjects.setup_project import open_project

SERVICE_ENDPOINT = 'gom.api.examples.custom_scalar_inspection'
SERVICE_TIMEOUT = 10000


def test_custom_scalar_inspection():
    """Test the custom scalar inspection element on an existing inspection result."""
    # Setup: open the standard optical test project
    open_project('zeiss_part_test_project', force_reopen=True)

    # Ensure the custom element service is running
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    # The checked element is the actual cylinder from the test project.
    # 'Cylinder 1' is a fitted cylinder with a measured diameter property.
    checked_element = gom.app.project.actual_elements['Cylinder 1']
    actual_diameter = float(checked_element.diameter)  # measured: ~4.68 mm

    # Nominal diameter from CAD (radius 2.41 mm → diameter 4.82 mm).
    # Deviation = actual − nominal ≈ 4.68 − 4.82 = −0.14 mm, which is
    # outside the ±0.1 mm tolerance → inspection fails (out of tolerance).
    nominal_diameter = 4.82   # mm
    tolerance = {'lower': -0.1, 'upper': 0.1}

    name = 'Cylinder 1.CusSca'

    # -------------------------------------------------------------------------
    # Create the custom scalar inspection element without a dialog by supplying
    # all required values programmatically.
    gom.script.customelements.create_inspection(
        contribution='examples.custom_scalar_inspection',
        name=name,
        values={'checked_element': checked_element, 'nominal': nominal_diameter},
        tolerance=tolerance
    )
    # -------------------------------------------------------------------------

    #
    # TEST
    #
    elem = gom.app.project.inspection[name]
    assert elem.computation_status == 'computed', \
        f"Expected computation_status 'computed', got '{elem.computation_status}'"

    # In the custom inspection framework:
    #   scalar_value    = nominal  (4.82 mm)
    #   result_dimension = deviation = actual − nominal  (≈ −0.137 mm)
    assert abs(float(elem.scalar_value) - nominal_diameter) < 1e-6, \
        f"Expected scalar_value {nominal_diameter}, got {elem.scalar_value}"

    expected_deviation = actual_diameter - nominal_diameter
    assert abs(float(elem.result_dimension) - expected_deviation) < 1e-6, \
        f"Expected result_dimension {expected_deviation}, got {elem.result_dimension}"

    # Custom data token: name of the element that was inspected
    assert elem.checked_element_name == checked_element.name, \
        f"Expected checked_element_name '{checked_element.name}', got '{elem.checked_element_name}'"
