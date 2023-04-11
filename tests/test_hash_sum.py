import pytest
from src.hash_sum import HashSum
from tests.utils.datasets import *
from tests.utils.tools import find_file_hash_sum, create_dir


@pytest.mark.parametrize(
    argnames='path, expect_result',
    argvalues=find_files_dataset
)
def test_find_files(path: str, expect_result: list[str]) -> None:
    class_instance = HashSum(path)
    result = class_instance.find_files()
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='files, expect_result',
    argvalues=calculate_files_hash_dataset
)
def test_calculate_files_hash(files: list[tuple[str]], expect_result: dict) -> None:
    class_instance = HashSum("data_for_tests")
    result = class_instance.calculate_files_hash(files)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='file_path, expect_result',
    argvalues=hash_sum_dataset
)
def test_hash_sum(file_path: str, expect_result: str) -> None:
    class_instance = HashSum("data_for_tests")
    result = class_instance.hash_sum(file_path)
    assert result == expect_result


@pytest.mark.parametrize(
    argnames='hash_table, expect_result',
    argvalues=save_calculated_hash_dataset
)
@pytest.mark.usefixtures('create_dir')
def test_save_calculated_hash(hash_table: dict, expect_result: str) -> None:
    class_instance = HashSum("data_for_tests")
    class_instance.save_calculated_hash(hash_table)
    result = find_file_hash_sum('repository/hash_sums.json')
    assert result == expect_result
