# -*- coding: utf-8 -*-
#
# resource_api_example.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
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
    res = gom.Resource(res_name)
    resfile = res.open(len(string_bytes))
    resfile.write(string_bytes)
    res.save()  # saving memory to hard disk


if __name__ == '__main__':
    print("Available resources:")
    print("\n".join(get_available_resources()))
    # -------------------------------------------------------------------------
    res = gom.Resource("test_resource.txt")
    if (res.exists()):
        print("Resource found with content: ", get_resource_content(res))
    else:
        string_bytes = b"Hello World"
        create_resource_with_content("test_resource.txt", string_bytes)
        print("Resource created with content:", string_bytes)
    # -------------------------------------------------------------------------
