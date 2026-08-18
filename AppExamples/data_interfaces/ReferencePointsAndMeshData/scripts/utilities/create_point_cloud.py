# -*- coding: utf-8 -*-
#
# create_point_cloud.py
#
# Example for creating a scripted point cloud element
#
# See https://zeissiqs.github.io/zeiss-inspect-addon-api/2023/python_api/scripted_elements_api.html#point-cloud
#
# Carl Zeiss GOM Metrology GmbH, 2023
#
# This script is part of the "Python API Examples" Add-on. For documentation, see:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2023/python_examples/
# ---

import gom


# -------------------------------------------------------------------------
def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {'points': params['points']}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
