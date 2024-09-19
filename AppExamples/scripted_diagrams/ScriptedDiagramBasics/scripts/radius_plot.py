# -*- coding: utf-8 -*-
#
# radius_plot.py
#
# Service function which receives the radii of all elements and plots
# radius and element name.
# See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---
"""Scripted diagram service plotting radius / element name"""

import gom

from gom import apifunction

import matplotlib.pyplot as plt
import gom.api.extensions.diagrams.matplotlib_tools as mpltools

@apifunction
def radius_plot(view, element_data)->str:
    """
    Plot circle radius marks
    """
    gom.log.info('Radius Plot Service')
    gom.log.info(f'{view=}, {element_data=}')

    mpltools.setup_plot (plt, view)

    for e in element_data:
        element = e['element']
        data = e['data']

        plt.plot ([element.name], [data['ude_diagram_radius']], 'bx')


    plt.xticks(rotation = 90)

    return mpltools.create_svg (plt, view) 

gom.run_api()
