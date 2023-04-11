import json
import hashlib
import os.path
import shutil
import zipfile
import pathlib


# test_extract_archive
def create_zip_file(path: str, zipfile_name: str) -> str:
    hash_string = ""
    with zipfile.ZipFile(f"data_for_tests/{zipfile_name}", "w") as zip_file:
        for foldername, _, filenames in os.walk(f"data_for_tests/{path}"):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                hash_string += find_file_hash_sum(file_path)
                zip_file.write(file_path)
    return hashlib.sha256(hash_string.encode()).hexdigest()


# test_extract_archive
def delete_test_zipfile(path: str) -> None:
    try:
        os.remove(path)
    except Exception as ex:
        print(ex)
        shutil.rmtree(path)


# test_extract_archive
def calculate_files_hash_sum(path: str) -> str:
    hash_string = ""
    for foldername, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            hash_string += find_file_hash_sum(file_path)
    return hashlib.sha256(hash_string.encode()).hexdigest()


# test_hash_sum
# test_download_archive
def find_file_hash_sum(file_path: str) -> str:
    with open(file_path, "rb") as file:
        file_bytes = file.read()
    hash_sum = hashlib.sha256(file_bytes).hexdigest()
    return hash_sum


# test_download_archive
def right_hash(filename: str) -> str:
    with open("data_for_tests/hash_sums.json") as file:
        hash_sums = json.load(file)
    return hash_sums[filename]["hash_sum"]


# test_download_archive
# test_download_recursive
# test_download_utils
def load_html_page(filename: str) -> str:
    with open(f"data_for_tests/html/{filename}") as file:
        data = file.read()
    return data


# test_download_utils
def clear_csrf_token(text: str) -> str:
    filtered_text = []
    for line in text.split("\n"):
        if "csrf" not in line.lower():
            filtered_text.append(line)
    return "\n".join(filtered_text)


# test_download_recursive
def find_dirs(start_path: str, filename: str) -> bool:
    path = pathlib.Path(start_path)

    for file in path.iterdir():
        if file.is_dir():
            absolute_path = file.as_posix()
            if filename in absolute_path:
                shutil.rmtree(filename)
                return True

            return find_dirs(absolute_path, filename)
    return False


# test_hash_sum
def create_dir(folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)
