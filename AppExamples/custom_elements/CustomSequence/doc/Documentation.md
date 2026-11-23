# CustomSequence

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create a custom `sequence.CustomSequence` element using the `@apicontribution` decorator. It creates a datum plane from three user-defined reference points and keeps the sequence synchronized when individual child elements are edited.

| Class | Type | Features |
|---|---|---|
| `DatumPlaneSequence` | `sequence.CustomSequence` | Datum plane from 3 points; child elements editable separately |

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `p1_x`, `p1_y`, `p1_z` | `float` (LENGTH) | Coordinates of reference point 1 |
| `p2_x`, `p2_y`, `p2_z` | `float` (LENGTH) | Coordinates of reference point 2 |
| `p3_x`, `p3_y`, `p3_z` | `float` (LENGTH) | Coordinates of reference point 3 |

### Sequence structure

The sequence contains one leading element and three child elements:

* Leading element: Datum plane (created by 3 points)
* Child 1: Reference Point 1
* Child 2: Reference Point 2
* Child 3: Reference Point 3

When `edit_child_elements_separately` is enabled, users can edit each point directly. The `on_edited()` callback writes updated point coordinates back to sequence arguments so the sequence dialog always reflects current values.

### Validation behavior

The dialog validates the three points in a handler attached to the dialog for the duration of that call. Collinear or identical points show a message in the dialog and disable **OK**. Direct script creation bypasses this dialog validation; the native plane-creation command then raises an error because the points do not define a plane. Editing the points recomputes the plane through its existing point references.

### Create result

The `create()` method returns the three reference points first and the datum plane last, with the plane marked as the leading element:

```python
return {'elements': [POINT_1, POINT_2, POINT_3, PLANE], 'leading': PLANE}
```

This ordering is important because `on_edited()` receives updated creation parameters in the same element order.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.sequence.CustomSequence](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-sequence-customsequence)