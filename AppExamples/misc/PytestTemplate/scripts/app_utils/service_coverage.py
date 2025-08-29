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

cov = Coverage(data_file=data_file)

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

def contribution_coverage(cls):
    """Class decorator for decorating all user-defined methods of an API contribution with @coverage
    Example:
    >>> @apicontribution
    >>> @contribution_coverage # decorate __init__(), dialog() and compute() with @coverage
    >>> class MyGeometry (gom.api.extensions.actuals.Circle):
    >>>     def __init__ (self):
    >>>         super ().__init__ (id='template_app.scripted_actual_circle', description='Scripted Circle'
    >>>
    >>>     def dialog (self, context, args):
    >>>         return self.show_dialog (context, args, 'Scripted_Circle.gdlg')
    >>>
    >>>     def compute (self, context, values):
    >>>         return generate_circle_element(
    >>>             center=[values['center_x'], values['center_y'], values['center_z']],
    >>>             radius=values['radius'],
    >>>             direction=[values['dir_x'], values['dir_y'], values['dir_z']]
    >>>            )
    """
    class_name = cls.__name__
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and (not attr_name.startswith("__") or attr_name == "__init__"):
            # Decorate only native methods of this class,
            # not those added by @apicontribution
            if attr.__qualname__.startswith(class_name + "."):
                setattr(cls, attr_name, coverage(attr))
    return cls
