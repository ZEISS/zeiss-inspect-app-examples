# -*- coding: utf-8 -*-
#
# test_blackbox.py
#
# This test runs the Unit Under Test (UUT) as script and treats it as opaque. After running it, the ZEISS INSPECT project
# is checked for the expected changes of state (in this example: project keywords).
#
# Carl Zeiss GOM Metrology GmbH, 2024
# 
# ---

import gom
import os

def test_blackbox():
    '''Executing the UUT as the entire script'''

    # Add-on relative path to UUT
    uut_path = 'scripts/uut_project_keywords.py'

    # Get path of UUT
    addon = gom.api.addons.get_current_addon()
    uut_path = os.path.join(addon.get_file(), uut_path) 

    # Run the UUT
    gom.script.sys.execute_script(file=uut_path)

    # Check project state
    assert gom.app.project.get('user_inspector') == 'Clouseau'
    assert gom.app.project.get('user_project') == 'Test Projet' # intended to fail
