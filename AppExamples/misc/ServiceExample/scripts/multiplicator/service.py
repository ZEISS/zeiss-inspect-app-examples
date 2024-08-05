# -*- coding: utf-8 -*-

import gom
from gom import apifunction

@apifunction
def multiply(value1: float, value2: float) -> float:
	gom.log.debug('Function "multiply" called')
	return value1 * value2
	
gom.run_api()

