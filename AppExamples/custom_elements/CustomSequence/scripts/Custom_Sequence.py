"""
Example for a custom sequence element: Datum Plane from 3 Reference Points

This script implements a custom sequence element that creates a datum plane
through 3 user-defined reference points. The plane and its 3 reference points
form a sequence — moving one reference point individually automatically
re-fits the plane.

Sequence structure:
    - Leading element: Datum Plane (the plane defined by the 3 reference points)
    - Child elements:  Reference Point 1, Reference Point 2, Reference Point 3

Metrological context:
    Defining a datum plane from 3 reference points is a fundamental technique in
    dimensional metrology (ISO 5459). The 3 points determine an unambiguous plane
    orientation, which can serve as a datum reference frame for downstream
    inspections (distances, flatness, angularity, etc.).

API reference:
    https://zeiss.github.io/zeiss-inspect-app-api/main/python_api/python_api.html#gom-api-extensions-sequence-customsequence

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples    
"""

import gom
import gom.api.dialog
import gom.api.extensions.sequence

from gom import apicontribution


@apicontribution
class DatumPlaneSequence(gom.api.extensions.sequence.CustomSequence):
    """
    Custom sequence element: Datum Plane from 3 Reference Points.

    Creates three nominal reference points and a nominal plane through them.
    The reference points are registered as child elements of the plane;
    editing them individually triggers an automatic plane update via on_edited().
    """

    def __init__(self):
        super().__init__(
            id='examples.custom_sequence',
            description='Datum Plane from 3 Reference Points',
            properties={'edit_child_elements_separately': True}
        )

    @staticmethod
    def _validation_error(values):
        points = [
            tuple(float(values[f'p{point}_{axis}']) for axis in 'xyz')
            for point in (1, 2, 3)
        ]
        vector1 = tuple(points[1][i] - points[0][i] for i in range(3))
        vector2 = tuple(points[2][i] - points[0][i] for i in range(3))
        cross = (
            vector1[1] * vector2[2] - vector1[2] * vector2[1],
            vector1[2] * vector2[0] - vector1[0] * vector2[2],
            vector1[0] * vector2[1] - vector1[1] * vector2[0],
        )
        length = sum(component ** 2 for component in cross) ** 0.5
        if length < 1e-10:
            return 'The 3 reference points are collinear or identical and do not define a plane.'
        return ''

    def dialog(self, context, args):
        """Show the dialog with call-local validation feedback."""
        dlg = gom.api.dialog.create(context, '/Custom_Sequence.gdlg')
        self.initialize_dialog(context, dlg, args)

        def update_validation(_widget=None):
            values = {
                name: getattr(dlg, name).value
                for point in (1, 2, 3)
                for name in (f'p{point}_x', f'p{point}_y', f'p{point}_z')
            }
            error = self._validation_error(values)
            dlg.control.status = error
            dlg.control.ok.enabled = not error

        dlg.handler = update_validation
        update_validation()
        return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))

    def create(self, _context, name, args):
        """
        Create the sequence of elements.

        Called on first creation of the element. Returns a dict with:
        - 'elements': list of all created elements (child elements first,
                      then the leading element last)
        - 'leading':  the leading element (the datum plane)
        """
        # -----------------------------------------------------------------------
        # Ensure the base name is unique: if child or leading element names
        # already exist (e.g. from a previous partial creation or a second run),
        # find the next available numbered variant.
        # -----------------------------------------------------------------------
        existing_names = {str(e.name) for e in gom.app.project.nominal_elements}
        unique_name = name
        suffix = 1
        while (unique_name in existing_names or
               str(self.generate_element_name(unique_name, 'Reference Point 1')) in existing_names):
            suffix += 1
            unique_name = f"{name} ({suffix})"
        name = unique_name

        # -----------------------------------------------------------------------
        # Create the three nominal reference points
        # -----------------------------------------------------------------------
        POINT_1 = gom.script.primitive.create_point(
            name=self.generate_element_name(name, 'Reference Point 1'),
            point={'point': gom.Vec3d(float(args['p1_x']), float(args['p1_y']), float(args['p1_z']))}
        )
        POINT_2 = gom.script.primitive.create_point(
            name=self.generate_element_name(name, 'Reference Point 2'),
            point={'point': gom.Vec3d(float(args['p2_x']), float(args['p2_y']), float(args['p2_z']))}
        )
        POINT_3 = gom.script.primitive.create_point(
            name=self.generate_element_name(name, 'Reference Point 3'),
            point={'point': gom.Vec3d(float(args['p3_x']), float(args['p3_y']), float(args['p3_z']))}
        )

        # -----------------------------------------------------------------------
        # Create the datum plane through the 3 reference points (leading element)
        # -----------------------------------------------------------------------
        PLANE = gom.script.primitive.create_plane_by_3_points(
            name=name,
            point1=POINT_1,
            point2=POINT_2,
            point3=POINT_3
        )

        return {'elements': [POINT_1, POINT_2, POINT_3, PLANE], 'leading': PLANE}

    def edit(self, _context, elements, args):
        """
        Update the sequence when it is re-opened via the edit dialog.

        Called after the user closes the dialog while editing the whole sequence.
        Receives the current element objects and the new dialog values (args).
        """
        POINT_1, POINT_2, POINT_3, _ = elements

        gom.script.sys.edit_creation_parameters(
            element=POINT_1,
            point={'point': gom.Vec3d(float(args['p1_x']), float(args['p1_y']), float(args['p1_z']))}
        )
        gom.script.sys.edit_creation_parameters(
            element=POINT_2,
            point={'point': gom.Vec3d(float(args['p2_x']), float(args['p2_y']), float(args['p2_z']))}
        )
        gom.script.sys.edit_creation_parameters(
            element=POINT_3,
            point={'point': gom.Vec3d(float(args['p3_x']), float(args['p3_y']), float(args['p3_z']))}
        )
        # The leading plane references these points and recomputes automatically.

    def on_edited(self, _context, args, parameters):
        """
        Synchronise the sequence dialog args when a child element is edited.

        Called when one of the child elements (reference points) is edited
        individually (i.e. with edit_child_elements_separately = True).
        The updated creation parameters of each element are passed in
        'parameters' in the same order as the 'elements' list returned by create():
        [POINT_1_PARAMS, POINT_2_PARAMS, POINT_3_PARAMS, PLANE_PARAMS]

        Returns the updated args so that re-opening the whole-sequence dialog
        shows the latest point coordinates.
        """
        POINT_1_PARAMS, POINT_2_PARAMS, POINT_3_PARAMS, _ = parameters

        # -----------------------------------------------------------------------
        # If a reference point was edited directly, reflect its new coordinates
        # back into the sequence args so the dialog stays consistent.
        # -----------------------------------------------------------------------
        if POINT_1_PARAMS:
            pos = POINT_1_PARAMS['point'].point
            args['p1_x'] = float(pos.x)
            args['p1_y'] = float(pos.y)
            args['p1_z'] = float(pos.z)

        if POINT_2_PARAMS:
            pos = POINT_2_PARAMS['point'].point
            args['p2_x'] = float(pos.x)
            args['p2_y'] = float(pos.y)
            args['p2_z'] = float(pos.z)

        if POINT_3_PARAMS:
            pos = POINT_3_PARAMS['point'].point
            args['p3_x'] = float(pos.x)
            args['p3_y'] = float(pos.y)
            args['p3_z'] = float(pos.z)

        return args


gom.run_api()
