# FileSelectionAndFiltering

File Selection and Filtering Examples

Examples for selecting and filtering files in ZEISS INSPECT Python scripts.

This App contains the following scripts:

| File                                                              | Description                                                                              |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [listdir_dialog.py](../scripts/listdir_dialog.py)                 | List files in a directory                                                                |
| [listdir_categories.py](../scripts/listdir_categories.py)         | List files in directory and print their category (file, folder or other)                 |
| [listdir_ext.py](../scripts/listdir_ext.py)                       | List files iin directory and print their extension                                       |
| [walkdir_ext.py](../scripts/walkdir_ext.py)                       | Traverses a directory tree and splits each file path in filename, basename and extension |
| [walkdir_import_scripts.py](../scripts/walkdir_import_scripts.py) | Traverses a directory tree and imports all Python scripts                                |
| [walkdir_import_stl_pol.py](../scripts/walkdir_import_stl_pol.py) | Traverses a directory tree and and imports all `.pol` and `.stl` files                   |

A detailed description can be found in the ZEISS Quality Tech Guide: [How Do I Select and Filter Files in Python Scripts](https://techguide.zeiss.com/en/zeiss-inspect-2025/article/how_to_select_and_filter_files_in_python_scripts.html).

## See also

* How-to: [Selecting a file or folder](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/file_selection_dialog.html)
* [User defined dialogs &mdash; File widget](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#file-widget)
* [User defined dialogs &mdash; File system browser widget](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#file-system-browser-widget)
* [Python3 documentation &mdash; os module &mdash; Files and directories](https://docs.python.org/3/library/os.html#files-and-directories)
* [Python3 documentation &mdash; os.path module](https://docs.python.org/3/library/os.path.html)
