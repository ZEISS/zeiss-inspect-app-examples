# CustomProbeMeasuredCurve

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create a custom probe measured curve element contribution using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualProbeMeasuredCurve` | `actuals.ProbeMeasuredCurve` | Helical probe path on a cylinder; per-point probe radii; custom data tokens (num_points, helix_pitch) |

> [!NOTE]
> `ProbeMeasuredCurve` only exists as an actual element type — there is no nominal probe measured curve in the API.

## Highlights

### Parameters

The element simulates a CMM tactile probe tracing a helical groove on a cylinder surface — a realistic task when measuring screw threads or helical features.

| Parameter | Type | Description |
|---|---|---|
| `cylinder_radius` | `float` (LENGTH) | Radius of the cylinder being measured |
| `height` | `float` (LENGTH) | Height of the helical path |
| `n_turns` | `float` (NO_UNIT) | Number of helical turns (may be fractional, e.g. 3.5) |
| `probe_radius` | `float` (LENGTH) | Radius of the probe tip (e.g. 1.5 mm ruby sphere) |

### Compute result

The `compute_stage()` method evaluates the helix at 500 evenly spaced parameter values `t ∈ [0, 1]`:

```
P(t) = ( R·cos(2π·n·t),  R·sin(2π·n·t),  H·t )
```

Each point carries the uniform probe tip radius. The helix pitch (axial advance per turn) is stored as a custom data token.

```python
for i in range(NUM_POINTS):
    t = i / (NUM_POINTS - 1)
    angle = 2.0 * math.pi * n_turns * t
    points.append((R * cos(angle), R * sin(angle), H * t))
    radii.append(probe_radius)
return {
    "curves": [{"points": points, "radii": radii}],
    "data": {"num_points": NUM_POINTS, "helix_pitch": H / n}
}
```

### Custom data tokens

The `compute_stage()` method stores the following as custom element data tokens:

| Token | Description |
|---|---|
| `elem.num_points` | Number of probe-contact points (always 500) |
| `elem.helix_pitch` | Axial pitch of the helix: `height / n_turns` |

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.ProbeMeasuredCurve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-probemeasuredcurve)
