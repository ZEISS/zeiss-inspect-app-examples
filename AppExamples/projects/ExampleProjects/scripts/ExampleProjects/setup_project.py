# -*- coding: utf-8 -*-
#
# setup_project.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---
import gom


def open_project(project_name, force_reopen=False):
    # if project already open, do nothing (except force_reopen)
    if (hasattr(gom.app, 'project') and gom.app.project.project_name == project_name and not force_reopen):
        return

    # Close current project (discard changes)
    gom.script.sys.close_project()

    tmp_dir = gom.app.temp_directory
    tmp_dir_project = tmp_dir + '/' + project_name + '.zinspect'

    # Write example project to tmp dir
    project_resource = gom.Resource(':ExampleProjects/projects/' + project_name + '.zinspect')
    with project_resource.open() as src, open(tmp_dir_project, 'wb') as target:
        target.write(src.read())

    # Open example project
    gom.script.sys.load_project(file=tmp_dir_project)


if __name__ == '__main__':

    DIALOG = gom.script.sys.create_user_defined_dialog(file='setup_project.gdlg')
    DIALOG.projectlist.items = ['zeiss_part_test_project', 'volume_test_project', 'zeiss_part_test_measurement']

    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    print("Opening project:", RESULT.projectlist)
    open_project(RESULT.projectlist, True)
