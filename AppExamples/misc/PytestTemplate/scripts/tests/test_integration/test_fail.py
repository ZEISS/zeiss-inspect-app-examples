""" Dummy test which always fails

Carl Zeiss GOM Metrology GmbH, 2026
"""

import gom
import pytest

@pytest.mark.xfail(reason="Intentional failure test")
def test_fail():
    """This test has no unit-under-test and always fails"""
    assert False
