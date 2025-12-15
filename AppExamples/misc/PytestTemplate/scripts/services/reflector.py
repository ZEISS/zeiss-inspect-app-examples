#
# reflector.py
#
# ZEISS INSPECT App service example
#
# See App Development Documentation: Using services
#
# The decorator @coverage is added to the basic service function definition
# to implement code coverage. The coverage data file is written to .coverage.<service_module>.
#
# See App documentation or https://coverage.readthedocs.io/en/latest/cmd.html for
# information on merging multiple coverage data files or creating coverage reports.
#
# Carl Zeiss GOM Metrology GmbH, 2025
# 
# ---

import gom                                              # pragma: no cover
from gom import apifunction                             # pragma: no cover
from app_utils.service_coverage import coverage         # pragma: no cover

@apifunction
@coverage
def reflect(value):
    gom.log.debug('Function "reflect" called')
    return value

gom.run_api()                                           # pragma: no cover
