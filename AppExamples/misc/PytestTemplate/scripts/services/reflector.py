#
# reflector_pass.py
#
# ZEISS INSPECT App service example
#
# See App Development Documentation: Using services
#
# Carl Zeiss GOM Metrology GmbH, 2025
# 
# ---

import gom
from gom import apifunction

@apifunction
def reflect(value):
    gom.log.debug('Function "reflect" called')
    return value


gom.run_api()

