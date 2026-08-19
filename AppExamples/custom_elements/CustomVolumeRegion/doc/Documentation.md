# CustomVolumeRegion

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray** and a project containing volume data with a linked volume element (e.g. `volume_test_project`).

This App demonstrates how to create a custom actual `VolumeRegion` element using the `@apicontribution` decorator. It mirrors the functionality of the [ScriptedActualVolumeRegion](../../scripted_actuals/ScriptedActualVolumeRegion/doc/Documentation.md) example: a rectangular region of interest (ROI) extracted from a linked volume, positioned by an offset and sized by dimensions — both in mm in the voxel coordinate system.

| Class | Type | Features |
|---|---|---|
| `ActualVolumeRegion` | `actuals.VolumeRegion` | Linked volume selector with type filter; mm→voxel conversion; `ones` mask |

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `volume_ele` | element | Linked volume to extract the region from |
| `x0`, `y0`, `z0` | `float` (LENGTH) | Offset of the ROI origin in the voxel coordinate system (mm) |
| `dx`, `dy`, `dz` | `float` (LENGTH) | Dimensions of the ROI in mm (converted to voxel counts) |

### Compute result

The `compute_stage()` method divides the mm dimensions by the voxel size of the referenced volume to obtain integer voxel counts. The ROI voxel mask is a `uint8` array filled with ones:

```python
dx_vox = int(dx / volume.voxel_size.x)
dy_vox = int(dy / volume.voxel_size.y)
dz_vox = int(dz / volume.voxel_size.z)

return {
    'volume_element': volume,                               # linked volume reference
    'offset': gom.Vec3d(x0, y0, z0),                      # ROI origin (mm, voxel CS)
    'voxel_data': np.ones((dx_vox, dy_vox, dz_vox), dtype=np.uint8)
}
```

### Element selector with type filter

`VolumeRegion` requires a linked volume as input. The dialog uses `gom.api.dialog.create()` instead of `self.show_dialog()` so that a programmatic filter can be attached to the element selector widget before the dialog is displayed:

```python
def dialog(self, context, args):
    dlg = gom.api.dialog.create(context, '/Custom_VolumeRegion.gdlg')
    dlg.volume_ele.filter = self.element_filter   # restrict to linked_volume type
    self.initialize_dialog(context, dlg, args)
    return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))
```

### Difference from ScriptedActualVolumeRegion

The scripted version uses `dialog()` / `calculation()` functions with a preview loop and a `context.data` user-defined token (`ude_mykey`). The custom element version uses `gom.api.dialog` + `compute_stage()` as the primary implementation, plus a `compute()` compatibility wrapper for older runtimes, without a preview event loop.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.VolumeRegion](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumeregion)
