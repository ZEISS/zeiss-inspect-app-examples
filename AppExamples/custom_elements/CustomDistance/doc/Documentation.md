# CustomDistance

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom distance element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualDistance` | `actuals.Distance` | Two points; custom data token `distance` (Euclidean distance) |
| `NominalDistance` | `nominals.Distance` | Two points; custom data token `distance` (Euclidean distance) |

## Highlights

### Parameters

Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `p1_x/y/z` | `float` (LENGTH) | First endpoint of the distance |
| `p2_x/y/z` | `float` (LENGTH) | Second endpoint of the distance |

### Custom data tokens

The `compute_stage()` method stores the Euclidean distance between the two points as a custom data token, computed directly in `compute_stage()`:

```python
import math

dx = float(values['p2_x']) - float(values['p1_x'])
dy = float(values['p2_y']) - float(values['p1_y'])
dz = float(values['p2_z']) - float(values['p1_z'])
distance = math.sqrt(dx * dx + dy * dy + dz * dz)

return {
    "point1": point1,
    "point2": point2,
    "data": {"distance": distance}
}
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Distance](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-distance)
- [API — gom.api.extensions.nominals.Distance](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-nominals-distance)
