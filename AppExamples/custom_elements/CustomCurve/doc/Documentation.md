# CustomCurve

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom curve element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualCurve` | `actuals.Curve` | Parametric spiral curve; custom data token (num_points) |
| `NominalCurve` | `nominals.Curve` | Parametric spiral curve; custom data token (num_points) |

## Highlights

### Parameters

A curve is defined by a parametric formula evaluated at 1000 evenly spaced steps. Both classes accept the same dialog parameters (matching the [ScriptedActualCurve](../../scripted_actuals/ScriptedActualCurve/doc/Documentation.md) example):

| Parameter | Type | Description |
|---|---|---|
| `x0` | `float` (LENGTH) | X coordinate of the center |
| `y0` | `float` (LENGTH) | Y coordinate of the center |
| `z0` | `float` (LENGTH) | Z coordinate of the center |
| `radius` | `float` (LENGTH) | Base radius |
| `j` | `float` | Radial growth factor per unit t |
| `k` | `float` | Z-axis step per unit t |
| `t_min` | `float` | Start of parameter range |
| `t_max` | `float` | End of parameter range |

### Compute result

The `compute_stage()` method evaluates the parametric formula at 1000 evenly spaced steps in `[t_min, t_max)`:

```
P(t) = ( x0 + (j * t + r) * cos(t), y0 + (j * t + r) * sin(t), z0 + k * t )
```

```python
step = (t_max - t_min) / NUM_STEPS
for i in range(NUM_STEPS):
    t = t_min + i * step
    points.append((
        x0 + (j * t + r) * math.cos(t),
        y0 + (j * t + r) * math.sin(t),
        z0 + k * t
    ))
return {
    "curves": [{"points": points}],
    "data": {"num_points": len(points)}
}
```

### Custom data tokens

The `compute_stage()` method stores the point count as a custom element data token accessible via `elem.num_points` (always 1000).

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Curve](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-curve)
- [API — gom.api.extensions.nominals.Curve](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-nominals-curve)
