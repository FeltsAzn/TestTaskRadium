import pytest
from src.download_recursive import DownloadRepository
from tests.utils.load_data import load_html_page, find_dirs
from tests.utils.datasets import *


@pytest.mark.parametrize(
    argnames='filename, expect_result',
    argvalues=check_page_dataset
)
def test_check_page(filename: str, expect_result) -> None:
    class_instance = DownloadRepository(address='https://gitea.radium.group')
    html_code = load_html_page(filename)
    result = class_instance.check_page(html_code)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='page, expect_result',
    argvalues=parse_html_code_recursive_dataset
)
def test_parse_html_code(page: str, expect_result: list) -> None:
    data = load_html_page(page)
    class_instance = DownloadRepository(address='https://gitea.radium.group')
    result = class_instance.parse_html_code(data)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='directory, expect_result',
    argvalues=create_temp_folder_dataset
)
@pytest.mark.usefixtures('remove_created_dirs')
def test_create_temp_folder(directory: str, expect_result: bool) -> None:
    class_instance = DownloadRepository(address='https://gitea.radium.group')
    class_instance.create_temp_folder()
    result = find_dirs('.', directory)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='filename, expect_result',
    argvalues=create_saving_directory_dataset)
@pytest.mark.usefixtures('clean_temp_folder')
def test_create_saving_directory(filename: str, expect_result: bool) -> None:
    class_instance = DownloadRepository(address='https://gitea.radium.group')
    class_instance.create_saving_directory(filename)
    result = find_dirs('temp', filename)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='link, expect_result',
    argvalues=extract_paths_dataset)
def test_extract_paths(link, expect_result) -> None:
    class_instance = DownloadRepository(address='https://gitea.radium.group')
    result = class_instance.extract_paths(link)
    assert result == expect_result
