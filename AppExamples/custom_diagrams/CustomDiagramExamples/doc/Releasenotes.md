# Releasenotes

## Installation Requirements

* Software Version
  * ZEISS INSPECT 2027

## Released at 2026-11-23 (v1.0.1)

* Updated click callbacks to read event parameters through `gom.read_parameters` and select the clicked element by UUID.
* Kept element overlay marker colors stable across re-renders without retaining click state in the diagram service.

## Released at 2026-08-28 (v1.0.0)

* Initial version of `CustomDiagramExamples`.
* Added self-contained custom element as diagram data source.
* Added three custom diagram services:
  * Basic static SVG diagram
  * Interactive element overlay diagram
  * Interactive point-cloud overlay diagram
* Added callback script for click interaction examples.
