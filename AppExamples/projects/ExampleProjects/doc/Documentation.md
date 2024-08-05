## ExampleProjects

Most of the App examples rely on a certain ZEISS INSPECT project file to be loaded. Some examples load the projects automatically when it is possible (E.g. in the `if __name__ == '__main__'` block) while other example require the project to be loaded manually. This is easily done using the `setup_project.py` script.

The project files are stored in this App to avoid duplication across multiple Apps.

The following project files are included:

| Project name                | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| zeiss_part_test_project     | Simple optically measured part with a CAD, mesh and some basic inspection |
| volume_test_part            | A small test volume for CT related inspections                            |
| zeiss_part_test_measurement | Optical measurement series and preliminary mesh of ZEISS part             |