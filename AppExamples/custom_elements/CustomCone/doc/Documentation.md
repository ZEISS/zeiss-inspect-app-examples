# CustomCone

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom cone element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualCone` | `actuals.Cone` | Two circles (point + radius each); custom data tokens (radius1, radius2) |
| `NominalCone` | `nominals.Cone` | Two circles (point + radius each); custom data tokens (radius1, radius2) |

## Highlights

### Parameters

A cone is defined by two circles. Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `p1_x/y/z` | `float` (LENGTH) | Center of circle 1 |
| `radius1` | `float` (LENGTH) | Radius of circle 1 |
| `p2_x/y/z` | `float` (LENGTH) | Center of circle 2 |
| `radius2` | `float` (LENGTH) | Radius of circle 2 |

### Custom data tokens

The `compute_stage()` method stores both radii as custom element data tokens:

```python
return {
    "point1": point1,
    "radius1": radius1,
    "point2": point2,
    "radius2": radius2,
    "data": {"radius1": radius1, "radius2": radius2}
}
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Cone](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-cone)
- [API — gom.api.extensions.nominals.Cone](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-cone)
