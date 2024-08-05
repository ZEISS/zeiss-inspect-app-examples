# -*- coding: utf-8 -*-

import gom
from gom import apifunction


@apifunction
def reflect(value: any) -> any:
	gom.log.debug('Function "reflect" called')
	return value


gom.run_api()
