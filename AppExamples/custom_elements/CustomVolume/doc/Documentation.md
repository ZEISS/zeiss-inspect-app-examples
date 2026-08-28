# CustomVolume

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray**.

This App demonstrates how to create a custom actual volume element from artificial voxel data using the `@apicontribution` decorator. It mirrors the functionality of the [ScriptedActualVolume](../../../scripted_actuals/ScriptedActualVolume/doc/Documentation.md) example.

| Class | Type | Features |
|---|---|---|
| `ActualVolume` | `actuals.Volume` | Dice-pattern voxel block; Mat4x4 placement; custom data token (num_voxels) |

> [!NOTE]
> `Volume` only exists as an actual element type — there is no nominal volume in the API.

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `gv_background` | `int` (0–65535) | Gray value of the background padding |
| `gv_mat1` | `int` (0–65535) | Gray value of the main material (fills the 70×70×70 core) |
| `gv_mat2` | `int` (0–65535) | Gray value of the dot markers (die-face pattern) |
| `dx`, `dy`, `dz` | `float` (LENGTH) | Translation of the volume origin |
| `rx`, `ry`, `rz` | `float` (ANGLE) | Rotation angles (applied as ZYX Euler) |

### Compute result

The `compute_stage()` method builds a 130×130×130 `uint16` NumPy array and a full `gom.Mat4x4` transformation:

1. A 70×70×70 core is filled with `gv_mat1`.
2. Dot-marker voxels (positions matching the six faces of a standard die) are overwritten with `gv_mat2`.
3. The core is padded by 30 voxels on every side with `gv_background`, yielding 130×130×130.
4. A 4×4 rotation + translation matrix is built from `rx`, `ry`, `rz`, `dx`, `dy`, `dz`.

```python
return {
    'voxel_data': voxels,          # np.array shape (130,130,130), dtype=uint16
    'transformation': transformation,  # gom.Mat4x4
    'data': {'num_voxels': 130**3}
}
```

### Custom data tokens

| Token | Description |
|---|---|
| `elem.num_voxels` | Total voxel count of the padded volume (130³ = 2 197 000) |

### Difference from ScriptedActualVolume

The scripted version uses `dialog()` / `calculation()` functions with a live preview and a "Random rotation" checkbox (dialog event handler). The custom element version uses `show_dialog()` + `compute_stage()` without a preview event loop, keeping the code simpler and self-contained.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.Volume](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volume)