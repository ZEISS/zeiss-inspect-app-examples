# CustomVolumeSection

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

> [!NOTE]
> This example requires **ZEISS INSPECT X-Ray**.

This App demonstrates how to create a custom actual `VolumeSection` element using the `@apicontribution` decorator. It mirrors the functionality of the [ScriptedActualVolumeSection](../../scripted_actuals/ScriptedActualVolumeSection/doc/Documentation.md) example: a grayscale image is loaded from disk, converted to a float32 pixel array, and placed in 3D space via a full 4×4 rotation + translation matrix.

| Class | Type | Features |
|---|---|---|
| `ActualVolumeSection` | `actuals.VolumeSection` | Grayscale image → float32 pixel_data; ZYX Euler placement; format-restricted `Image.open` |

## Highlights

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `file` | file path | Path to a JPG, PNG, GIF or TIFF grayscale image |
| `dx`, `dy`, `dz` | `float` (LENGTH) | Translation of the section plane |
| `rx`, `ry`, `rz` | `float` (ANGLE) | Rotation angles (ZYX Euler, radians) |

### Compute result

The `compute_stage()` method returns the image-derived section data and placement transformation:

```python
return {
    'pixel_data': img_array,       # np.array, shape (H, W), dtype=float32
    'transformation': transformation  # gom.Mat4x4
}
```

### Security: restricted image formats

`Image.open()` is called with an explicit `formats` allowlist to prevent decompression-bomb and other image-based attacks (see [dependabot advisory #3](https://github.com/ZEISS/zeiss-inspect-app-examples/security/dependabot/3)):

```python
ALLOWED_FORMATS = ['JPEG', 'PNG', 'GIF', 'TIFF']
image = Image.open(file, formats=ALLOWED_FORMATS)
```

### App resource path support (for testing)

If the file value starts with `':'`, it is interpreted as an App resource path (e.g. `':CustomVolumeSection/Grayscale_8bits_palette.png'`). This allows automated tests to run without requiring an external file on disk.

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.VolumeSection](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-volumesection)
