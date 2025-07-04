# ResourceAccess

Demonstration for accessing App based resources via scripts.

## Highlights

1. **Reading a resource**

Resources are addressed with a relative or absolute file system path. In this example, the path relative to the Python script file is used:

```python
with gom.Resource("assets/zeiss_logo.png").open() as fh:
    data = fh.read()
```

The equivalent absolute path is `:Resources/assets/zeiss_logo.png`.

* An absolute has the prefix `:`
* The root folder is `<App>/scripts`

2. **Using an image from a resource**

```python
print ('Type:', type (data))
# Output: Type: <class 'bytes'>

print ('Size:', len (data))
# Output: Size: 29387

# [...]

# Use script dialog to display the resource as an image. The 'data' field of
# the image widget expects a displayable byte object and will render it.
DIALOG.image.data = data

# [...]
```

## See also

* [gom.api.resource](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/resource_api.html)
* [Image widget](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#image-widget)
