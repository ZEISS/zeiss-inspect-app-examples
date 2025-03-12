# ScriptedDiagramBasics

![Circle radius histogram](scripted_diagram-histogram.png)

## Short description

This example includes a script for generating scripted actual circles, which can provide data &mdash; their radius &mdash; to any of two scripted diagram services. The diagram service `RadiusPlot` plots the radius of each circle element, the diagram service `RadiusHistogram` creates a radius histogram.

## Prerequisite

Review [Using scripted diagrams](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html) for a general introduction.

## Creating scripted actual circle elements

![Scripted circle creation parameters dialog](scripted_circle_dialog.png)

The script `scr_act_circle.py` creates a scripted circle and passes the radius to any of the two scripted diagram services, which is selected from the circle's creation parameters dialog.

The radius of any scripted circle is passed as a parameter to the scripted diagram service using:
``` python
context.data[stage] = {
    "ude_diagram_custom": 1,
    "ude_diagram_type": "SVGDiagram",
    # Selected by circle creation dialog:
    # polisher = 'gom.api.diagram.radius_plot' or polisher = 'gom.api.statistics.radius_histogram'
    "ude_diagram_service" : polisher,
    "ude_diagram_radius": params['radius']
}
```

## Managing the scripted diagram services

Use Apps->Manage Services... to start `RadiusPlot` and/or `RadiusHistogram`.

## Diagram settings

![App-Settings](app_settings.png)

The `RadiusHistogram` service uses some user settings from Preferences->App-Settings.

This feature is implemented using the [Settings API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-settings).

The settings are stored in `metainfo.json`:
```
...
"settings": [
        {
            "description": "Histogram bin edges",
            "name": "bins",
            "value": "0, 10, 20, 30",
            "visible": true
        },
        {
            "description": "Bar color",
            "name": "barcolor",
            "value": "blue",
            "visible": true
        },
        {
            "description": "Title",
            "name": "title",
            "value": "Circle radius histogram",
            "visible": true
        },
        {
            "description": "X label",
            "name": "xlabel",
            "value": "Radius",
            "visible": true
        },
        {
            "description": "Y label",
            "name": "ylabel",
            "value": "Count",
            "visible": true
        }
],
...
```

## View the diagram

The diagram is shown in the tab **Inspection Details** in the 3D view. Adding/removing scripted elements contributing to the diagram or modifying the scripted elements' creation parameters updates the diagram accordingly.

## See also

* [How-to: Using scripted diagrams](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)
* [How-to: Scripted elements](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_elements_toc.html)
* [How-to: Tokens on scripted elements](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/tokens_on_scripted_elements.html)
* [How-to: Using services](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_services/using_services.html)
* [Settings API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-settings)
* [Matplotlib: Visualization with Python](https://matplotlib.org/)

