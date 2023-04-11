import os
import pathlib
import shutil
import pytest


def create_folder(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def delete_folder(path: str) -> None:
    path = pathlib.Path(path)
    for file in path.iterdir():
        if file.is_file():
            os.remove(file)
        else:
            shutil.rmtree(file)
    os.rmdir(path)


@pytest.fixture(scope="function")
def clean_temp_folder():
    create_folder("temp")
    # clean temporary folder before test
    path = pathlib.Path("temp")
    for file in path.iterdir():
        if file.is_file():
            os.remove(file)
        else:
            shutil.rmtree(file)
    yield

    # clean again
    delete_folder("temp")


@pytest.fixture(scope="function")
def remove_created_dirs():
    yield
    try:
        delete_folder("repository")
    except FileNotFoundError:
        ...


@pytest.fixture(scope="function")
def create_dir():
    create_folder("repository")
    yield
    delete_folder("repository")
