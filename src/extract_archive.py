import os
from zipfile import ZipFile


class Extractor:
    def __init__(self, path: str):
        self.path = path

    def start_extracting(self):
        zipfile_path = self.find_zipfile()
        self.decompress_zip(file_path=zipfile_path)

    def find_zipfile(self) -> str:
        for foldername, _, filenames in os.walk(self.path):
            for filename in filenames:
                if filename.endswith('.zip'):
                    file_path = os.path.join(foldername, filename)
                    return file_path

    @staticmethod
    def decompress_zip(file_path: str) -> None:
        base_folder = 'repository'
        if not os.path.exists(base_folder):
            os.mkdir(base_folder)
        with ZipFile(file_path) as zip_object:
            zip_object.extractall(path=base_folder)
        os.remove(file_path)
