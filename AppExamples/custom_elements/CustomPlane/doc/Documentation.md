# CustomPlane

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom plane element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualPlane` | `actuals.Plane` | Normal vector + point on plane; custom data tokens (normal_x, normal_y, normal_z) |
| `NominalPlane` | `nominals.Plane` | Normal vector + point on plane; custom data tokens (normal_x, normal_y, normal_z) |

## Highlights

### Parameters

Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `normal_x/y/z` | `float` (dimensionless) | Normal direction of the plane |
| `point_x/y/z` | `float` (LENGTH) | A point lying on the plane |

### Custom data tokens

The `compute_stage()` method stores the normal vector components as custom element data tokens:

```python
return {
    "normal": normal,
    "point": point,
    "data": {"normal_x": nx, "normal_y": ny, "normal_z": nz}
}
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Plane](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-plane)
- [API — gom.api.extensions.nominals.Plane](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-nominals-plane)
