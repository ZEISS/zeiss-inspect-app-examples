# -*- coding: utf-8 -*-
#
# uut_project_keywords.py
#
# Unit Under Test (UUT) Example
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# ---

import gom


####################################################################################
# Note: This entire script is run by test_blackbox
####################################################################################

# Create a new project. This will raise an exception if a project is already open - which is fine.
try:
    gom.script.sys.create_project ()
except:
    pass

def not_covered_by_test():
    '''This is not covered by any test'''
    print("Hello")

def excluded_from_coverage(): # pragma: no cover
    '''This is not covered by any test either, but won't contribute to the coverage'''
    print("Nothing to say")

def covered_by_unittest(arg):
    '''This function is covered by a unit test'''
    return arg

def get_project_keywords():
    '''This is called by test_whitebox'''
    keywords = {}
    for kw in gom.app.project.project_keywords:
        keywords[kw] = {
            'description': gom.app.project.get(f'description({kw})'),
            'value': gom.app.project.get(kw)
        }
    print(keywords)
    return keywords

PROJECT_KEYWORDS = {
    'project': {'description': 'Project Name', 'value': 'Test Project'},
    'inspector': {'description': 'Inspector', 'value': 'Clouseau'}
}

if __name__ == "__main__":
    for k, v in PROJECT_KEYWORDS.items():
        gom.script.sys.set_project_keywords(
            keywords={k:v['value']},
            keywords_description={k:v['description']}
        )

    print("-- Project keywords --")
    for k in gom.app.project.project_keywords:
        print(f"{k}='{gom.app.project.get(k)}'")
