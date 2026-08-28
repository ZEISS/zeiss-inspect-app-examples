# CustomSection

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom section element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualSection` | `actuals.Section` | Circular section in the XY plane with outward normals; custom data token (num_points) |
| `NominalSection` | `nominals.Section` | Circular section in the XY plane with outward normals; custom data token (num_points) |

## Highlights

### Parameters

A section is defined by a set of 3D points with associated surface normals. Both classes accept the same dialog parameters:

| Parameter | Type | Description |
|---|---|---|
| `radius` | `float` (LENGTH) | Radius of the circular section |
| `num_points` | `int` | Number of points on the circle |

### Compute result

The `compute_stage()` method generates `num_points` evenly spaced points on a circle of the given `radius` in the XY plane (z = 0). Each point has an outward radial normal:

```python
for i in range(num_points):
    angle = 2 * math.pi * i / num_points
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    points.append((radius * cos_a, radius * sin_a, 0.0))
    normals.append((cos_a, sin_a, 0.0))  # outward radial normals
return {
    "curves": [{"points": points, "normals": normals}],
    "data": {"num_points": num_points}
}
```

### Custom data tokens

The `compute_stage()` method stores the point count as a custom element data token accessible via `elem.num_points`.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Section](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-section)
- [API — gom.api.extensions.nominals.Section](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-section)
