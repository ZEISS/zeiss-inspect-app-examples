# ZEISS INSPECT App Examples Overview

## data_interfaces &mdash; How to access data of ZEISS INSPECT elements

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="CheckResultsDataArray">CheckResultsDataArray</a><br>[view](data_interfaces/CheckResultsDataArray/doc/Documentation.md)  | This example demonstrates two ways of accessing result data from checks using the element properties and data interfaces. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/python_api_introduction.html#access-element-properties)<br> | [![Static Badge](https://img.shields.io/badge/element--properties-blue)](#element-properties)<br>[![Static Badge](https://img.shields.io/badge/element--data-blue)](#element-data)<br> |
| <a id="ReferencePointsAndMeshData">ReferencePointsAndMeshData</a><br>[view](data_interfaces/ReferencePointsAndMeshData/doc/Documentation.md)  | This example demonstrates how to access the reference points in a measurement and the mesh from Python. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)<br> | [![Static Badge](https://img.shields.io/badge/reference--points-blue)](#reference-points)<br>[![Static Badge](https://img.shields.io/badge/mesh-blue)](#mesh)<br>[![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="VolumeSectionImageData">VolumeSectionImageData</a><br>[view](data_interfaces/VolumeSectionImageData/doc/Documentation.md)  | This example demonstrates how to access the image data of a volume section. | [3)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)<br> | [![Static Badge](https://img.shields.io/badge/element--data-blue)](#element-data)<br> |

## dialog_widgets &mdash; How to use custom dialogs and handle user input events

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="DropdownWidget">DropdownWidget</a><br>[view](dialog_widgets/DropdownWidget/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/dropdown-widget) | This basic example shows how to use the dropdown widget and how to define items at script runtime. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-list-widget)<br> | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)](#selection-list-widget)<br> |
| <a id="ExplorerSelectedElementsInDialog">ExplorerSelectedElementsInDialog</a><br>[view](dialog_widgets/ExplorerSelectedElementsInDialog/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/explorer-selected-elements-in-dialog) | This example shows how to get a list of elements selected in the element explorer and use it in a script dialog.  | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-element-widget)<br> | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)](#selection-element-widget)<br> |
| <a id="UnitDialogEventHandler">UnitDialogEventHandler</a><br>[view](dialog_widgets/UnitDialogEventHandler/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/unit-dialog-event-handler) | This basic example demonstrates how to use an event handler on a script dialog to set the unit to multiple widgets. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#unit-widget)<br> | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/unit--widget-blue)](#unit-widget)<br> |
| <a id="WidgetVisibility">WidgetVisibility</a><br>[view](dialog_widgets/WidgetVisibility/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/widget-visibility) | This example shows how to use a dialog event handler to turn on/off widget visibilities. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html)<br> | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br>[![Static Badge](https://img.shields.io/badge/widget--properties-blue)](#widget-properties)<br> |

## misc &mdash; Miscellaneous

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="CSVExample">CSVExample</a><br>[view](misc/CSVExample/doc/Documentation.md)  | This example demonstrates how to read and write CSV files (comma separated values) from an App. | [1)](#example-projects)  |  | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br>[![Static Badge](https://img.shields.io/badge/export-blue)](#export)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="DialogReopenExample">DialogReopenExample</a><br>[view](misc/DialogReopenExample/doc/Documentation.md)  | This examples demonstrates, how a dialog can be closed from its own handler, just to be opened again. | | [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#executing-dialogs)<br> | [![Static Badge](https://img.shields.io/badge/dialog-blue)](#dialog)<br> |
| <a id="DisplayImage">DisplayImage</a><br>[view](misc/DisplayImage/doc/Documentation.md)  | Display measurement as a single image | |  | [![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br>[![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="ExcelExample">ExcelExample</a><br>[view](misc/ExcelExample/doc/Documentation.md)  | Example for reading and writing Excel files from an App | |  | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br>[![Static Badge](https://img.shields.io/badge/export-blue)](#export)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="FileSelectionAndFiltering">FileSelectionAndFiltering</a><br>[view](misc/FileSelectionAndFiltering/doc/Documentation.md)  | File Selection and Filtering Examples | |  | [![Static Badge](https://img.shields.io/badge/file-blue)](#file)<br>[![Static Badge](https://img.shields.io/badge/directory-blue)](#directory)<br>[![Static Badge](https://img.shields.io/badge/folder-blue)](#folder)<br>[![Static Badge](https://img.shields.io/badge/path-blue)](#path)<br> |
| <a id="IPCWebsocketExample">IPCWebsocketExample</a><br>[view](misc/IPCWebsocketExample/doc/Documentation.md)  | Example for triggering command execution via WebSocket protocol | |  | [![Static Badge](https://img.shields.io/badge/import-blue)](#import)<br> |
| <a id="MeasurementSystemAnalysis">MeasurementSystemAnalysis</a><br>[view](misc/MeasurementSystemAnalysis/doc/Documentation.md)  | MSA conformal measurement system analysis (ANOVA, ARM) | |  | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br> |
| <a id="PointPixelTransformations">PointPixelTransformations</a><br>[view](misc/PointPixelTransformations/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/point-pixel-transformations) | This example demonstrates how to find the 2D pixel coordinates of a 3D point coordinate and vice versa. | [2)](#example-projects)  | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-imaging)<br> | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br>[![Static Badge](https://img.shields.io/badge/reference--points-blue)](#reference-points)<br> |
| <a id="ProgressBar">ProgressBar</a><br>[view](misc/ProgressBar/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/progress-bar) | This example shows how to display a progress bar at the bottom of the ZEISS INSPECT main window | |  |  |
| <a id="SQLExample">SQLExample</a><br>[view](misc/SQLExample/doc/Documentation.md)  | Example for SQL Database Access | |  | [![Static Badge](https://img.shields.io/badge/sql--database-blue)](#sql-database)<br>[![Static Badge](https://img.shields.io/badge/project--keywords-blue)](#project-keywords)<br> |
| <a id="ServiceExample">ServiceExample</a><br>[view](misc/ServiceExample/doc/Documentation.md)  | Service API Example | | [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/using_services/using_services.html)<br>[API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-services)<br> | [![Static Badge](https://img.shields.io/badge/service-blue)](#service)<br> |
| <a id="SettingsAPI">SettingsAPI</a><br>[view](misc/SettingsAPI/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/settings-a-p-i) | Example App demonstrating usage of the settings API | | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-settings)<br> | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br> |
| <a id="TemplateUnittestCoverage">TemplateUnittestCoverage</a><br>[view](misc/TemplateUnittestCoverage/doc/Documentation.md)  | App template for running unit testing and generating a test coverage report | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html)<br> | [![Static Badge](https://img.shields.io/badge/testing-blue)](#testing)<br> |
| <a id="TextDetection">TextDetection</a><br>[view](misc/TextDetection/doc/Documentation.md)  | Text detection example | |  | [![Static Badge](https://img.shields.io/badge/measurement-blue)](#measurement)<br>[![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br> |

## projects &mdash; ZEISS INSPECT projects

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="ExampleProjects">ExampleProjects</a><br>[view](projects/ExampleProjects/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/example-projects) | ZEISS INSPECT Example Projects | |  | [![Static Badge](https://img.shields.io/badge/project-blue)](#project)<br> |

## script_icons &mdash; How to set icons for scripts or buttons

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="ScriptIcon">ScriptIcon</a><br>[view](script_icons/ScriptIcon/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/script-icon) | This example shows how an icon can be set to a script, whereas the icon itself resides in the App as a resource. | |  | [![Static Badge](https://img.shields.io/badge/menu-blue)](#menu)<br> |

## script_resources &mdash; How to access binary data of your App (resources)

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="ResourceAccess">ResourceAccess</a><br>[view](script_resources/ResourceAccess/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/resource-access) | Accessing an image as an App based resources | | [API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/resource_api.html)<br> | [![Static Badge](https://img.shields.io/badge/resources-blue)](#resources)<br>[![Static Badge](https://img.shields.io/badge/image--widget-blue)](#image-widget)<br> |
| <a id="ScriptResources">ScriptResources</a><br>[view](script_resources/ScriptResources/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/script-resources) | A simple example showing the usage of script resources. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/using_script_resources.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/resource_api.html)<br> | [![Static Badge](https://img.shields.io/badge/resources-blue)](#resources)<br> |

## scripted_actuals &mdash; Building custom actual elements with Python code

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="ScriptedActualCircle">ScriptedActualCircle</a><br>[view](scripted_actuals/ScriptedActualCircle/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-circle) | This is an example for a scripted actual 'circle' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#circle)<br> | [![Static Badge](https://img.shields.io/badge/circle-blue)](#circle)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCone">ScriptedActualCone</a><br>[view](scripted_actuals/ScriptedActualCone/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-cone) | This is an example for a scripted actual 'cone' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#cone)<br> | [![Static Badge](https://img.shields.io/badge/cone-blue)](#cone)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCurve">ScriptedActualCurve</a><br>[view](scripted_actuals/ScriptedActualCurve/doc/Documentation.md)  | This is an example for a scripted actual 'curve' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#curve)<br> | [![Static Badge](https://img.shields.io/badge/curve-blue)](#curve)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualCylinder">ScriptedActualCylinder</a><br>[view](scripted_actuals/ScriptedActualCylinder/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-cylinder) | This is an example for a scripted actual 'cylinder' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#cylinder)<br> | [![Static Badge](https://img.shields.io/badge/cylinder-blue)](#cylinder)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualDistance">ScriptedActualDistance</a><br>[view](scripted_actuals/ScriptedActualDistance/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-actual-distance) | This is an example for a scripted actual 'distance' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#distance)<br> | [![Static Badge](https://img.shields.io/badge/distance-blue)](#distance)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualPoint">ScriptedActualPoint</a><br>[view](scripted_actuals/ScriptedActualPoint/doc/Documentation.md)  | These are two examples for scripted actual points, which serve as an introduction to the concept of scripted actual elements. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#point)<br> | [![Static Badge](https://img.shields.io/badge/point-blue)](#point)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualPointCloud">ScriptedActualPointCloud</a><br>[view](scripted_actuals/ScriptedActualPointCloud/doc/Documentation.md)  | This is an example for a scripted actual 'point cloud' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#point-cloud)<br> | [![Static Badge](https://img.shields.io/badge/point--cloud-blue)](#point-cloud)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSection">ScriptedActualSection</a><br>[view](scripted_actuals/ScriptedActualSection/doc/Documentation.md)  | This is an example for a scripted actual 'section' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#section)<br> | [![Static Badge](https://img.shields.io/badge/section-blue)](#section)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSurface">ScriptedActualSurface</a><br>[view](scripted_actuals/ScriptedActualSurface/doc/Documentation.md)  | This is an example for a scripted actual 'surface' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#surface)<br> | [![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualSurfaceCurve">ScriptedActualSurfaceCurve</a><br>[view](scripted_actuals/ScriptedActualSurfaceCurve/doc/Documentation.md)  | This is an example for a scripted actual 'surface curve' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#surface-curve)<br> | [![Static Badge](https://img.shields.io/badge/surface--curve-blue)](#surface-curve)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolume">ScriptedActualVolume</a><br>[view](scripted_actuals/ScriptedActualVolume/doc/Documentation.md)  | This is an example for a scripted actual 'volume' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#volume)<br> | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume-blue)](#volume)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeDefects">ScriptedActualVolumeDefects</a><br>[view](scripted_actuals/ScriptedActualVolumeDefects/doc/Documentation.md)  | This is an example for a scripted actual 'volume defects' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#volume-defects)<br> | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--defects-blue)](#volume-defects)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeRegion">ScriptedActualVolumeRegion</a><br>[view](scripted_actuals/ScriptedActualVolumeRegion/doc/Documentation.md)  | This is an example for a scripted actual 'volume region' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#volume-region)<br> | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--region-blue)](#volume-region)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedActualVolumeSection">ScriptedActualVolumeSection</a><br>[view](scripted_actuals/ScriptedActualVolumeSection/doc/Documentation.md)  | This is an example for a scripted actual 'volume section' element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#volume-section)<br> | [![Static Badge](https://img.shields.io/badge/xray-blue)](#xray)<br>[![Static Badge](https://img.shields.io/badge/volume--section-blue)](#volume-section)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |
| <a id="ScriptedElementProgress">ScriptedElementProgress</a><br>[view](scripted_actuals/ScriptedElementProgress/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-element-progress) | This examples demonstrates how to show progress information to the user while calcualting a scripted element. | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br> | [![Static Badge](https://img.shields.io/badge/computation--progress-blue)](#computation-progress)<br> |
| <a id="TrimeshDeformMesh">TrimeshDeformMesh</a><br>[view](scripted_actuals/TrimeshDeformMesh/doc/Documentation.md)  | This example demonstrates how to generate a custom surface element using a scripted element. The example script accesses mesh information from an existing mesh in the project and adds a random deformation to each point. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_actuals.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#surface)<br> | [![Static Badge](https://img.shields.io/badge/mesh-blue)](#mesh)<br>[![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br>[![Static Badge](https://img.shields.io/badge/scripted--actual-blue)](#scripted-actual)<br> |

## scripted_checks &mdash; Building custom checks with Python code

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="ScriptedCurveCheck">ScriptedCurveCheck</a><br>[view](scripted_checks/ScriptedCurveCheck/doc/Documentation.md)  | This example demonstrates how to create a scalar curve check by a script. Also, the usage of custom coordinate systems in scripted checks is shown. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#scalar-curve)<br> | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/curve-blue)](#curve)<br> |
| <a id="ScriptedScalarCheck">ScriptedScalarCheck</a><br>[view](scripted_checks/ScriptedScalarCheck/doc/Documentation.md)  / [download](https://software-store.zeiss.com/products/apps/scripted-scalar-check) | This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#scalar)<br> | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/scalar-blue)](#scalar)<br> |
| <a id="ScriptedSurfaceCheck">ScriptedSurfaceCheck</a><br>[view](scripted_checks/ScriptedSurfaceCheck/doc/Documentation.md)  | This example demonstrates how to create a scalar surface check by a script. Also, the usage of custom coordinate systems and element preview in scripted checks is shown. | [1)](#example-projects)  | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_checks.html)<br>[API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/scripted_elements_api.html#scalar-surface)<br> | [![Static Badge](https://img.shields.io/badge/scripted--check-blue)](#scripted-check)<br>[![Static Badge](https://img.shields.io/badge/surface-blue)](#surface)<br> |

## scripted_diagrams &mdash; Creating custom diagrams

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;App&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example Projects | References | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| --- | ----------- | ---------------- | ---------- | ---- |
| <a id="OSMMapDiagram">OSMMapDiagram</a><br>[view](scripted_diagrams/OSMMapDiagram/doc/Documentation.md)  | Display geolocation using a scripted diagram | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)<br> | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br>[![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)](#scripted-diagrams)<br> |
| <a id="ScriptedDiagramBasics">ScriptedDiagramBasics</a><br>[view](scripted_diagrams/ScriptedDiagramBasics/doc/Documentation.md)  | Scripted diagram basics | | [HowTo](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)<br> | [![Static Badge](https://img.shields.io/badge/settings-blue)](#settings)<br>[![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)](#scripted-diagrams)<br> |

## Example projects

| No. | Project name | Description |
| --- | ------------ | ----------- |
| 1 | zeiss_part_test_project | Simple optically measured part with a CAD, mesh and some basic inspections |
| 2 | zeiss_part_test_measurement | Optical measurement series and preliminary mesh of ZEISS part |
| 3 | volume_test_project | A small test volume for CT related inspections |

[Download Example Projects App](https://software-store.zeiss.com/products/apps/example-projects)

## Tag Index

### <a name="circle"></a>![Static Badge](https://img.shields.io/badge/circle-blue)

* [ScriptedActualCircle](#ScriptedActualCircle)


### <a name="computation-progress"></a>![Static Badge](https://img.shields.io/badge/computation--progress-blue)

* [ScriptedElementProgress](#ScriptedElementProgress)


### <a name="cone"></a>![Static Badge](https://img.shields.io/badge/cone-blue)

* [ScriptedActualCone](#ScriptedActualCone)


### <a name="curve"></a>![Static Badge](https://img.shields.io/badge/curve-blue)

* [ScriptedActualCurve](#ScriptedActualCurve)
* [ScriptedCurveCheck](#ScriptedCurveCheck)


### <a name="cylinder"></a>![Static Badge](https://img.shields.io/badge/cylinder-blue)

* [ScriptedActualCylinder](#ScriptedActualCylinder)


### <a name="dialog"></a>![Static Badge](https://img.shields.io/badge/dialog-blue)

* [DialogReopenExample](#DialogReopenExample)
* [DropdownWidget](#DropdownWidget)
* [ExplorerSelectedElementsInDialog](#ExplorerSelectedElementsInDialog)
* [UnitDialogEventHandler](#UnitDialogEventHandler)
* [WidgetVisibility](#WidgetVisibility)


### <a name="directory"></a>![Static Badge](https://img.shields.io/badge/directory-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


### <a name="distance"></a>![Static Badge](https://img.shields.io/badge/distance-blue)

* [ScriptedActualDistance](#ScriptedActualDistance)


### <a name="element-data"></a>![Static Badge](https://img.shields.io/badge/element--data-blue)

* [CheckResultsDataArray](#CheckResultsDataArray)
* [VolumeSectionImageData](#VolumeSectionImageData)


### <a name="element-properties"></a>![Static Badge](https://img.shields.io/badge/element--properties-blue)

* [CheckResultsDataArray](#CheckResultsDataArray)


### <a name="export"></a>![Static Badge](https://img.shields.io/badge/export-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)


### <a name="file"></a>![Static Badge](https://img.shields.io/badge/file-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


### <a name="folder"></a>![Static Badge](https://img.shields.io/badge/folder-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


### <a name="image-widget"></a>![Static Badge](https://img.shields.io/badge/image--widget-blue)

* [DisplayImage](#DisplayImage)
* [ResourceAccess](#ResourceAccess)
* [TextDetection](#TextDetection)


### <a name="import"></a>![Static Badge](https://img.shields.io/badge/import-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)
* [IPCWebsocketExample](#IPCWebsocketExample)


### <a name="measurement"></a>![Static Badge](https://img.shields.io/badge/measurement-blue)

* [DisplayImage](#DisplayImage)
* [MeasurementSystemAnalysis](#MeasurementSystemAnalysis)
* [PointPixelTransformations](#PointPixelTransformations)
* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)
* [TextDetection](#TextDetection)


### <a name="menu"></a>![Static Badge](https://img.shields.io/badge/menu-blue)

* [ScriptIcon](#ScriptIcon)


### <a name="mesh"></a>![Static Badge](https://img.shields.io/badge/mesh-blue)

* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)
* [TrimeshDeformMesh](#TrimeshDeformMesh)


### <a name="path"></a>![Static Badge](https://img.shields.io/badge/path-blue)

* [FileSelectionAndFiltering](#FileSelectionAndFiltering)


### <a name="point"></a>![Static Badge](https://img.shields.io/badge/point-blue)

* [ScriptedActualPoint](#ScriptedActualPoint)


### <a name="point-cloud"></a>![Static Badge](https://img.shields.io/badge/point--cloud-blue)

* [ScriptedActualPointCloud](#ScriptedActualPointCloud)


### <a name="project"></a>![Static Badge](https://img.shields.io/badge/project-blue)

* [ExampleProjects](#ExampleProjects)


### <a name="project-keywords"></a>![Static Badge](https://img.shields.io/badge/project--keywords-blue)

* [CSVExample](#CSVExample)
* [ExcelExample](#ExcelExample)
* [SQLExample](#SQLExample)


### <a name="reference-points"></a>![Static Badge](https://img.shields.io/badge/reference--points-blue)

* [PointPixelTransformations](#PointPixelTransformations)
* [ReferencePointsAndMeshData](#ReferencePointsAndMeshData)


### <a name="resources"></a>![Static Badge](https://img.shields.io/badge/resources-blue)

* [ResourceAccess](#ResourceAccess)
* [ScriptResources](#ScriptResources)


### <a name="scalar"></a>![Static Badge](https://img.shields.io/badge/scalar-blue)

* [ScriptedScalarCheck](#ScriptedScalarCheck)


### <a name="scripted-actual"></a>![Static Badge](https://img.shields.io/badge/scripted--actual-blue)

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


### <a name="scripted-check"></a>![Static Badge](https://img.shields.io/badge/scripted--check-blue)

* [ScriptedCurveCheck](#ScriptedCurveCheck)
* [ScriptedScalarCheck](#ScriptedScalarCheck)
* [ScriptedSurfaceCheck](#ScriptedSurfaceCheck)


### <a name="scripted-diagrams"></a>![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)

* [OSMMapDiagram](#OSMMapDiagram)
* [ScriptedDiagramBasics](#ScriptedDiagramBasics)


### <a name="section"></a>![Static Badge](https://img.shields.io/badge/section-blue)

* [ScriptedActualSection](#ScriptedActualSection)


### <a name="selection-element-widget"></a>![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)

* [ExplorerSelectedElementsInDialog](#ExplorerSelectedElementsInDialog)


### <a name="selection-list-widget"></a>![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)

* [DropdownWidget](#DropdownWidget)


### <a name="service"></a>![Static Badge](https://img.shields.io/badge/service-blue)

* [ServiceExample](#ServiceExample)


### <a name="settings"></a>![Static Badge](https://img.shields.io/badge/settings-blue)

* [OSMMapDiagram](#OSMMapDiagram)
* [ScriptedDiagramBasics](#ScriptedDiagramBasics)
* [SettingsAPI](#SettingsAPI)


### <a name="sql-database"></a>![Static Badge](https://img.shields.io/badge/sql--database-blue)

* [SQLExample](#SQLExample)


### <a name="surface"></a>![Static Badge](https://img.shields.io/badge/surface-blue)

* [ScriptedActualSurface](#ScriptedActualSurface)
* [ScriptedSurfaceCheck](#ScriptedSurfaceCheck)
* [TrimeshDeformMesh](#TrimeshDeformMesh)


### <a name="surface-curve"></a>![Static Badge](https://img.shields.io/badge/surface--curve-blue)

* [ScriptedActualSurfaceCurve](#ScriptedActualSurfaceCurve)


### <a name="testing"></a>![Static Badge](https://img.shields.io/badge/testing-blue)

* [TemplateUnittestCoverage](#TemplateUnittestCoverage)


### <a name="unit-widget"></a>![Static Badge](https://img.shields.io/badge/unit--widget-blue)

* [UnitDialogEventHandler](#UnitDialogEventHandler)


### <a name="volume"></a>![Static Badge](https://img.shields.io/badge/volume-blue)

* [ScriptedActualVolume](#ScriptedActualVolume)


### <a name="volume-defects"></a>![Static Badge](https://img.shields.io/badge/volume--defects-blue)

* [ScriptedActualVolumeDefects](#ScriptedActualVolumeDefects)


### <a name="volume-region"></a>![Static Badge](https://img.shields.io/badge/volume--region-blue)

* [ScriptedActualVolumeRegion](#ScriptedActualVolumeRegion)


### <a name="volume-section"></a>![Static Badge](https://img.shields.io/badge/volume--section-blue)

* [ScriptedActualVolumeSection](#ScriptedActualVolumeSection)


### <a name="widget-properties"></a>![Static Badge](https://img.shields.io/badge/widget--properties-blue)

* [WidgetVisibility](#WidgetVisibility)


### <a name="xray"></a>![Static Badge](https://img.shields.io/badge/xray-blue)

* [ScriptedActualVolume](#ScriptedActualVolume)
* [ScriptedActualVolumeDefects](#ScriptedActualVolumeDefects)
* [ScriptedActualVolumeRegion](#ScriptedActualVolumeRegion)
* [ScriptedActualVolumeSection](#ScriptedActualVolumeSection)


## Related

* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html)
* [ZEISS Quality Software Store](https://software-store.zeiss.com)

