# -*- coding: utf-8 -*-

import gom
import gom.api.math
import gom.api.test

# Call reflect function from service #2
result = gom.api.test.reflect({'test': 123})
print(result)

# Call multiply function from service #1
result = gom.api.math.multiply (23, 42)
print(result)
 


