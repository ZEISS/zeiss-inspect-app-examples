# CustomCylinder

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom cylinder element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualCylinder` | `actuals.Cylinder` | Center point, direction, radius; custom data tokens (center_x, center_y, center_z) |
| `NominalCylinder` | `nominals.Cylinder` | Center point, direction, radius; custom data tokens (center_x, center_y, center_z) |

## Highlights

### Parameters

Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `center_x/y/z` | `float` (LENGTH) | Center point of the cylinder |
| `dir_x/y/z` | `float` (dimensionless) | Direction of the cylinder axis |
| `radius` | `float` (LENGTH) | Radius of the cylinder |

### Custom data tokens

The `compute_stage()` method stores the center point coordinates as custom element data tokens:

```python
return {
    "center": center,
    "direction": direction,
    "radius": radius,
    "data": {
        "center_x": float(values['center_x']),
        "center_y": float(values['center_y']),
        "center_z": float(values['center_z'])
    }
}
```
## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Cylinder](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-cylinder)
- [API — gom.api.extensions.nominals.Cylinder](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-cylinder)
