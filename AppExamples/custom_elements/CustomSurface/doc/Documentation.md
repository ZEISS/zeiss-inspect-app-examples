# CustomSurface

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom surface element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualSurface` | `actuals.Surface` | Cuboid mesh from 8 vertices; custom data token (num_vertices) |
| `NominalSurface` | `nominals.Surface` | Cuboid mesh from 8 vertices; custom data token (num_vertices) |

## Highlights

### Parameters

A surface element is defined by 8 corner vertices. Both classes accept the same dialog parameters (matching the [ScriptedActualSurface](../../scripted_actuals/ScriptedActualSurface/doc/Documentation.md) example):

| Parameter | Type | Description |
|---|---|---|
| `v0_x` … `v7_x` | `float` (LENGTH) | X coordinate of each corner vertex |
| `v0_y` … `v7_y` | `float` (LENGTH) | Y coordinate of each corner vertex |
| `v0_z` … `v7_z` | `float` (LENGTH) | Z coordinate of each corner vertex |

### Compute result

The `compute_stage()` method assembles a cuboid mesh from the 8 corner vertices using 12 fixed triangles (2 per face):

```python
CUBOID_TRIANGLES = [
    (0,1,2),(0,2,3),  # front  (x+)
    (1,5,6),(1,6,2),  # right  (y+)
    (3,2,6),(3,6,7),  # top    (z+)
    (0,1,5),(0,5,4),  # bottom (z-)
    (4,5,6),(4,6,7),  # back   (x-)
    (0,4,7),(0,7,3),  # left   (y-)
]
return {
    "vertices": vertices,
    "triangles": CUBOID_TRIANGLES,
    "data": {"num_vertices": len(vertices)}
}
```

### Custom data tokens

The `compute_stage()` method stores the vertex count as a custom element data token accessible via `elem.num_vertices` (always 8).

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — Extensions API - gom.api.extensions.actuals.CustomSurface](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-surface)
- [API — Extensions API - gom.api.extensions.nominals.CustomSurface](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-surface)