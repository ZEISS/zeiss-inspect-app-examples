""" Group of unit tests

This test group can be run without ZEISS INSPECT.

Carl Zeiss GOM Metrology GmbH, 2025
"""

# Import unit-under-test (UUT)
# Note: This UUT imports gom (which is not provided in the unit test environment),
#       but the test runner provides a mock gom module as substitute.
import uut_project_keywords

def test_pass():
    """Unit test for a function in the UUT
    """
    rv = uut_project_keywords.covered_by_unittest(42)
    assert rv == 42
