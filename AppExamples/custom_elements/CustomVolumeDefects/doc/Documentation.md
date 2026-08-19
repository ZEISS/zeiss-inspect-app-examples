# CustomVolumeDefects

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray**.

This App demonstrates how to create a custom actual `VolumeDefects` element using the `@apicontribution` decorator. It mirrors the functionality of the [ScriptedActualVolumeDefects](../../scripted_actuals/ScriptedActualVolumeDefects/doc/Documentation.md) example: a tetrahedral 3D volume defect mesh built from four user-supplied vertices.

| Class | Type | Features |
|---|---|---|
| `ActualVolumeDefects` | `actuals.VolumeDefects` | Tetrahedral mesh; user-defined vertices; fixed triangulation |

> [!NOTE]
> `VolumeDefects` represents 3D volumetric defects as a mesh (vertices + triangle indices). For 2D slice-based defect contours see the [CustomVolumeDefects2d](../../custom_elements/CustomVolumeDefects2d/doc/Documentation.md) example.

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `v0_x`, `v0_y`, `v0_z` | `float` (LENGTH) | Coordinates of vertex 0 |
| `v1_x`, `v1_y`, `v1_z` | `float` (LENGTH) | Coordinates of vertex 1 |
| `v2_x`, `v2_y`, `v2_z` | `float` (LENGTH) | Coordinates of vertex 2 |
| `v3_x`, `v3_y`, `v3_z` | `float` (LENGTH) | Coordinates of vertex 3 |

### Compute result

The four vertices form a tetrahedron with four triangular faces. Triangle vertex order is fixed and counter-clockwise so that surface normals point outward (inward normals make the surface invisible in the viewer):

```python
return {
    'vertices': [np.array([v0, v1, v2, v3], dtype=np.float64)],
    'triangles': [np.array([(0, 1, 2), (1, 0, 3), (0, 2, 3), (2, 1, 3)], dtype=np.int32)]
}
```

Each list entry in `vertices` / `triangles` is one connected defect mesh. Multiple separate defects can be returned by appending further arrays to each list.

### Difference from ScriptedActualVolumeDefects

The scripted version uses `dialog()` / `calculation()` functions with a live preview loop and a `context.data` user-defined token (`ude_mykey`). The custom element version uses `show_dialog()` + `compute()` without a preview event loop, keeping the code simpler and self-contained.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.VolumeDefects](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumedefects)