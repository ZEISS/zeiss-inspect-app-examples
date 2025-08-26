# ---
# service_coverage.py
#
# Utility for code coverage of ZEISS INSPECT services
#
# Carl Zeiss GOM Metrology GmbH, 2025
# ---

import gom
import os
import json
from coverage import Coverage
from functools import wraps

class ServiceCoverage:
    """Measure code coverage of service functions."""
    cov_enabled = False

    def __init__(self, path):
        """Decorator for wrapping service functions in cov.start() / cov.stop();cov.save()
        Example:
        >>> cover_myfunc = ServiceCoverage(__file__)           # pragma: no cover
        >>> 
        >>> @apifunction
        >>> @cover_myfunc.cover
        >>> def myfunc(...):
        >>>    ...

        Coverage is only measured if the App's metainfo.json contains "services-coverage": true
        or if 'cov_enabled' is set to True.
        
        The coverage data filename is generated from 'path' by prepending ".coverage." to the
        script's filename:
        /my/scripts/service.py -> /my/scripts/.coverage.service.py

        Args:
            path (str): Path of covered Python file.
        """
        with gom.Resource(":metainfo.json").open() as fh:
            json_bytes = fh.read()
            metainfo = json.loads(json_bytes.decode('utf-8'))
            self.cov_enabled = metainfo.get('services-coverage', False)
            gom.log.debug(f"{path}: cov_enabled={self.cov_enabled}")

        if self.cov_enabled:
            dirname, filename = os.path.split(path)
            self.cov = Coverage(data_file=os.path.join(dirname, ".coverage." + filename))

    def cover(self, func):
        if not self.cov_enabled:
            return func

        @wraps(func)
        def wrapper(*args, **kwargs):
            self.cov.start()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                raise e
            finally:
                self.cov.stop()
                self.cov.save()

            return result
        return wrapper
