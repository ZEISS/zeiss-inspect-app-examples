# -*- coding: utf-8 -*-
#
# resource_api_example.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom


def get_available_resources():
    # -------------------------------------------------------------------------
    return gom.Resource.list()
    # -------------------------------------------------------------------------


def get_resource_content(res):
    file_handle = res.open()
    return file_handle.read()


def create_resource_with_content(res_name, content):
    _res = gom.Resource(res_name)
    resfile = _res.open(len(content))
    resfile.write(content)
    _res.save()  # saving memory to hard disk


if __name__ == '__main__':
    print("Available resources:")
    print("\n".join(get_available_resources()))
    # -------------------------------------------------------------------------
    res = gom.Resource("test_resource.txt")
    if res.exists():
        print("Resource found with content: ", get_resource_content(res))
    else:
        STRING_BYTES = b"Hello World"
        create_resource_with_content("test_resource.txt", STRING_BYTES)
        print("Resource created with content:", STRING_BYTES)
    # -------------------------------------------------------------------------
