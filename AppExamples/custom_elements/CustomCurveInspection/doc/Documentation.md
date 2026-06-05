# CustomCurveInspection — Documentation

## Overview

This example demonstrates how to build a **Custom Curve Inspection** element using the modern `gom.api.extensions.inspections.Curve` API, as the counterpart to the legacy [`ScriptedCurveCheck`](../../scripted_checks/ScriptedCurveCheck) example.

A curve inspection assigns a per-vertex deviation value to each point along a curve element. The deviations are displayed as a color-coded plot along the curve in the 3D view. This custom check computes the **y-coordinate** of each vertex as the deviation from the XZ-plane (nominal = 0).

## Key Concepts

### API

| Legacy (scripted elements) | Modern (custom elements) |
|---|---|
| `gom.script.sys.create_element_by_script(check_type='scalar_curve', ...)` | `gom.script.customelements.create_inspection(contribution='examples.custom_curve_inspection', ...)` |
| `gom.api.scripted_checks_util.is_curve_checkable` | `gom.api.custom_checks_util.is_curve_checkable` |
| Function-based script with `context.stages` iteration | `@apicontribution` class inheriting `gom.api.extensions.inspections.Curve` |

### Class structure

```python
@apicontribution
class CustomCurveInspection(gom.api.extensions.inspections.Curve):

    def __init__(self):
        super().__init__(
            id='examples.custom_curve_inspection',
            description='Custom Curve Inspection',
            dimension='LENGTH',   # values are in mm (base unit for LENGTH)
            abbreviation='CusCrv'
        )

    def element_filter(self, element):
        return gom.api.custom_checks_util.is_curve_checkable(element)

    def dialog(self, context, args): ...

    def apply_dialog(self, dlg, result):
        params = super().apply_dialog(dlg, result)
        params['name'] = result['name']
        params['tolerance'] = result['tolerance']   # required for tolerance support
        return params

    def compute_stage(self, context, values):
        return _compute_curve_check(values, context.stage)
```

### Stage handling

Unlike the legacy scripted check (which iterates `context.stages` explicitly), the modern `compute_stage()` method is called **once per stage** by the framework. The current stage index is accessed via `context.stage` and passed to the compute logic:

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

### Compute return value

```python
{
    'actual_values': [float, ...],  # per-vertex y-coordinates (deviations from y=0)
    'nominal_value': 0.0,           # single common nominal for all vertices
    'target_element': element,      # the inspected gom.Item
    'data': {
        'checked_element_name': str,  # custom data token
        'num_points': int             # number of curve vertices (custom data token)
    }
}
```

The `actual_values` list has one entry per curve vertex. Using `nominal_value` (single float) instead of `nominal_values` (array) applies the same reference to every vertex.

### Tolerance support

Tolerance support requires two things:

1. A `tolerances` widget named **`tolerance`** in the dialog.
2. Overriding `apply_dialog()` to forward `result['tolerance']` → `params['tolerance']`.

The framework uses `params['tolerance']` to attach the tolerance to the created element.

### Element filter

`gom.api.custom_checks_util.is_curve_checkable(element)` returns `True` for elements that support curve inspection — typically cross-section planes, actual curves, and surface curves.

The filter is attached to the element selector widget *before* the dialog is shown:

```python
dlg = gom.api.dialog.create(context, '/Custom_CurveInspection.gdlg')
dlg.checked_element.filter = self.element_filter
self.initialize_dialog(context, dlg, args)
return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))
```

### Custom data tokens

`checked_element_name` and `num_points` are stored via the `'data'` key in the compute return value and can be read as `elem.checked_element_name` and `elem.num_points`.

## Use in ZEISS INSPECT

1. Import the App (ZIP) or open the folder App in edit mode.
2. The service **Custom curve inspection** (`gom.api.examples.custom_curve_inspection`) starts automatically.
3. In the inspection menu, select the custom curve check command.
4. Pick a curve-checkable actual element (e.g. a cross-section plane such as `Plane X +0.00 mm`).
5. Set the check name and optional tolerance limits.
6. The check element appears in the inspection list with a per-vertex color-coded deviation plot along the curve.

## Notes

- The `dimension='LENGTH'` parameter means values are interpreted in **mm** (SI base unit for length). This is appropriate for spatial deviation checks (y-coordinate distance from zero). Adapt `dimension` for other physical quantities.
- The `abbreviation='CusCrv'` label distinguishes this check from the legacy `'ScrCrv'` abbreviation.
- This example requires **ZEISS INSPECT 2027** or later for the `gom.api.extensions.inspections` API.

## Related references

- API: [gom.api.extensions.inspections.Curve](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-inspections-curve)
- How-to: [Custom inspections](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_inspections.html)
