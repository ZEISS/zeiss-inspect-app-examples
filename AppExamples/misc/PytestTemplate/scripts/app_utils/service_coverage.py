# ---
# service_coverage.py
#
# Utility for code coverage of ZEISS INSPECT services
#
# Carl Zeiss GOM Metrology GmbH, 2025
# ---

import gom
import os
import sys
import json
from coverage import Coverage
from functools import wraps

dirname, filename = os.path.split(sys.argv[0])
filename, _ = os.path.splitext(filename)
data_file = os.path.join(dirname, ".coverage." + filename)

with gom.Resource(":metainfo.json").open() as fh:
    json_bytes = fh.read()
    metainfo = json.loads(json_bytes.decode('utf-8'))
    cov_enabled = metainfo.get('services-coverage', False)
    gom.log.debug(f"{data_file}: cov_enabled={cov_enabled}")


def coverage(func):
    """Decorator for wrapping service functions in cov.start() / cov.stop();cov.save()
    Example:
    >>> @apifunction
    >>> @coverage
    >>> def myfunc(...):
    >>>    ...

    Coverage is only measured if the App's metainfo.json contains "services-coverage": true
    or if 'cov_enabled' is set to True.
    
    The coverage data filename is generated from 'path' by prepending ".coverage." to the
    script's filename:
    /my/scripts/service.py -> /my/scripts/.coverage.service
    """
    if not cov_enabled:
        return func(*args, **kwargs)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        cov = Coverage(data_file=data_file)
        cov.start()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            cov.stop()
            cov.save()
        return result
    return wrapper

