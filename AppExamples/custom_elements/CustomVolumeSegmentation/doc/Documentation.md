# CustomVolumeSegmentation

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray** and a project containing volume data with a linked volume element (e.g. `volume_test_project`).

This App demonstrates how to create a custom actual `VolumeSegmentation` element using the `@apicontribution` decorator. It mirrors the functionality of the [ScriptedActualVolumeSegmentation](../../../scripted_actuals/ScriptedActualVolumeSegmentation/doc/Documentation.md) example: the voxel data of a linked volume is classified into three material segments (background, material 1, material 2) using two user-supplied grayscale thresholds.

| Class | Type | Features |
|---|---|---|
| `ActualVolumeSegmentation` | `actuals.VolumeSegmentation` | Linked volume selector with type filter; two-threshold classification; per-label voxel counts |

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `selected_element` | element | Linked volume to segment |
| `gv_mat1` | `int` (NO_UNIT, 0–255) | Upper grayscale boundary for background; voxels above are label 1 |
| `gv_mat2` | `int` (NO_UNIT, 0–255) | Upper grayscale boundary for material 1; voxels above are label 2 |

### Compute result

The `compute_stage()` method reads the voxel data from the linked volume, classifies it by threshold comparison, and returns a `uint8` label array:

```python
segmentation_array = np.where(
    original_array > gv_mat2, 2,
    np.where(original_array > gv_mat1, 1, 0)
).astype(np.uint8)

return {
    'segmentation_labels': segmentation_array[0],  # label array
    'number_of_segments': 3,
    'volume_element': values['selected_element']
}
```

### Custom data tokens

| Token | Type | Description |
|---|---|---|
| `voxel_count_0` | `int` | Number of voxels classified as background (label 0) |
| `voxel_count_1` | `int` | Number of voxels classified as material 1 (label 1) |
| `voxel_count_2` | `int` | Number of voxels classified as material 2 (label 2) |

The three counts always sum to the total number of voxels in the label array, providing a quick material-fraction overview without additional scripting:

```python
assert elem.voxel_count_0 + elem.voxel_count_1 + elem.voxel_count_2 == total_voxels
```

### Element selector with type filter

`VolumeSegmentation` requires a linked volume as input. The dialog uses `gom.api.dialog.create()` instead of `self.show_dialog()` so that a programmatic filter can be attached to the element selector widget before the dialog is displayed:

```python
def dialog(self, context, args):
    dlg = gom.api.dialog.create(context, '/Custom_VolumeSegmentation.gdlg')
    dlg.selected_element.filter = self.element_filter   # restrict to linked_volume type
    self.initialize_dialog(context, dlg, args)
    return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.VolumeSegmentation](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumesegmentation)

