# CustomValueElement

## Short description

> [!NOTE]
> This example is a companion to the [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html). Head there for the concept documentation.

This App demonstrates how to create custom value element contributions — one actual and one nominal — using the `@apicontribution` decorator.

| Class | Type | Features |
|---|---|---|
| `ActualValueElement` | `actuals.ValueElement` | Single float value; custom data token `value_squared` |
| `NominalValueElement` | `nominals.ValueElement` | Single float value; custom data token `value_squared` |

## Highlights

### Parameters

Both classes accept a single dialog parameter:

| Parameter | Type | Description |
|---|---|---|
| `value` | `float` (dimensionless) | The scalar value of the element |

### Value element return format

Unlike geometric elements, `ValueElement` returns a plain `float` (not a dict) as the `"value"`:

```python
return {
    "value": value,           # plain float, not a dict
    "data": {"value_squared": value * value}
}
```

### Custom data tokens

The `compute_stage()` method stores the square of the input value as a custom data token, demonstrating that custom data can hold values derived from the element's own value:

```python
value = float(values['value'])
return {
    "value": value,
    "data": {"value_squared": value * value}
}
```

After creation, the token is accessible as an element attribute:

```python
elem = gom.app.project.actual_elements["Actual Value Element"]
print(elem.value_squared)  # → 49.0  (if value was 7.0)
```

## Related links

- [How-to: Custom elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API — gom.api.extensions.actuals.ValueElement](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-actuals-valueelement)
- [API — gom.api.extensions.nominals.ValueElement](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-nominals-valueelement)
