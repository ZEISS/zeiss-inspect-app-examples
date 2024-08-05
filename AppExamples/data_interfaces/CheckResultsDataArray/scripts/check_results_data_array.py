# -*- coding: utf-8 -*-
#
# check_results_data_array.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np
from ExampleProjects.setup_project import open_project


# Getting a single value using the expression 'result_dimension[0].deviation'
# This would be very slow if you iterate through all values (e.g. with a for-loop)
def get_single_result_value(element):
    # -------------------------------------------------------------------------
    single_scalar_value = element.get('result_dimension[0].deviation')
    # -------------------------------------------------------------------------
    return single_scalar_value

# But, you can get the whole data as a numpy array
# The shape of the array is (stages, number of values, dimension=1)


def get_result_values_array(element):
    # -------------------------------------------------------------------------
    scalars = np.array(element.data.result_dimension.deviation)
    # -------------------------------------------------------------------------
    return scalars


#
# Example execution
#
if __name__ == '__main__':
    open_project('zeiss_part_test_project')
    example_element = gom.app.project.inspection['Surface comparison 1']

    single_result_value = get_single_result_value(example_element)
    result_array = get_result_values_array(example_element)

    print("Single deviation value: ", single_result_value)
    print("Array of deviation values (", result_array.shape, ", dtype=", result_array.dtype, ")")
    print(result_array)
