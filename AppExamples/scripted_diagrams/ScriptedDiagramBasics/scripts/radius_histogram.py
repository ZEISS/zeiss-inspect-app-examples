# -*- coding: utf-8 -*-
#
# radius_histogram.py
#
# Service function which receives the radii of all elements and generates a histogram
# Diagram settings are available in Preferences->App-Settings->ScriptedDiagramBasics
# See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---
"""Scripted diagram service creating a radius histogram"""

import gom
import gom.api.settings

from gom import apifunction

import matplotlib.pyplot as plt
import gom.api.extensions.diagrams.matplotlib_tools as mpltools

@apifunction
def radius_histogram(view, element_data)->str:
    """
    Plot radius histogram
    """
    gom.log.info('Radius Histogram Service')
    gom.log.info(f'{view=}, {element_data=}')

    bins = gom.api.settings.get('bins')
    bins = [int(elem) for elem in bins.split(',') if elem.strip().isnumeric()]

    mpltools.setup_plot (plt, view)

    radius = []

    for e in element_data:
        data = e['data']

        radius.append(data['ude_diagram_radius'])

    color =  gom.api.settings.get('barcolor')

    # Creating the histogram plot
    nbins, bins, _ = plt.hist(radius, bins=bins, color = color, rwidth=0.5)
    gom.log.debug(f'{nbins=},{bins=}')
    plt.title(gom.api.settings.get('title'))
    plt.xlabel(gom.api.settings.get('xlabel'))
    plt.ylabel(gom.api.settings.get('ylabel'))

    # Create customized x-ticks
    xticks = []
    xlabels = []
    for i in range(len(nbins)):
        xticks.append((bins[i] + bins[i+1])/2)
        if i < len(nbins)-1:
            # All but last bin:
            # Interval [n, n+1)
            xlabels.append(f'[{bins[i]},{bins[i+1]})')
        else:
            # Last bin:
            # Interval [n, n+1]
            xlabels.append(f'[{bins[i]},{bins[i+1]}]')
    plt.xticks(xticks, xlabels)

    return mpltools.create_svg (plt, view)

gom.run_api()
