#
# reflector_pass.py
#
# ZEISS INSPECT App service example
#
# See App Development Documentation: Using services
#
# The decorator @cover_reflect.cover is added to the basic service function definition
# to implement code coverage. The coverage data file is written to <__file__>.coverage.
#
# See App documentation or https://coverage.readthedocs.io/en/latest/cmd.html for
# information on merging multiple coverage data files or creating coverage reports.
#
# Carl Zeiss GOM Metrology GmbH, 2025
# 
# ---

import gom                                              # pragma: no cover
from gom import apifunction                             # pragma: no cover
from app_utils.service_coverage import ServiceCoverage  # pragma: no cover

cover_reflect = ServiceCoverage(__file__)               # pragma: no cover

@apifunction
@cover_reflect.cover
def reflect(value):
    gom.log.debug('Function "reflect" called')
    return value

gom.run_api()                                           # pragma: no cover
