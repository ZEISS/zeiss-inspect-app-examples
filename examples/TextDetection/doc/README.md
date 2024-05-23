# Text detection in images

This example demonstrates how external libraries can be used to detect and extract text fragments in images. It uses the Tesseract library for that purpose. The resulting element will be a "scripted element" which 
integrated nealty into a ZEISS inspect project and can be edited, recalculated or checked.

## Preliminaries

The following python wheels must be added to the add-on and are not included due to copyright reasons:

* numpy
* opencv_python
* pytesseract

In addition, the tesseract executable must be installed and the path to that executable must be adapted in the script.

## Example

![Software](text_detection.png)