# ZEISS INSPECT App Examples Overview

```{important}
The examples provided here serve as illustrative versions of ZEISS INSPECT Apps. They are not intended for productive use.
Users may utilize these examples at their own risk, and ZEISS assumes no liability for their use.
```

## custom_diagrams &mdash; How to create custom diagrams

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="CustomDiagramExamples">CustomDiagramExamples</a><br>[view](custom_diagrams/CustomDiagramExamples/doc/Documentation.md)  | Self-contained custom diagram examples: basic rendering, element overlay, and point-cloud overlay. | | [HowTo - Custom Diagrams](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/using_custom_diagrams/using_custom_diagrams.html)<br>[HowTo - Custom Elements](https://zeiss.github.io/zeiss-inspect-app-api/main/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - diagrams](https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-diagrams)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/custom--diagrams-blue)](#custom-diagrams)<br>[![Static Badge](https://img.shields.io/badge/custom--elements-blue)](#custom-elements)<br>[![Static Badge](https://img.shields.io/badge/overlay-blue)](#overlay)<br>[![Static Badge](https://img.shields.io/badge/matplotlib-blue)](#matplotlib)<br> |

## custom_elements &mdash; How to create custom elements

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="CustomCircle">CustomCircle</a><br>[view](custom_elements/CustomCircle/doc/Documentation.md)  | This example shows how to create a custom nominal/actual circle element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Circle](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-circle)<br>[API - nominals.Circle](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-circle)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/circle-blue)](#circle)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomCone">CustomCone</a><br>[view](custom_elements/CustomCone/doc/Documentation.md)  | This example shows how to create a custom nominal/actual cone element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Cone](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-cone)<br>[API - nominals.Cone](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-cone)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/cone-blue)](#cone)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomCurve">CustomCurve</a><br>[view](custom_elements/CustomCurve/doc/Documentation.md)  | This example shows how to create a custom nominal/actual curve element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Curve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-curve)<br>[API - nominals.Curve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-curve)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/curve-blue)](#curve)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomCurveInspection">CustomCurveInspection</a><br>[view](custom_elements/CustomCurveInspection/doc/Documentation.md)  | This example shows how to create a Custom Curve Inspection element using the gom.api.extensions.inspections.Curve API. A curve inspection assigns per-vertex deviation values to a curve element, displayed as a color-coded deviation plot along the curve. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_inspections.html)<br>[API - inspections.Curve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-inspections-curve)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/curve--check-blue)](#curve-check)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br>[![Static Badge](https://img.shields.io/badge/inspection-blue)](#inspection)<br> |
| <a id="CustomCylinder">CustomCylinder</a><br>[view](custom_elements/CustomCylinder/doc/Documentation.md)  | This example shows how to create a custom nominal/actual cylinder element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Cylinder](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-cylinder)<br>[API - nominals.Cylinder](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-cylinder)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/cylinder-blue)](#cylinder)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomDistance">CustomDistance</a><br>[view](custom_elements/CustomDistance/doc/Documentation.md)  | This example shows how to create a custom nominal/actual distance element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Distance](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-distance)<br>[API - nominals.Distance](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-distance)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/distance-blue)](#distance)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomPlane">CustomPlane</a><br>[view](custom_elements/CustomPlane/doc/Documentation.md)  | This example shows how to create a custom nominal/actual plane element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Plane](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-plane)<br>[API - nominals.Plane](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-plane)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/plane-blue)](#plane)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomPoint">CustomPoint</a><br>[view](custom_elements/CustomPoint/doc/Documentation.md)  | This example shows how to create a custom nominal/actual offset point element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Point](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-point)<br>[API - nominals.Point](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-point)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/point-blue)](#point)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomPointCloud">CustomPointCloud</a><br>[view](custom_elements/CustomPointCloud/doc/Documentation.md)  | This example shows how to create a custom nominal/actual point cloud element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.PointCloud](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-pointcloud)<br>[API - nominals.PointCloud](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-pointcloud)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/point--cloud-blue)](#point-cloud)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomProbeMeasuredCurve">CustomProbeMeasuredCurve</a><br>[view](custom_elements/CustomProbeMeasuredCurve/doc/Documentation.md)  | This example shows how to create a custom actual probe measured curve element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.ProbeMeasuredCurve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-probemeasuredcurve)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/probe--measured--curve-blue)](#probe-measured-curve)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomScalarInspection">CustomScalarInspection</a><br>[view](custom_elements/CustomScalarInspection/doc/Documentation.md)  | This example shows how to create a Custom Scalar Inspection element using the gom.api.extensions.inspections.Scalar API. A scalar inspection compares the deviation of an existing inspection element against user-defined tolerance limits, creating a new check result on top of the original inspection. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_inspections.html)<br>[API - inspections.Scalar](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-inspections-scalar)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/scalar--check-blue)](#scalar-check)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br>[![Static Badge](https://img.shields.io/badge/inspection-blue)](#inspection)<br> |
| <a id="CustomSection">CustomSection</a><br>[view](custom_elements/CustomSection/doc/Documentation.md)  | This example shows how to create a custom nominal/actual section element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Section](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-section)<br>[API - nominals.Section](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-section)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/section-blue)](#section)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomSequence">CustomSequence</a><br>[view](custom_elements/CustomSequence/doc/Documentation.md)  | Example for a custom sequence element that creates a datum plane through 3 reference points. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - sequence.CustomSequence](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-sequence-customsequence)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/custom--sequence-blue)](#custom-sequence)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br>[![Static Badge](https://img.shields.io/badge/datum--plane-blue)](#datum-plane)<br>[![Static Badge](https://img.shields.io/badge/reference--points-blue)](#reference-points)<br> |
| <a id="CustomSurface">CustomSurface</a><br>[view](custom_elements/CustomSurface/doc/Documentation.md)  | This example shows how to create a custom nominal/actual surface element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Surface](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-surface)<br>[API - nominals.Surface](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-surface)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomSurfaceCurve">CustomSurfaceCurve</a><br>[view](custom_elements/CustomSurfaceCurve/doc/Documentation.md)  | This example shows how to create a custom nominal/actual surface curve element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.SurfaceCurve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-surfacecurve)<br>[API - nominals.SurfaceCurve](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-surfacecurve)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/surface--curve-blue)](#surface-curve)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomSurfaceInspection">CustomSurfaceInspection</a><br>[view](custom_elements/CustomSurfaceInspection/doc/Documentation.md)  | This example shows how to create a Custom Surface Inspection element using the gom.api.extensions.inspections.Surface API. A surface inspection assigns per-vertex deviation values to a mesh element, displayed as a color-coded deviation map on the surface. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_inspections.html)<br>[API - inspections.Surface](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-inspections-surface)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/surface--check-blue)](#surface-check)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br>[![Static Badge](https://img.shields.io/badge/inspection-blue)](#inspection)<br> |
| <a id="CustomValueElement">CustomValueElement</a><br>[view](custom_elements/CustomValueElement/doc/Documentation.md)  | This example shows how to create a custom nominal/actual value element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.ValueElement](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-valueelement)<br>[API - nominals.ValueElement](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-nominals-valueelement)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/value--element-blue)](#value-element)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolume">CustomVolume</a><br>[view](custom_elements/CustomVolume/doc/Documentation.md)  | This example shows how to create a custom actual volume element from artificial voxel data (NumPy array). | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.Volume](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volume)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume-blue)](#volume)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolumeDefects">CustomVolumeDefects</a><br>[view](custom_elements/CustomVolumeDefects/doc/Documentation.md)  | This example shows how to create a custom actual volume defects element from a tetrahedron defined by four vertices. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.VolumeDefects](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumedefects)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--defects-blue)](#volume-defects)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolumeDefects2d">CustomVolumeDefects2d</a><br>[view](custom_elements/CustomVolumeDefects2d/doc/Documentation.md)  | This example shows how to create a custom actual 2D volume defects element from parametric circular defect contours. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.VolumeDefects2d](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumedefects2d)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--defects--2d-blue)](#volume-defects-2d)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolumeRegion">CustomVolumeRegion</a><br>[view](custom_elements/CustomVolumeRegion/doc/Documentation.md)  | This example shows how to create a custom actual volume region element from a user-defined region of interest within a linked volume. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.VolumeRegion](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumeregion)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--region-blue)](#volume-region)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolumeSection">CustomVolumeSection</a><br>[view](custom_elements/CustomVolumeSection/doc/Documentation.md)  | This example shows how to create a custom actual volume section element from a grayscale image and a placement transformation. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.VolumeSection](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumesection)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--section-blue)](#volume-section)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |
| <a id="CustomVolumeSegmentation">CustomVolumeSegmentation</a><br>[view](custom_elements/CustomVolumeSegmentation/doc/Documentation.md)  | This example shows how to create a custom actual volume segmentation element that classifies voxels of a linked volume into three material segments using two grayscale thresholds. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2027/howtos/custom_elements/custom_nominals_actuals.html)<br>[API - actuals.VolumeSegmentation](https://zeiss.github.io/zeiss-inspect-app-api/2027/python_api/python_api.html#gom-api-extensions-actuals-volumesegmentation)<br> | ZEISS INSPECT 2027 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--segmentation-blue)](#volume-segmentation)<br>[![Static Badge](https://img.shields.io/badge/custom--element-blue)](#custom-element)<br> |

## data_interfaces &mdash; How to access data of ZEISS INSPECT elements

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="CheckResultsDataArray">CheckResultsDataArray</a><br>[view](data_interfaces/CheckResultsDataArray/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/check-results-data-array) | This example demonstrates two ways of accessing result data from checks using the element properties and data interfaces. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/python_api_introduction/python_api_introduction.html#access-element-properties)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/element--properties-blue)](#element-properties)<br>[![Static Badge](https://img.shields.io/badge/element--data-blue)](#element-data)<br> |
| <a id="ReferencePointsAndMeshData">ReferencePointsAndMeshData</a><br>[view](data_interfaces/ReferencePointsAndMeshData/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/reference-points-and-mesh-data) | This example demonstrates how to access the reference points in a measurement and the mesh from Python. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/reference--points-blue)](#reference-points)<br>[![Static Badge](https://img.shields.io/badge/mesh-blue)](#mesh)<br>[![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="VolumeSectionImageData">VolumeSectionImageData</a><br>[view](data_interfaces/VolumeSectionImageData/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/volume-section-image-data) | This example demonstrates how to access the image data of a volume section. | [3)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/element--data-blue)](#element-data)<br> |

## dialog_widgets &mdash; How to use custom dialogs and handle user input events

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="DropdownWidget">DropdownWidget</a><br>[view](dialog_widgets/DropdownWidget/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/dropdown-widget) | This basic example shows how to use the dropdown widget and how to define items at script runtime. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-list-widget)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)](#selection-list-widget)<br> |
| <a id="ExplorerSelectedElementsInDialog">ExplorerSelectedElementsInDialog</a><br>[view](dialog_widgets/ExplorerSelectedElementsInDialog/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/explorer-selected-elements-in-dialog) | This example shows how to get a list of elements selected in the element explorer and use it in a script dialog.  | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-element-widget)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)](#selection-element-widget)<br> |
| <a id="UnitDialogEventHandler">UnitDialogEventHandler</a><br>[view](dialog_widgets/UnitDialogEventHandler/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/unit-dialog-event-handler) | This basic example demonstrates how to use an event handler on a script dialog to set the unit to multiple widgets. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#unit-widget)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/unit--widget-blue)](#unit-widget)<br> |
| <a id="WidgetVisibility">WidgetVisibility</a><br>[view](dialog_widgets/WidgetVisibility/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/widget-visibility) | This example shows how to use a dialog event handler to turn on/off widget visibilities. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/widget--properties-blue)](#widget-properties)<br> |

## misc &mdash; Miscellaneous

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="CSVExample">CSVExample</a><br>[view](misc/CSVExample/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/csv-example) | This example demonstrates how to read and write CSV files (comma separated values) from an App. | [1)](#example-projects)  |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br>[![Static Badge](https://img.shields.io/badge/export-blue)](#export)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="DialogReopenExample">DialogReopenExample</a><br>[view](misc/DialogReopenExample/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/dialog-reopen-example) | This examples demonstrates, how a dialog can be closed from its own handler, just to be opened again. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#executing-dialogs)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br> |
| <a id="DisplayImage">DisplayImage</a><br>[view](misc/DisplayImage/doc/Documentation.md)  | Display measurement as a single image | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br>[![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="ExcelExample">ExcelExample</a><br>[view](misc/ExcelExample/doc/Documentation.md)  | Example for reading and writing Excel files from an App | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br>[![Static Badge](https://img.shields.io/badge/export-blue)](#export)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="FileSelectionAndFiltering">FileSelectionAndFiltering</a><br>[view](misc/FileSelectionAndFiltering/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/file-selection-and-filtering) | File Selection and Filtering Examples | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/file-blue)](#file)<br>[![Static Badge](https://img.shields.io/badge/directory-blue)](#directory)<br>[![Static Badge](https://img.shields.io/badge/folder-blue)](#folder)<br>[![Static Badge](https://img.shields.io/badge/path-blue)](#path)<br> |
| <a id="IPCWebsocketBasics">IPCWebsocketBasics</a><br>[view](misc/IPCWebsocketBasics/doc/Documentation.md)  | Basic example for triggering command execution in ZEISS INSPECT from command line via WebSocket protocol | |  | ZEISS INSPECT 2023 |  |
| <a id="IPCWebsocketExample">IPCWebsocketExample</a><br>[view](misc/IPCWebsocketExample/doc/Documentation.md)  | Example for triggering command execution via WebSocket protocol | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br> |
| <a id="MeasurementSystemAnalysis">MeasurementSystemAnalysis</a><br>[view](misc/MeasurementSystemAnalysis/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/measurement-system-analysis) | MSA conformal measurement system analysis (ANOVA, ARM) | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="PointPixelTransformations">PointPixelTransformations</a><br>[view](misc/PointPixelTransformations/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/point-pixel-transformations) | This example demonstrates how to find the 2D pixel coordinates of a 3D point coordinate and vice versa. | [2)](#example-projects)  | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-imaging)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br>[![Static Badge](https://img.shields.io/badge/reference--points-blue)](#reference-points)<br> |
| <a id="ProgressBar">ProgressBar</a><br>[view](misc/ProgressBar/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/progress-bar) | This example shows how to display a progress bar at the bottom of the ZEISS INSPECT main window | |  | ZEISS INSPECT 2025 |  |
| <a id="PytestTemplate">PytestTemplate</a><br>[view](misc/PytestTemplate/doc/Documentation.md)  | App template for running integration tests and unit tests with coverage using pytest | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html)<br> | ZEISS INSPECT 2025 | [![Static Badge](https://img.shields.io/badge/testing-blue)](#testing)<br> |
| <a id="Pywin32Example">Pywin32Example</a><br>[view](misc/Pywin32Example/doc/Documentation.md)  | Example demonstrating how to use the pywin32 package in a ZEISS INSPECT App | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/pywin32-blue)](#pywin32)<br>[![Static Badge](https://img.shields.io/badge/windows-blue)](#windows)<br>[![Static Badge](https://img.shields.io/badge/python-blue)](#python)<br> |
| <a id="SQLExample">SQLExample</a><br>[view](misc/SQLExample/doc/Documentation.md)  | Example for SQL Database Access | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/sql--database-blue)](#sql-database)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="ServiceExample">ServiceExample</a><br>[view](misc/ServiceExample/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/service-example) | Service API Example | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_services/using_services.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-services)<br> | ZEISS INSPECT 2025 | [![Static Badge](https://img.shields.io/badge/service-blue)](#service)<br> |
| <a id="SettingsAPI">SettingsAPI</a><br>[view](misc/SettingsAPI/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/settings-api) | Example App demonstrating usage of the settings API | | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-settings)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br> |
| <a id="TemplateUnittestCoverage">TemplateUnittestCoverage</a><br>[view](misc/TemplateUnittestCoverage/doc/Documentation.md)  | App template for running unit testing and generating a test coverage report | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/testing-blue)](#testing)<br> |
| <a id="TextDetection">TextDetection</a><br>[view](misc/TextDetection/doc/Documentation.md)  | Text detection example | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br>[![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br> |
| <a id="WorkflowAssistants">WorkflowAssistants</a><br>[view](misc/WorkflowAssistants/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/workflow-assistants) | Examples for Workflow Assistants | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/workflow_assistant/workflow_assistant.html)<br> | ZEISS INSPECT 2025 | [![Static Badge](https://img.shields.io/badge/workflow--assistant-blue)](#workflow-assistant)<br>[![Static Badge](https://img.shields.io/badge/workspace-blue)](#workspace)<br> |
| <a id="Workspace">Workspace</a><br>[view](misc/Workspace/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/workspace) | Template for custom workspaces | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/adding_workspaces_to_apps/adding_workspaces_to_apps.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/api-blue)](#api)<br>[![Static Badge](https://img.shields.io/badge/workspace-blue)](#workspace)<br> |

## projects &mdash; ZEISS INSPECT projects

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="ExampleProjects">ExampleProjects</a><br>[view](projects/ExampleProjects/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/example-projects) | ZEISS INSPECT Example Projects | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/project-blue)](#project)<br> |

## script_icons &mdash; How to set icons for scripts or buttons

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="ScriptIcon">ScriptIcon</a><br>[view](script_icons/ScriptIcon/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/script-icon) | This example shows how an icon can be set to a script, whereas the icon itself resides in the App as a resource. | |  | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/menu-blue)](#menu)<br> |

## script_resources &mdash; How to access binary data of your App (resources)

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="ResourceAccess">ResourceAccess</a><br>[view](script_resources/ResourceAccess/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/resource-access) | Accessing an image as an App based resources | | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/resource_api.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/resources-blue)](#resources)<br>[![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br> |
| <a id="ScriptResources">ScriptResources</a><br>[view](script_resources/ScriptResources/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/script-resources) | A simple example showing the usage of script resources. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/using_script_resources.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/resource_api.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/resources-blue)](#resources)<br> |

## scripted_actuals &mdash; Building custom actual elements (deprecated)

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="ScriptedActualCircle">ScriptedActualCircle</a><br>[view](scripted_actuals/ScriptedActualCircle/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-circle) | This is an example for a scripted actual 'circle' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#circle)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/circle-blue)](#circle)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCone">ScriptedActualCone</a><br>[view](scripted_actuals/ScriptedActualCone/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-cone) | This is an example for a scripted actual 'cone' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#cone)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/cone-blue)](#cone)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCurve">ScriptedActualCurve</a><br>[view](scripted_actuals/ScriptedActualCurve/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-curve) | This is an example for a scripted actual 'curve' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#curve)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/curve-blue)](#curve)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCylinder">ScriptedActualCylinder</a><br>[view](scripted_actuals/ScriptedActualCylinder/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-cylinder) | This is an example for a scripted actual 'cylinder' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#cylinder)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/cylinder-blue)](#cylinder)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualDistance">ScriptedActualDistance</a><br>[view](scripted_actuals/ScriptedActualDistance/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-distance) | This is an example for a scripted actual 'distance' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#distance)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/distance-blue)](#distance)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualPoint">ScriptedActualPoint</a><br>[view](scripted_actuals/ScriptedActualPoint/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-point) | These are two examples for scripted actual points, which serve as an introduction to the concept of scripted actual elements. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#point)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/point-blue)](#point)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualPointCloud">ScriptedActualPointCloud</a><br>[view](scripted_actuals/ScriptedActualPointCloud/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-point-cloud) | This is an example for a scripted actual 'point cloud' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#point-cloud)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/point--cloud-blue)](#point-cloud)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSection">ScriptedActualSection</a><br>[view](scripted_actuals/ScriptedActualSection/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-section) | This is an example for a scripted actual 'section' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#section)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/section-blue)](#section)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSurface">ScriptedActualSurface</a><br>[view](scripted_actuals/ScriptedActualSurface/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-surface) | This is an example for a scripted actual 'surface' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#surface)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSurfaceCurve">ScriptedActualSurfaceCurve</a><br>[view](scripted_actuals/ScriptedActualSurfaceCurve/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-surface-curve) | This is an example for a scripted actual 'surface curve' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#surface-curve)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/surface--curve-blue)](#surface-curve)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolume">ScriptedActualVolume</a><br>[view](scripted_actuals/ScriptedActualVolume/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-volume) | This is an example for a scripted actual 'volume' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#volume)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume-blue)](#volume)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeDefects">ScriptedActualVolumeDefects</a><br>[view](scripted_actuals/ScriptedActualVolumeDefects/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-volume-defects) | This is an example for a scripted actual 'volume defects' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#volume-defects)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--defects-blue)](#volume-defects)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeRegion">ScriptedActualVolumeRegion</a><br>[view](scripted_actuals/ScriptedActualVolumeRegion/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-volume-region) | This is an example for a scripted actual 'volume region' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#volume-region)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--region-blue)](#volume-region)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeSection">ScriptedActualVolumeSection</a><br>[view](scripted_actuals/ScriptedActualVolumeSection/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-volume-section) | This is an example for a scripted actual 'volume section' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#volume-section)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--section-blue)](#volume-section)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedElementProgress">ScriptedElementProgress</a><br>[view](scripted_actuals/ScriptedElementProgress/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-element-progress) | This examples demonstrates how to show progress information to the user while calculating a scripted element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/computation--progress-blue)](#computation-progress)<br> |
| <a id="TrimeshDeformMesh">TrimeshDeformMesh</a><br>[view](scripted_actuals/TrimeshDeformMesh/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/trimesh-deform-mesh) | This example demonstrates how to generate a custom surface element using a scripted element. The example script accesses mesh information from an existing mesh in the project and adds a random deformation to each point. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#surface)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/mesh-blue)](#mesh)<br>[![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |

## scripted_checks &mdash; Building custom checks (deprecated)

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="ScriptedCurveCheck">ScriptedCurveCheck</a><br>[view](scripted_checks/ScriptedCurveCheck/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-curve-check) | This example demonstrates how to create a scalar curve check by a script. Also, the usage of custom coordinate systems in scripted checks is shown. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#scalar-curve)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/curve-blue)](#curve)<br> |
| <a id="ScriptedScalarCheck">ScriptedScalarCheck</a><br>[view](scripted_checks/ScriptedScalarCheck/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-scalar-check) | This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#scalar)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/scalar-blue)](#scalar)<br> |
| <a id="ScriptedSurfaceCheck">ScriptedSurfaceCheck</a><br>[view](scripted_checks/ScriptedSurfaceCheck/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-surface-check) | This example demonstrates how to create a scalar surface check by a script. Also, the usage of custom coordinate systems and element preview in scripted checks is shown. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2026/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#scalar-surface)<br> | ZEISS INSPECT 2023 | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br> |

## scripted_diagrams &mdash; Creating custom diagrams (deprecated)

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | Required Software | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | -------- | ---- |
| <a id="OSMMapDiagram">OSMMapDiagram</a><br>[view](scripted_diagrams/OSMMapDiagram/doc/Documentation.md)  | Display geolocation using a scripted diagram | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)<br> | ZEISS INSPECT 2025 | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br>[![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)](#scripted-diagrams)<br> |
| <a id="ScriptedDiagramBasics">ScriptedDiagramBasics</a><br>[view](scripted_diagrams/ScriptedDiagramBasics/doc/Documentation.md)  | Scripted diagram basics | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)<br> | ZEISS INSPECT 2025 | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br>[![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)](#scripted-diagrams)<br> |

## Example projects

| No. | Project name | Description |
| --- | ------------ | ----------- |
| 1 | zeiss_part_test_project | Simple optically measured part with a CAD, mesh and some basic inspections |
| 2 | zeiss_part_test_measurement | Optical measurement series and preliminary mesh of ZEISS part |
| 3 | volume_test_project | A small test volume for CT related inspections |

[Download Example Projects App](https://software-store.zeiss.com/products/apps/example-projects)

## Tag Index

<a name="api"></a>![Static Badge](https://img.shields.io/badge/api-blue)

* [Workspace](#Workspace)


<a name="circle"></a>![Static Badge](https://img.shields.io/badge/circle-blue)

* [CustomCircle](#CustomCircle)
* [ScriptedActualCircle](#ScriptedActualCircle)


<a name="computation-progress"></a>![Static Badge](https://img.shields.io/badge/computation--progress-blue)

* [ScriptedElementProgress](#ScriptedElementProgress)


<a name="cone"></a>![Static Badge](https://img.shields.io/badge/cone-blue)

* [CustomCone](#CustomCone)
* [ScriptedActualCone](#ScriptedActualCone)


<a name="curve"></a>![Static Badge](https://img.shields.io/badge/curve-blue)

* [CustomCurve](#CustomCurve)
* [ScriptedActualCurve](#ScriptedActualCurve)
* [ScriptedCurveCheck](#ScriptedCurveCheck)


<a name="curve-check"></a>![Static Badge](https://img.shields.io/badge/curve--check-blue)

* [CustomCurveInspection](#CustomCurveInspection)


<a name="custom-diagrams"></a>![Static Badge](https://img.shields.io/badge/custom--diagrams-blue)

* [CustomDiagramExamples](#CustomDiagramExamples)


<a name="custom-element"></a>![Static Badge](https://img.shields.io/badge/custom--element-blue)

* [CustomCircle](#CustomCircle)
* [CustomCone](#CustomCone)
* [CustomCurve](#CustomCurve)
* [CustomCurveInspection](#CustomCurveInspection)
* [CustomCylinder](#CustomCylinder)
* [CustomDistance](#CustomDistance)
* [CustomPlane](#CustomPlane)
* [CustomPoint](#CustomPoint)
* [CustomPointCloud](#CustomPointCloud)
* [CustomProbeMeasuredCurve](#CustomProbeMeasuredCurve)
* [CustomScalarInspection](#CustomScalarInspection)
* [CustomSection](#CustomSection)
* [CustomSequence](#CustomSequence)
* [CustomSurface](#CustomSurface)
* [CustomSurfaceCurve](#CustomSurfaceCurve)
* [CustomSurfaceInspection](#CustomSurfaceInspection)
* [CustomValueElement](#CustomValueElement)
* [CustomVolume](#CustomVolume)
* [CustomVolumeDefects](#CustomVolumeDefects)
* [CustomVolumeDefects2d](#CustomVolumeDefects2d)
* [CustomVolumeRegion](#CustomVolumeRegion)
* [CustomVolumeSection](#CustomVolumeSection)
* [CustomVolumeSegmentation](#CustomVolumeSegmentation)


<a name="custom-elements"></a>![Static Badge](https://img.shields.io/badge/custom--elements-blue)

* [CustomDiagramExamples](#CustomDiagramExamples)


<a name="custom-sequence"></a>![Static Badge](https://img.shields.io/badge/custom--sequence-blue)

* [CustomSequence](#CustomSequence)


<a name="cylinder"></a>![Static Badge](https://img.shields.io/badge/cylinder-blue)

* [CustomCylinder](#CustomCylinder)
* [ScriptedActualCylinder](#ScriptedActualCylinder)


<a name="datum-plane"></a>![Static Badge](https://img.shields.io/badge/datum--plane-blue)

* [CustomSequence](#CustomSequence)


<a name="dialog"></a>![Static Badge](https://img.shields.io/badge/dialog-blue)

* [DialogReopenExample](#DialogReopenExample)
* [DropdownWidget](#DropdownWidget)
* [ExplorerSelectedElementsInDialog](#ExplorerSelectedElementsInDialog)
* [UnitDialogEventHandler](#UnitDialogEventHandler)
* [WidgetVisibility](#WidgetVisibility)


<a name="directory"></a>![Static Badge](https://img.shields.io/badge/directory-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


<a name="distance"></a>![Static Badge](https://img.shields.io/badge/distance-blue)

* [CustomDistance](#CustomDistance)
* [ScriptedActualDistance](#ScriptedActualDistance)


<a name="element-data"></a>![Static Badge](https://img.shields.io/badge/element--data-blue)

* [CheckResultsDataArray](#CheckResultsDataArray)
* [VolumeSectionImageData](#VolumeSectionImageData)


<a name="element-properties"></a>![Static Badge](https://img.shields.io/badge/element--properties-blue)

* [CheckResultsDataArray](#CheckResultsDataArray)


<a name="export"></a>![Static Badge](https://img.shields.io/badge/export-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)


<a name="file"></a>![Static Badge](https://img.shields.io/badge/file-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


<a name="folder"></a>![Static Badge](https://img.shields.io/badge/folder-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


<a name="image-widget"></a>![Static Badge](https://img.shields.io/badge/image--widget-blue)

* [DisplayImage](#DisplayImage)
* [ResourceAccess](#ResourceAccess)
* [TextDetection](#TextDetection)


<a name="import"></a>![Static Badge](https://img.shields.io/badge/import-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)
* [IPCWebsocketExample](#IPCWebsocketExample)


<a name="inspection"></a>![Static Badge](https://img.shields.io/badge/inspection-blue)

* [CustomCurveInspection](#CustomCurveInspection)
* [CustomScalarInspection](#CustomScalarInspection)
* [CustomSurfaceInspection](#CustomSurfaceInspection)


<a name="matplotlib"></a>![Static Badge](https://img.shields.io/badge/matplotlib-blue)

* [CustomDiagramExamples](#CustomDiagramExamples)


<a name="measurement"></a>![Static Badge](https://img.shields.io/badge/measurement-blue)

* [DisplayImage](#DisplayImage)
* [MeasurementSystemAnalysis](#MeasurementSystemAnalysis)
* [PointPixelTransformations](#PointPixelTransformations)
* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)
* [TextDetection](#TextDetection)


<a name="menu"></a>![Static Badge](https://img.shields.io/badge/menu-blue)

* [ScriptIcon](#ScriptIcon)


<a name="mesh"></a>![Static Badge](https://img.shields.io/badge/mesh-blue)

* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)
* [TrimeshDeformMesh](#TrimeshDeformMesh)


<a name="overlay"></a>![Static Badge](https://img.shields.io/badge/overlay-blue)

* [CustomDiagramExamples](#CustomDiagramExamples)


<a name="path"></a>![Static Badge](https://img.shields.io/badge/path-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


<a name="plane"></a>![Static Badge](https://img.shields.io/badge/plane-blue)

* [CustomPlane](#CustomPlane)


<a name="point"></a>![Static Badge](https://img.shields.io/badge/point-blue)

* [CustomPoint](#CustomPoint)
* [ScriptedActualPoint](#ScriptedActualPoint)


<a name="point-cloud"></a>![Static Badge](https://img.shields.io/badge/point--cloud-blue)

* [CustomPointCloud](#CustomPointCloud)
* [ScriptedActualPointCloud](#ScriptedActualPointCloud)


<a name="probe-measured-curve"></a>![Static Badge](https://img.shields.io/badge/probe--measured--curve-blue)

* [CustomProbeMeasuredCurve](#CustomProbeMeasuredCurve)


<a name="project"></a>![Static Badge](https://img.shields.io/badge/project-blue)

* [ExampleProjects](#ExampleProjects)


<a name="project-keywords"></a>![Static Badge](https://img.shields.io/badge/project--keywords-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)
* [SQLExample](#SQLExample)


<a name="python"></a>![Static Badge](https://img.shields.io/badge/python-blue)

* [Pywin32Example](#Pywin32Example)


<a name="pywin32"></a>![Static Badge](https://img.shields.io/badge/pywin32-blue)

* [Pywin32Example](#Pywin32Example)


<a name="reference-points"></a>![Static Badge](https://img.shields.io/badge/reference--points-blue)

* [CustomSequence](#CustomSequence)
* [PointPixelTransformations](#PointPixelTransformations)
* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)


<a name="resources"></a>![Static Badge](https://img.shields.io/badge/resources-blue)

* [ResourceAccess](#ResourceAccess)
* [ScriptResources](#ScriptResources)


<a name="scalar"></a>![Static Badge](https://img.shields.io/badge/scalar-blue)

* [ScriptedScalarCheck](#ScriptedScalarCheck)


<a name="scalar-check"></a>![Static Badge](https://img.shields.io/badge/scalar--check-blue)

* [CustomScalarInspection](#CustomScalarInspection)


<a name="scripted-actual"></a>![Static Badge](https://img.shields.io/badge/scripted--actual-blue)

* [ScriptedActualCircle](#ScriptedActualCircle)
* [ScriptedActualCone](#ScriptedActualCone)
* [ScriptedActualCurve](#ScriptedActualCurve)
* [ScriptedActualCylinder](#ScriptedActualCylinder)
* [ScriptedActualDistance](#ScriptedActualDistance)
* [ScriptedActualPoint](#ScriptedActualPoint)
* [ScriptedActualPointCloud](#ScriptedActualPointCloud)
* [ScriptedActualSection](#ScriptedActualSection)
* [ScriptedActualSurface](#ScriptedActualSurface)
* [ScriptedActualSurfaceCurve](#ScriptedActualSurfaceCurve)
* [ScriptedActualVolume](#ScriptedActualVolume)
* [ScriptedActualVolumeDefects](#ScriptedActualVolumeDefects)
* [ScriptedActualVolumeRegion](#ScriptedActualVolumeRegion)
* [ScriptedActualVolumeSection](#ScriptedActualVolumeSection)
* [TrimeshDeformMesh](#TrimeshDeformMesh)


<a name="scripted-check"></a>![Static Badge](https://img.shields.io/badge/scripted--check-blue)

* [ScriptedCurveCheck](#ScriptedCurveCheck)
* [ScriptedScalarCheck](#ScriptedScalarCheck)
* [ScriptedSurfaceCheck](#ScriptedSurfaceCheck)


<a name="scripted-diagrams"></a>![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)

* [OSMMapDiagram](#OSMMapDiagram)
* [ScriptedDiagramBasics](#ScriptedDiagramBasics)


<a name="section"></a>![Static Badge](https://img.shields.io/badge/section-blue)

* [CustomSection](#CustomSection)
* [ScriptedActualSection](#ScriptedActualSection)


<a name="selection-element-widget"></a>![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)

* [ExplorerSelectedElementsInDialog](#ExplorerSelectedElementsInDialog)


<a name="selection-list-widget"></a>![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)

* [DropdownWidget](#DropdownWidget)


<a name="service"></a>![Static Badge](https://img.shields.io/badge/service-blue)

* [ServiceExample](#ServiceExample)


<a name="settings"></a>![Static Badge](https://img.shields.io/badge/settings-blue)

* [OSMMapDiagram](#OSMMapDiagram)
* [ScriptedDiagramBasics](#ScriptedDiagramBasics)
* [SettingsAPI](#SettingsAPI)


<a name="sql-database"></a>![Static Badge](https://img.shields.io/badge/sql--database-blue)

* [SQLExample](#SQLExample)


<a name="surface"></a>![Static Badge](https://img.shields.io/badge/surface-blue)

* [CustomSurface](#CustomSurface)
* [ScriptedActualSurface](#ScriptedActualSurface)
* [ScriptedSurfaceCheck](#ScriptedSurfaceCheck)
* [TrimeshDeformMesh](#TrimeshDeformMesh)


<a name="surface-check"></a>![Static Badge](https://img.shields.io/badge/surface--check-blue)

* [CustomSurfaceInspection](#CustomSurfaceInspection)


<a name="surface-curve"></a>![Static Badge](https://img.shields.io/badge/surface--curve-blue)

* [CustomSurfaceCurve](#CustomSurfaceCurve)
* [ScriptedActualSurfaceCurve](#ScriptedActualSurfaceCurve)


<a name="testing"></a>![Static Badge](https://img.shields.io/badge/testing-blue)

* [PytestTemplate](#PytestTemplate)
* [TemplateUnittestCoverage](#TemplateUnittestCoverage)


<a name="unit-widget"></a>![Static Badge](https://img.shields.io/badge/unit--widget-blue)

* [UnitDialogEventHandler](#UnitDialogEventHandler)


<a name="value-element"></a>![Static Badge](https://img.shields.io/badge/value--element-blue)

* [CustomValueElement](#CustomValueElement)


<a name="volume"></a>![Static Badge](https://img.shields.io/badge/volume-blue)

* [CustomVolume](#CustomVolume)
* [ScriptedActualVolume](#ScriptedActualVolume)


<a name="volume-defects"></a>![Static Badge](https://img.shields.io/badge/volume--defects-blue)

* [CustomVolumeDefects](#CustomVolumeDefects)
* [ScriptedActualVolumeDefects](#ScriptedActualVolumeDefects)


<a name="volume-defects-2d"></a>![Static Badge](https://img.shields.io/badge/volume--defects--2d-blue)

* [CustomVolumeDefects2d](#CustomVolumeDefects2d)


<a name="volume-region"></a>![Static Badge](https://img.shields.io/badge/volume--region-blue)

* [CustomVolumeRegion](#CustomVolumeRegion)
* [ScriptedActualVolumeRegion](#ScriptedActualVolumeRegion)


<a name="volume-section"></a>![Static Badge](https://img.shields.io/badge/volume--section-blue)

* [CustomVolumeSection](#CustomVolumeSection)
* [ScriptedActualVolumeSection](#ScriptedActualVolumeSection)


<a name="volume-segmentation"></a>![Static Badge](https://img.shields.io/badge/volume--segmentation-blue)

* [CustomVolumeSegmentation](#CustomVolumeSegmentation)


<a name="widget-properties"></a>![Static Badge](https://img.shields.io/badge/widget--properties-blue)

* [WidgetVisibility](#WidgetVisibility)


<a name="windows"></a>![Static Badge](https://img.shields.io/badge/windows-blue)

* [Pywin32Example](#Pywin32Example)


<a name="workflow-assistant"></a>![Static Badge](https://img.shields.io/badge/workflow--assistant-blue)

* [WorkflowAssistants](#WorkflowAssistants)


<a name="workspace"></a>![Static Badge](https://img.shields.io/badge/workspace-blue)

* [WorkflowAssistants](#WorkflowAssistants)
* [Workspace](#Workspace)


<a name="xray"></a>![Static Badge](https://img.shields.io/badge/xray-blue)

* [CustomVolume](#CustomVolume)
* [CustomVolumeDefects](#CustomVolumeDefects)
* [CustomVolumeDefects2d](#CustomVolumeDefects2d)
* [CustomVolumeRegion](#CustomVolumeRegion)
* [CustomVolumeSection](#CustomVolumeSection)
* [CustomVolumeSegmentation](#CustomVolumeSegmentation)
* [ScriptedActualVolume](#ScriptedActualVolume)
* [ScriptedActualVolumeDefects](#ScriptedActualVolumeDefects)
* [ScriptedActualVolumeRegion](#ScriptedActualVolumeRegion)
* [ScriptedActualVolumeSection](#ScriptedActualVolumeSection)


## Related

* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeiss.github.io/zeiss-inspect-app-api/main/index.html)
* [ZEISS Quality Software Store](https://software-store.zeiss.com)

