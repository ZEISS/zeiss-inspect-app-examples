# CustomCircle

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom circle element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualCircle` | `actuals.Circle` | Center, direction, radius; custom data tokens (center_x, center_y, center_z) |
| `NominalCircle` | `nominals.Circle` | Center, direction, radius; custom data tokens (center_x, center_y, center_z) |

## Highlights

### Parameters

Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `center_x/y/z` | `float` (LENGTH) | Center point of the circle |
| `dir_x/y/z` | `float` (dimensionless) | Normal direction of the circle plane |
| `radius` | `float` (LENGTH) | Radius of the circle |

### Custom data tokens

The `compute_stage()` method stores the input center coordinates as custom element data tokens in the `"data"` key of the return value:

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

After creation, the tokens are accessible as element attributes:

```python
elem = gom.app.project.actual_elements["Actual Circle"]
print(elem.center_x)  # → 10.0
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Circle](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-circle)
- [API — gom.api.extensions.nominals.Circle](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-circle)
