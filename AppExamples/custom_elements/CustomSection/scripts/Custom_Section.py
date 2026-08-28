"""
Custom nominal/actual Section Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals
import numpy as np
from numpy import linalg as la

from gom import apicontribution


def calc_section_length(verts):
    """Calculate the total length of a section (sum of Euclidean distances between adjacent vertices)."""
    length = 0.0
    for i in range(len(verts) - 1):
        length += la.norm(verts[i + 1] - verts[i])
    return length


def get_sub_sections(base_curve, stage=0):
    """Separate a section curve into sub-sections by checking if adjacent points are connected.

    Returns:
        List of (verts, normals) tuples, one per sub-section.
    """
    curve_coords = np.array(base_curve.data.coordinate)[stage]
    curve_normals = np.array(base_curve.data.normal)[stage]
    sub_sections = []
    start_index = 0
    for end_index, conn in enumerate(base_curve.scanline_point_connection):
        if conn != "connected":
            sub_sections.append((
                curve_coords[start_index:end_index + 1],
                curve_normals[start_index:end_index + 1]
            ))
            start_index = end_index + 1
    return sub_sections


def filter_by_length(sub_sections, mode):
    """Filter sub-sections by length and return the one matching the filter criterion."""
    max_len = 0
    min_len = 0
    r_min = None
    r_max = None
    for verts, normals in sub_sections:
        ssl = calc_section_length(verts)
        if max_len < ssl:
            max_len = ssl
            r_max = verts, normals
        if min_len == 0 or min_len > ssl:
            min_len = ssl
            r_min = verts, normals
    if mode.lower() == "max. length":
        return r_max, max_len
    else:
        return r_min, min_len


def _compute_section(values):
    """Compute filtered section data from dialog values."""
    base_curve = values['i_elem']
    mode = str(values['i_mode'])
    sub_sections = get_sub_sections(base_curve)
    (verts, normals), length = filter_by_length(sub_sections, mode)
    points = [tuple(float(x) for x in v) for v in verts]
    normals_list = [tuple(float(x) for x in n) for n in normals]
    return points, normals_list, len(verts), length


@apicontribution
class ActualSection(gom.api.extensions.actuals.Section):
    """
    Custom actual section element.

    Features:
    - Accepts an existing section element and a filter mode (Min. Length / Max. Length)
    - Splits the section into sub-sections by checking scanline point connectivity
    - Returns the sub-section matching the filter criterion
    - Stores num_points and section_length as custom element data tokens
    """

    def __init__(self):
        """Register the custom actual section contribution."""
        super().__init__(id='examples.custom_actual_section', description='Custom Actual Section')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Section.gdlg')

    def compute(self, _context, values):
        """Compute the actual section element."""
        # -------------------------------------------------------------------------
        points, normals, num_points, section_length = _compute_section(values)
        return {
            "curves": [{"points": points, "normals": normals}],
            "data": {"num_points": num_points, "section_length": float(section_length)}
        }
        # -------------------------------------------------------------------------


@apicontribution
class NominalSection(gom.api.extensions.nominals.Section):
    """
    Custom nominal section element.

    Features:
    - Accepts an existing section element and a filter mode (Min. Length / Max. Length)
    - Splits the section into sub-sections by checking scanline point connectivity
    - Returns the sub-section matching the filter criterion
    - Stores num_points and section_length as custom element data tokens
    """

    def __init__(self):
        """Register the custom nominal section contribution."""
        super().__init__(id='examples.custom_nominal_section', description='Custom Nominal Section')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Section.gdlg')

    def compute(self, _context, values):
        """Compute the nominal section element."""
        # -------------------------------------------------------------------------
        points, normals, num_points, section_length = _compute_section(values)
        return {
            "curves": [{"points": points, "normals": normals}],
            "data": {"num_points": num_points, "section_length": float(section_length)}
        }
        # -------------------------------------------------------------------------


gom.run_api()
