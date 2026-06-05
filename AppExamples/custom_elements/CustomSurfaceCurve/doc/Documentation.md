# CustomSurfaceCurve

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom surface curve element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualSurfaceCurve` | `actuals.SurfaceCurve` | Sphere section curve; custom data tokens (num_points, phi_range) |
| `NominalSurfaceCurve` | `nominals.SurfaceCurve` | Sphere section curve; custom data tokens (num_points, phi_range) |

## Highlights

### Parameters

A surface curve is defined by a sphere section at a fixed elevation angle. Both classes accept the same dialog parameters (matching the [ScriptedActualSurfaceCurve](../../scripted_actuals/ScriptedActualSurfaceCurve/doc/Documentation.md) example):

| Parameter | Type | Description |
|---|---|---|
| `r` | `float` (LENGTH) | Sphere radius |
| `theta` | `float` (ANGLE) | Elevation angle (latitude), fixed for all points |
| `phi_min` | `float` (ANGLE) | Start of azimuth angle range |
| `phi_max` | `float` (ANGLE) | End of azimuth angle range |

### Compute result

The `compute_stage()` method evaluates the parametric formula at 1000 evenly spaced steps in `[phi_min, phi_max)`:

```
P(phi) = ( r * cos(theta) * cos(phi),
           r * cos(theta) * sin(phi),
           r * sin(theta) )
```

Normals equal the point coordinates (outward radial direction, not normalized), matching the behavior of the scripted element reference.

```python
step = (phi_max - phi_min) / NUM_STEPS
for i in range(NUM_STEPS):
    phi = phi_min + i * step
    p = (r_cos_theta * cos(phi), r_cos_theta * sin(phi), z)
    points.append(p)
    normals.append(p)
return {
    "curves": [{"points": points, "normals": normals}],
    "data": {"num_points": len(points), "phi_range": phi_range}
}
```

### Custom data tokens

The `compute_stage()` method stores the following as custom element data tokens:

| Token | Description |
|---|---|
| `elem.num_points` | Number of curve points (always 1000) |
| `elem.phi_range` | Azimuth range covered: `phi_max - phi_min` |

