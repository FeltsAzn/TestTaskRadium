"""Extract downloaded repository archive.

Functions:
- extract: recursive function for find zip archive in repository
- decompress_zip: decompress found zip file
"""

import os
import pathlib
from zipfile import ZipFile


def extract(path: str) -> None:
    """Recursive searching.

    Args:
        path (str): Start path to searching repository
    """
    files = pathlib.Path(path)
    if files.iterdir():
        for found_file in files.iterdir():
            file_path = found_file.as_posix()

            filename = found_file.name
            if filename.endswith('.zip'):
                decompress_zip(file_path=file_path)


def decompress_zip(file_path: str) -> None:
    """Decompress a zip archive.

    Args:
        file_path (str): Path to the zip archive file.
    """
    base_folder = 'repository'
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)
    with ZipFile(file_path) as zip_object:
        zip_object.extractall(path=base_folder)
    os.remove(file_path)
