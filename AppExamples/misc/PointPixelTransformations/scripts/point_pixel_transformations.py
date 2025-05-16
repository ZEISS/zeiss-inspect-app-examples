# -*- coding: utf-8 -*-
#
# point_pixel_transformations.py
#
# Example for computing 2D image pixel coordinates from 3D point coordinates and vice versa
#
# Terminology:
# ‘point’: 3D coordinate in the project
# ‘pixel’: 2D coordinate in an image
#
# 1) Get 2D image pixel coordinates of 3D point coordinates
# 2) Get 3D point coordinates of 2D image pixel coordinates
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import gom.api.project
from ExampleProjects.setup_project import open_project

if __name__ == '__main__':
    open_project('zeiss_part_test_measurement')
    MEASUREMENT_SERIES = gom.app.project.measurement_series[0].name
    MEASUREMENT = gom.app.project.measurement_series[MEASUREMENT_SERIES].measurements[0].name

    print(f'Measurement Series: {MEASUREMENT_SERIES}')
    print(f'Measurement       : {MEASUREMENT}')
    print('\n')

    #################################################################################################
    #
    # 1) Get 2D image pixel coordinates of 3D point coordinates
    #
    # See https://zeiss.github.io/zeiss-inspect-app-api/2023/python_api/python_api.html#gom-api-imaging-compute-pixels-from-point
    #
    #################################################################################################

    print("1) Computing 2D image pixel coordinates of 3D point coordinates")
    measurement = gom.app.project.measurement_series[MEASUREMENT_SERIES].measurements[MEASUREMENT]
    stage_index = 0

    # Using the first valid reference point in the selected measurement as the point example
    for index, id in enumerate(measurement.reference_point_id):
        if id is not None:
            break

    reference_point = measurement.reference_point_coordinate[index]
    print(f'\tFirst reference point in {MEASUREMENT_SERIES} - {MEASUREMENT}: ID = {id}, P = {reference_point})')

    left = gom.api.project.get_image_acquisition(measurement, 'left camera', [stage_index])[0]
    right = gom.api.project.get_image_acquisition(measurement, 'right camera', [stage_index])[0]

    image_coordinates = gom.api.imaging.compute_pixels_from_point([(reference_point, left), (reference_point, right)])
    print(f'\tImage coordinates of reference point (left, right): {image_coordinates}\n')

    ##################################################################################################
    #
    # 2) Get 3D point coordinates of 2D image pixel coordinates
    #
    # https://zeiss.github.io/zeiss-inspect-app-api/2023/python_api/python_api.html#gom-api-imaging-compute-point-from-pixels
    #
    ##################################################################################################

    print("2) 3D point coordinates of 2D image pixel coordinates - inverse of 1)")

    # Measurement as in step 1)
    # Left/right image acquisition as in step 1)
    # Image coordinates as computed in step 1)
    print(f'\tLeft image: {image_coordinates[0]}, Right image: {image_coordinates[1]}')
    use_calibration = False
    point_and_residuum = gom.api.imaging.compute_point_from_pixels(
        [[(image_coordinates[0], left), (image_coordinates[1], right)]], use_calibration)[0]
    print(f'\tComputation result: P = {point_and_residuum[0]}, Residuum: {point_and_residuum[1]}')
