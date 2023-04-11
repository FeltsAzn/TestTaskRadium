import asyncio
import pytest
from src.download_archive import DownloadArchive
from tests.utils.tools import find_file_hash_sum, right_hash, load_html_page
from tests.utils.datasets import *


@pytest.mark.parametrize(
    argnames="path, filename",
    argvalues=download_file_dataset
)
@pytest.mark.usefixtures("clean_temp_folder")
def test_download_file(path: str, filename: str) -> None:
    expected_result = right_hash(filename)
    class_instance = DownloadArchive(address="https://gitea.radium.group", path=path)
    asyncio.run(class_instance.download_file("temp", path))
    result = find_file_hash_sum(f"temp/{filename}")
    assert result == expected_result


@pytest.mark.parametrize(
    argnames="page, expect_result",
    argvalues=parse_html_code_archive_dataset
)
def test_parse_html_code(page: str, expect_result: str | None) -> None:
    data = load_html_page(page)
    class_instance = DownloadArchive(address="https://gitea.radium.group", path="some_path")
    result = class_instance.parse_html_code(data)
    assert result == expect_result
