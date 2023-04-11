import pytest
from src.extract_archive import Extractor
from tests.utils.tools import create_zip_file, calculate_files_hash_sum, delete_test_zipfile
from tests.utils.datasets import *


@pytest.mark.parametrize(
    argnames="test_files, zipfile_name",
    argvalues=find_zipfile_dataset
)
def test_find_zipfile(test_files: str, zipfile_name: str):
    create_zip_file(test_files, zipfile_name)
    expect_result = f'data_for_tests/{zipfile_name}'
    result = Extractor('data_for_tests').find_zipfile()
    delete_test_zipfile(expect_result)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames="test_files, expect_zip_file",
    argvalues=decompress_zip_dataset
)
def test_decompress_zip(test_files: str, expect_zip_file: str):
    expect_result = create_zip_file(test_files, expect_zip_file)
    Extractor('.').decompress_zip(f'data_for_tests/{expect_zip_file}')
    result = calculate_files_hash_sum('repository')
    delete_test_zipfile('repository')
    assert result == expect_result
