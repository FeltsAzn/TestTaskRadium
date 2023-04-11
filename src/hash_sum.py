"""Calculate hash sum for downloaded files.

Classes:
- HashSum: class which accumulate methods to find files hash sums
"""


import json
from hashlib import sha256
from pathlib import Path


class HashSum:
    """Calculate hash sum.

    Methods:
    - start_analyze: start analyze repository to find files hash sums
    - find_files: recursive searching repository
    - find_hash_sum: calculate file hash sum
    - save_calculate_hash: save found hash sums to json file
    """

    def __init__(self):
        self.hash_sum_table = {}

    def start_analyze(self, path: str) -> None:
        """Start main process.

        Args:
            path (str): target path, which contain downloaded files
        """
        self.find_files(path=path)
        self.save_calculate_hash()

    def find_files(self, path: str) -> None:
        """Recursive repository searching.

        Args:
            path (str): path to searching
        """
        context = Path(path)
        if context.iterdir():
            for found_file in context.iterdir():
                file_path = found_file.as_posix()
                filename = found_file.name
                if found_file.is_dir():
                    # recursion entry
                    self.find_files(path=file_path)
                else:
                    # recursion exit
                    hash_sum = self.find_hash_sum(file_path=file_path)
                    self.hash_sum_table[filename] = {
                        'hash_sum': hash_sum,
                        'path': file_path,
                    }

    def find_hash_sum(self, file_path: str) -> str:
        """Calculate hash sum.

        Args:
            file_path (str): file for calculating hash sum

        Returns:
            a hash string
        """
        with open(file_path, 'rb') as downloaded_file:
            file_bytes = downloaded_file.read()
        return sha256(file_bytes).hexdigest()

    def save_calculate_hash(self) -> None:
        """Save calculated result."""
        with open('repository/hash_sums.json', 'w') as result_file:
            json.dump(self.hash_sum_table, result_file, indent=4)
