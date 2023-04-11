import json
import os
from hashlib import sha256


class HashSum:
    def __init__(self, path):
        self.path = path

    def start_analyze(self) -> None:
        paths = self.find_files()
        hash_sums = self.calculate_files_hash(paths)
        self.save_calculated_hash(hash_sums)

    def find_files(self) -> list[tuple[str, str]]:
        files_paths = []
        for folder_name, _, filenames in os.walk(self.path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                files_paths.append((filename, file_path))
        return files_paths

    def calculate_files_hash(self, files: list[tuple]) -> dict:
        hash_sum_table = {}
        for filename, file_path in files:
            hash_sum = self.hash_sum(file_path=file_path)
            hash_sum_table[filename] = {
                'hash_sum': hash_sum,
                'path': file_path,
            }
        return hash_sum_table

    @staticmethod
    def hash_sum(file_path: str) -> str:
        with open(file_path, 'rb') as downloaded_file:
            file_bytes = downloaded_file.read()
        return sha256(file_bytes).hexdigest()

    @staticmethod
    def save_calculated_hash(hash_sums: dict) -> None:
        with open('repository/hash_sums.json', 'w') as result_file:
            json.dump(hash_sums, result_file, indent=4)
