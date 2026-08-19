# CustomPointCloud

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom point cloud element contributions, one actual and one nominal, using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualPointCloud` | `actuals.PointCloud` | Toroid point cloud; explicit normals; custom data tokens (`num_points`, `u_range`) |
| `NominalPointCloud` | `nominals.PointCloud` | Toroid point cloud; explicit normals; custom data tokens (`num_points`, `u_range`) |

## Highlights

### Parameters

Both classes use the same dialog parameters to sample a toroid surface:

| Parameter | Type | Description |
|---|---|---|
| `R` | `float` (LENGTH) | Major radius of the toroid |
| `r` | `float` (LENGTH) | Minor radius of the toroid |
| `u_min`, `u_max` | `float` (ANGLE) | Start and end values for parameter `u` |
| `u_steps` | `int` | Number of sampling steps in `u` direction |
| `v_min`, `v_max` | `float` (ANGLE) | Start and end values for parameter `v` |
| `v_steps` | `int` | Number of sampling steps in `v` direction |

The dialog also shows the parametric surface formula used by the implementation:

```text
P(u,v) = ((R+r*cos(v*pi))*cos(u*pi), (R+r*cos(v*pi))*sin(u*pi), r*sin(v*pi))
```

### Compute result

The shared `_compute_point_cloud()` helper samples the toroid on a regular `u`/`v` grid, computes one 3D point and one outward normal per sample, and returns the generated data for both contributions:

```python
return {
    "points": points,
    "normals": normals,
    "data": {
        "num_points": num_points,
        "u_range": u_range,
    }
}
```

The number of generated points equals `u_steps * v_steps`.

### Custom data tokens

The compute result stores two custom element data tokens:

| Token | Meaning |
|---|---|
| `num_points` | Total number of sampled point-cloud points |
| `u_range` | Covered range in the `u` parameter direction (`u_max - u_min`) |

These values are available on created elements as `elem.num_points` and `elem.u_range`.

## Related references

- API: [gom.api.extensions.actuals.PointCloud](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-pointcloud)
- API: [gom.api.extensions.nominals.PointCloud](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-pointcloud)
- How-to: [Custom nominals and actuals](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)