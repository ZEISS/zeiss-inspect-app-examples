# -*- coding: utf-8 -*-
#
# reference_points_and_mesh_data.py
#
# Example for handling numpy data structures from ZEISS INSPECT elements in Python
#
# 1) Read reference points and create a Point Cloud element from it
# 2) Read part points and create a Point Cloud element from it
# 3) Read part points and create a Surface element from it
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import numpy as np
from ExampleProjects.setup_project import open_project

#
# Example execution
#
if __name__ == '__main__':
    open_project('zeiss_part_test_measurement')
    MEASUREMENT_SERIES = gom.app.project.measurement_series[0].name
    MEASUREMENT = gom.app.project.measurement_series[MEASUREMENT_SERIES].measurements[0].name
    PART = gom.app.project.parts[0].name
    GENERATE_ELEMENTS = True  # Set to 'False' to skip some time-consuming computations

    print(f'Measurement Series: {MEASUREMENT_SERIES}')
    print(f'Measurement       : {MEASUREMENT}')
    print(f'Part              : {PART}')

    # Remove previously generated elements
    element_names = {
        'reference_points': 'Reference Points',
        'part_points': 'Part Points',
        'part_surface': 'Part Surface',
        'shifted_part_surface': 'Shifted Part Surface'
    }

    elements = [i.get('name') for i in gom.ElementSelection(
        {'category': ['key', 'elements', 'part', gom.app.project.parts[PART], 'explorer_category', 'actual']})]

    for element in element_names:
        if element_names[element] in elements:
            gom.script.cad.delete_element(
                elements=[gom.app.project.actual_elements[element_names[element]]],
                with_measuring_principle=True)

    #################################################################################################
    #
    # 1) Read reference points and create a Point Cloud element from it
    #
    #################################################################################################

    # Reference points
    # Shape: e.g. (1, 44, 3)
    # Indices:
    # 0 - stage
    # 1 - points
    # 2 - coordinates
    reference_points = np.array(
        gom.app.project.measurement_series[MEASUREMENT_SERIES].results['points'].data.coordinate)

    if GENERATE_ELEMENTS:
        print("1) Generating point cloud from reference points...", end="")
        create_point_cloud = gom.script.sys.create_element_by_script(
            check_type='none',
            element_type='point_cloud',
            name=element_names['reference_points'],
            parameters={
                'points': reference_points[0].tolist()
            },
            script_uuid='ff73513a-e857-43da-b4d2-382f80f25c28'
        )
        print(" done.")

    # Image data - list of RGB values
    # To display it, see https://github.com/ZeissIQS/AddOnExamples/tree/main (DisplayImage)
    # image_left = gom.app.project.measurement_series['Scan 1'].measurements['M1'].images['left camera'].data.rgb

    #################################################################################################
    #
    # 2) Read part points and create a Point Cloud element from it
    #
    #################################################################################################

    # Part points
    # Shape: e.g. (1, 876397, 3)
    # 0 - stage
    # 1 - points
    # 2 - coordinates
    part_points = np.array(gom.app.project.parts[PART].actual.data.coordinate)
    # print(np.shape(part_points))
    # print(part_points)

    if GENERATE_ELEMENTS:
        print("2) Generating point cloud from part points...", end="")
        create_point_cloud = gom.script.sys.create_element_by_script(
            check_type='none',
            element_type='point_cloud',
            name=element_names['part_points'],
            parameters={
                'points': part_points[0].tolist()
            },
            script_uuid='ff73513a-e857-43da-b4d2-382f80f25c28'
        )
        print(" done.")

    #################################################################################################
    #
    # 3) Read part points and create a Surface element from it
    #
    #################################################################################################

    # Part triangles
    # Shape: e.g. (1, 1591204, 3)
    # 0 - stage
    # 1 - triangles
    # 3 - indices into list of points
    part_triangles = np.array(gom.app.project.parts[PART].actual.data.triangle)
    # print(np.shape(part_triangles))
    # print(part_triangles)

    shifted_part_points = part_points.copy()
    shifted_part_points[0, :, 2] += 200

    if GENERATE_ELEMENTS:
        print("3) Generating surface from part (shifted in Z direction)...", end="")
        create_surface = gom.script.sys.create_element_by_script(
            check_type='none',
            element_type='surface',
            name=element_names['shifted_part_surface'],
            parameters={
                'vertices': shifted_part_points[0].tolist(),
                'triangles': part_triangles[0].tolist()
            },
            script_uuid='af863fa6-27d6-44d9-bba3-636eb09119fa'
        )
        print(" done.")
