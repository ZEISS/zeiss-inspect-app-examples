# CustomDiagramExamples

## Overview

This example App demonstrates the custom diagram patterns from the custom diagrams howto in one self-contained App:

1. Basic custom diagram (static SVG)
2. Custom diagram with auto-generated element overlay
3. Custom diagram with manual point-based overlay

The App includes a custom actual circle element so no external custom element example is required.

## Included Scripts

- `Custom_Circle.py`: custom actual and nominal circle elements plus the shared diagram payload mapping in `finish()`.
- `basic_custom_diagram.py`: static SVG diagram service.
- `element_overlay_custom_diagram.py`: interactive overlay using full-element mapping and matplotlib `gid` tags. Here, `gid` is the SVG group identifier written into the exported plot so the `SVGDiagram` renderer can associate a drawn marker with the corresponding ZEISS INSPECT element UUID.
- `point_cloud_overlay_custom_diagram.py`: interactive overlay using point-cloud display coordinates.
- `diagram_click_callback.py`: callback script triggered by interactive diagram clicks.

## Prerequisites

1. Configure and start the app services in ZEISS INSPECT.
2. Ensure required Python packages are available (`matplotlib`, `numpy`).
3. Open the `Inspection Details` tab in the 3D View to see custom diagrams.

## Usage

1. Start services from the App service manager.
2. Create a custom actual circle element (dialog from `Custom_Circle.gdlg`).
3. Open the element in the 3D view and switch to `Inspection Details`.
4. Select one of the generated diagrams:
   - `Basic Custom Diagram`
   - `Interactive Custom Diagram with Element Overlay`
   - `Interactive Custom Diagram with Point Cloud Overlay`

## How It Works

### Basic Custom Diagram

- Uses contribution-based routing in `finish()`: `add_diagram_data(..., service_id='com.zeiss.example.custom_diagrams.basic', ...)` points to the diagram contribution id.
- Intentionally returns a raw SVG string from `plot()`. `SVGDiagram` sanitizes this automatically into the renderer format.

### Element Overlay Diagram

- Enables auto-generated overlay mode: plotted markers are tagged via `get_overlay_tag(...)`, and `finish_plot(..., render_config={'auto_generated_overlay_use': True})` lets the renderer derive full-element hitboxes from tagged SVG groups.
- Uses matplotlib `gid` tags: the `gid` attribute becomes the SVG group `id` in exported markup and bridges plotted graphics to ZEISS INSPECT element UUIDs.
- Keeps marker size stable across re-renders and recolors the last clicked element in the diagram service itself.

### Point-Cloud Overlay Diagram

- Uses point-based overlay mode: interaction points are derived from `mpltools.get_display_coords(...)`, normalized to relative coordinates, and passed to `add_element_to_overlay(...)`.
- Uses fixed marker size and color.
- Keeps `custom_interaction=True` on the first overlay point only; remaining points are added without custom interaction to explicitly demonstrate mixed interaction behavior.

### Shared Behavior

- The examples follow the current `plot(view, element_data)` contract from `gom.api.extensions.diagrams`: each entry is read via `entry['element']`, `entry['data']`, and `entry['type']`.
- UUIDs and display names for overlays are resolved from `entry['element']`.
- The callback script logs event data and attempts a UUID-based selection as a demo action.
- The custom circle contributions attach the payload from `finish()` directly; diagram scripts receive that payload under `entry['data']`.

## References

- [HowTo: Using Custom Diagrams](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/using_custom_diagrams/using_custom_diagrams.html)
- [HowTo: Custom Elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)
- [API: gom.api.extensions.diagrams](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-diagrams)
