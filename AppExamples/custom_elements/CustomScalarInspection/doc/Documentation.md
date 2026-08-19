# CustomScalarInspection — Documentation

## Overview

This example demonstrates how to build a **Custom Scalar Inspection** element using the modern `gom.api.extensions.inspections.Scalar` API, as the counterpart to the legacy [`ScriptedScalarCheck`](../../scripted_checks/ScriptedScalarCheck) example.

A scalar inspection assigns a single scalar value and a deviation to an element. This custom check reads the **diameter** of a cylindrical actual element and evaluates it against a user-supplied nominal value and optional tolerance limits.

## Key Concepts

### API

| Legacy (scripted elements) | Modern (custom elements) |
|---|---|
| `gom.script.sys.create_element_by_script(check_type='scalar', ...)` | `gom.script.customelements.create_inspection(contribution='examples.custom_scalar_inspection', ...)` |
| `gom.api.scripted_checks_util.is_scalar_checkable` | `gom.api.custom_checks_util.is_scalar_checkable` |
| Function-based script | `@apicontribution` class inheriting `gom.api.extensions.inspections.Scalar` |

### Class structure

```python
@apicontribution
class CustomScalarInspection(gom.api.extensions.inspections.Scalar):

    def __init__(self):
        super().__init__(
            id='examples.custom_scalar_inspection',
            description='Custom Scalar Inspection',
            dimension='LENGTH',   # values are in mm (base unit for LENGTH)
            abbreviation='CusSca'
        )

    def element_filter(self, element):
        return gom.api.custom_checks_util.is_scalar_checkable(element)

    def dialog(self, context, args): ...

    def apply_dialog(self, dlg, result):
        params = super().apply_dialog(dlg, result)
        params['name'] = result['name']
        params['tolerance'] = result['tolerance']   # required for tolerance support
        return params

    def compute_stage(self, context, values):
        return _compute_scalar_check(values)
```

### Compute return value

For new implementations, override `compute_stage(context, values)`.

```python
{
    'nominal': float,         # user-supplied reference value (e.g. nominal diameter in mm)
    'actual': float,          # measured value (e.g. actual diameter in mm)
    'target_element': element,# the inspected gom.Item
    'data': {
        'checked_element_name': str   # custom data token
    }
}
```

The framework derives the deviation internally as `actual − nominal` and stores the results on the created element:

| Element property | Value |
|---|---|
| `scalar_value` | `nominal` from the compute dict |
| `result_dimension` | `actual − nominal` (deviation) |
| `computation_status` | `'computed'` when successful |

### Tolerance support

Tolerance support requires two things:

1. A `tolerances` widget named **`tolerance`** in the dialog.
2. Overriding `apply_dialog()` to forward `result['tolerance']` → `params['tolerance']`.

The framework uses `params['tolerance']` to attach the tolerance to the created element.

### Element filter

`gom.api.custom_checks_util.is_scalar_checkable(element)` returns `True` for elements that support scalar inspection (e.g., inspection elements such as diameter checks, distance checks, etc.).

The filter is attached to the element selector widget *before* the dialog is shown:

```python
dlg = gom.api.dialog.create(context, '/Custom_ScalarInspection.gdlg')
dlg.checked_element.filter = self.element_filter
self.initialize_dialog(context, dlg, args)
return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))
```

### Custom data token

`checked_element_name` is stored via the `'data'` key in the compute return value and can be read as `elem.checked_element_name`.

## Use in ZEISS INSPECT

1. Import the App (ZIP) or open the folder App in edit mode.
2. The service **Custom scalar inspection** (`gom.api.examples.custom_scalar_inspection`) starts automatically.
3. In the inspection menu, select the custom scalar check command.
4. Pick a scalar-checkable inspection element (e.g., a diameter or distance check).
5. Set the check name and optional tolerance limits.
6. The check element appears in the inspection list with the computed deviation.

## Notes

- The `dimension='LENGTH'` parameter means values are interpreted in **mm** (the SI base unit for length). This is appropriate for length-based checks (diameter, distance, etc.). For angle checks, the deviation would be in radians which would be misrepresented with this dimension. Adapt the `dimension` parameter for other use cases.
- The `abbreviation='CusSca'` label distinguishes this check from the legacy `'ScrSca'` abbreviation.
- This example requires **ZEISS INSPECT 2027** or later for the `gom.api.extensions.inspections` API.

## Related references

- API: [gom.api.extensions.inspections.Scalar](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-inspections-scalar)
- How-to: [Custom inspections](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_inspections.html)
