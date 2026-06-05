# CustomVolumeDefects2d

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray**.

This App demonstrates how to create a custom actual `VolumeDefects2d` element using the `@apicontribution` decorator. It generates circular defect contours on a single CT slice (all curves coplanar) to illustrate the `curves`-based compute format.

> [!NOTE]
> `VolumeDefects2d` is distinct from `VolumeDefects`: `VolumeDefects2d` represents 2D contours found on individual CT slices (pore outlines), while `VolumeDefects` represents 3D volumetric defects defined by a mesh (vertices + triangles). There is no corresponding Scripted Element example for `VolumeDefects2d`.

| Class | Type | Features |
|---|---|---|
| `ActualVolumeDefects2d` | `actuals.VolumeDefects2d` | Circular slice contours; parametric count/radius/spacing; custom data tokens |

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `n_defects` | `int` | Number of defect contours to generate |
| `defect_radius` | `float` (LENGTH) | Radius of each circular defect contour |
| `z_pos` | `float` (LENGTH) | Z coordinate of the CT slice (shared by all contours) |
| `xy_spacing` | `float` (LENGTH) | X spacing between defect-circle centers |
| `n_points` | `int` | Number of points discretising each circular contour |

### Compute result

Each contour is a circle in the XY-plane at Z = `z_pos`, with centres distributed along X:

```
P(j) = ( defect_radius * cos(2π·j/n_points),
          defect_radius * sin(2π·j/n_points),
          z_pos )
```

The `curves`-only format is used:

```python
return {
    'curves': [[(x, y, z), ...], ...],   # one list per defect slice
    'data': {
        'num_defects': n_defects,
        'total_points': n_defects * n_points
    }
}
```

### Extended format (optional, not used in this example)

The API also supports optional outer contours and per-vertex normals:

```python
{
    'curves': [...],                   # inner defect contours
    'outer_contours': [...],           # optional outer hull contours
    'curves_normals': [...],           # optional normals for curves
    'outer_contours_normals': [...],   # optional normals for outer_contours
    'data': {...}
}
```

When normals are provided, the first contour of a defect must point outward and subsequent internal contours must alternate orientation (starting inward). Each normals list must match the structure and vertex count of its corresponding contour list. When normals are omitted, they are derived automatically.

### Custom data tokens

| Token | Description |
|---|---|
| `elem.num_defects` | Number of defect contours |
| `elem.total_points` | Total point count across all contours (`n_defects × n_points`) |

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.VolumeDefects2d](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-volumedefects2d)
