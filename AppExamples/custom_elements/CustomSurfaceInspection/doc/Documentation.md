# CustomSurfaceInspection — Documentation

## Overview

This example demonstrates how to build a **Custom Surface Inspection** element using the modern `gom.api.extensions.inspections.Surface` API, as the counterpart to the legacy [`ScriptedSurfaceCheck`](../../scripted_checks/ScriptedSurfaceCheck) example.

A surface inspection assigns a per-vertex deviation value to each point on a mesh element. The deviations are displayed as a color-coded map on the surface in the 3D view. This custom check computes the **y-coordinate** of each mesh vertex as the deviation from the XZ-plane (nominal = 0).

## Key Concepts

### API

| Legacy (scripted elements) | Modern (custom elements) |
|---|---|
| `gom.script.sys.create_element_by_script(check_type='scalar_surface', ...)` | `gom.script.customelements.create_inspection(contribution='examples.custom_surface_inspection', ...)` |
| `gom.api.scripted_checks_util.is_surface_checkable` | `gom.api.custom_checks_util.is_surface_checkable` |
| Function-based script with `context.stages` iteration | `@apicontribution` class inheriting `gom.api.extensions.inspections.Surface` |

### Class structure

```python
@apicontribution
class CustomSurfaceInspection(gom.api.extensions.inspections.Surface):

    def __init__(self):
        super().__init__(
            id='examples.custom_surface_inspection',
            description='Custom Surface Inspection',
            dimension='LENGTH',   # values are in mm (base unit for LENGTH)
            abbreviation='CusSrf'
        )

    def element_filter(self, element):
        return gom.api.custom_checks_util.is_surface_checkable(element)

    def dialog(self, context, args): ...

    def apply_dialog(self, dlg, result):
        params = super().apply_dialog(dlg, result)
        params['name'] = result['name']
        params['tolerance'] = result['tolerance']   # required for tolerance support
        return params

    def compute_stage(self, context, values):
        return _compute_surface_check(values, context.stage)
```

### Compute return value

```python
{
    'deviation_values': [float, ...],  # per-vertex y-coordinates (deviations from y=0)
    'nominal': 0.0,                    # single nominal for all vertices
    'target_element': element,         # the inspected gom.Item
    'data': {
        'checked_element_name': str,   # custom data token
        'num_points': int              # number of mesh vertices (custom data token)
    }
}
```

The `deviation_values` list has one entry per surface point. The `nominal` value is used as the common reference for all points.

### Stage handling

The modern `compute_stage()` method is called **once per stage** by the framework. The current stage index is accessed via `context.stage`:

```python
# Legacy pattern (scripted check):
for s in context.stages:
    vertices = np.array(element.data.coordinate[s])
    context.result[s] = {...}

# Modern pattern (custom element):
def compute_stage(self, context, values):
    vertices = np.array(element.data.coordinate)[context.stage]
    return {...}
```

### Tolerance support

Tolerance support requires two things:

1. A `tolerances` widget named **`tolerance`** in the dialog.
2. Overriding `apply_dialog()` to forward `result['tolerance']` → `params['tolerance']`.

The framework uses `params['tolerance']` to attach the tolerance to the created element.

### Element filter

`gom.api.custom_checks_util.is_surface_checkable(element)` returns `True` for elements that support surface inspection — typically actual mesh elements (e.g. `gom.app.project.parts['Training Object'].actual`).

The filter is attached to the element selector widget *before* the dialog is shown:

```python
dlg = gom.api.dialog.create(context, '/Custom_SurfaceInspection.gdlg')
dlg.checked_element.filter = self.element_filter
self.initialize_dialog(context, dlg, args)
return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))
```

### Custom data tokens

`checked_element_name` and `num_points` are stored via the `'data'` key in the compute return value and can be read as `elem.checked_element_name` and `elem.num_points`.

## Use in ZEISS INSPECT

1. Import the App (ZIP) or open the folder App in edit mode.
2. The service **Custom surface inspection** (`gom.api.examples.custom_surface_inspection`) starts automatically.
3. In the inspection menu, select the custom surface check command.
4. Pick a surface-checkable actual element (e.g. the part mesh).
5. Set the check name and optional tolerance limits.
6. The check element appears in the inspection list with a per-vertex color-coded deviation map on the surface.

## Notes

- The `dimension='LENGTH'` parameter means values are interpreted in **mm**. Adapt `dimension` for other physical quantities.
- The `abbreviation='CusSrf'` label distinguishes this check from the legacy `'ScrSrf'` abbreviation.
- This example requires **ZEISS INSPECT 2027** or later for the `gom.api.extensions.inspections` API.

## Related references

- API: [gom.api.extensions.inspections.Surface](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-inspections-surface)
- How-to: [Custom inspections](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_inspections.html)
