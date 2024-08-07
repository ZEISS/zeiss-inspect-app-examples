# ZEISS INSPECT App Examples

This repository contains various [ZEISS INSPECT](https://www.zeiss.com/metrology/products/software.html#inspectionsolutions) App examples for educational and inspirational purposes.

> [!NOTE]
> Please have a look into the [ZEISS INSPECT App Development Documentation](https://zeissiqs.github.io/) for a general introduction to ZEISS INSPECT App development, a set of documented App examples and the API specification.

In principle, a ZEISS INSPECT App is just a zip'ped directory with a special structure, containing scripts, templates, definitions etc. necessary to add features to the ZEISS INSPECT software. The Apps listed here can be downloaded in compressed form via the ZEISS Quality Software Store in the [ZEISS Quality Suite](https://www.zeiss.com/metrology/products/software.html). Alternatively, for fiddling around with them, the App repository can be cloned, zip'ed and then dropped right into ZEISS INSPECT. Please see the documentation mentioned above for more details or consult the [ZEISS Quality Training Center](https://training.gom.com) for a general feature overview.

## Complete App examples

* Measurement System Analysis App: [MSA](examples/MeasurementSystemAnalysis) ([Download](https://software-store.zeiss.com/products/apps/measurement-system-analysis))

## App programming examples

* Access resources from within scripts: [ResourceAccess](examples/ResourceAccess)
* Display measurement data from a scan as an image in a user-defined dialog: [DisplayImage](examples/DisplayImage)
* Extract text from images (measurement data) and provide it as a scripted actual element: [TextDetection](examples/TextDetection)
* File selection and filtering: [FileSelectionAndFiltering](examples/FileSelectionAndFiltering)
* Save settings persistently using the `settings` API: [SettingsAPI](examples/SettingsAPI)
* Template for unit testing and generating a test coverage report: [TemplateUnittestCoverage](examples/TemplateUnittestCoverage)
