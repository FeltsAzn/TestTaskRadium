"""Recursive download repository.

Classes:
- DownloadRepository - class which accumulate methods to recursive
download repository
"""

import asyncio
import multiprocessing as mp
import os
import time

from bs4 import BeautifulSoup

from src.download_utils import download_page


class DownloadRepository:
    """Recursive download repository.

    Methods:
    - start_collect: main handler to start
    - search_repository: recursive repository searching for finding files
    - check_page: examination if page had link to download file
    - parse_html_code: find specify attributes on page
    - start_download: start extra process for download file from repository
    - create_temp_folder: create temporary folder for saving downloaded file
    - create_saving_directory: create folders to right saving file
    - extract_paths: find absolute file path and directory, which contain file
    - save_file: save downloaded files
    """

    def __init__(self, address: str):
        self.files = []
        self.address = address
        self.queue = mp.Queue()
        self.process = mp.Process(target=self.start_download)

    async def start_collect(self, start_page: str) -> None:
        """Start main process.

        Args:
            start_page (str): repository root
        """
        self.process.start()
        await self.search_repository(start_page)
        time.sleep(2)
        self.process.terminate()

    async def search_repository(self, url: str) -> None:
        """Recursive searching if repository.

        Args:
            url (str): path to searching
        """
        raw_html = await download_page(self.address, url)
        is_file = self.check_page(raw_html)
        if not is_file:
            embedded_links = self.parse_html_code(raw_html)
            for link in embedded_links:
                await self.search_repository(link)

    def check_page(self, html_text: str) -> bool:
        """Check page on specify attributes.

        If we have attributes with download links - put to queue

        Args:
            html_text (str): path to download page

        Returns:
             a boolean value
        """
        soup = BeautifulSoup(html_text, 'lxml')
        tool_bar = soup.find(
            name='h4',
            attrs='file-header ui top attached header df ac sb',
        )
        if tool_bar:
            tag = tool_bar.find('div', class_='ui buttons mr-2')
            if tag is None:
                return False
            link = tag.find('a', string='Raw').get('href')
            print(f'[+]Found file -> {self.address}{link}')
            self.queue.put(link)
            return True
        return False

    def parse_html_code(self,  html_code: str) -> list[str]:
        """Parse page by tags.

        Args:
            html_code (str): page html code

        Returns:
            a list of links for next pages
        """
        soup = BeautifulSoup(html_code, 'lxml')
        links = []
        if soup.tbody:
            for tag in soup.tbody.find_all('a'):
                link = tag.get('href')
                title = tag.get('title')
                if link and title:
                    links.append(link)
            return links
        return []

    def start_download(self):
        """Start downloading and saving files."""
        asyncio.run(self.save_file())

    def create_temp_folder(self):
        """Create 'repository' directory if it isn't exist."""
        if not os.path.exists('repository'):
            os.mkdir('repository')

    def create_saving_directory(self, path: str) -> None:
        """Create path to saving file.

        Args:
            path (str): path context from repository
        """
        if not os.path.exists(path):
            os.makedirs(path)

    def extract_paths(self, link: str) -> tuple[str, str]:
        """Extract directory and full path fore saving file.

        Args:
            link (str): link which contain paths

        Returns:
            a tuple with absolute file path and directory, which contain file
        """
        paths = link.split('/')
        project = paths[2]
        directory = '/'.join(paths[6:-1])
        filename = paths[-1]
        folder = f'repository/{project}/{directory}'
        full_path = f'{folder}/{filename}'

        return full_path, folder

    async def save_file(self):
        """Download and save downloaded files to repository directory."""
        self.create_temp_folder()

        while True:
            if not self.queue.empty():
                link = self.queue.get()
                text = await download_page(self.address, link)
                full_path, directory = self.extract_paths(link)
                self.create_saving_directory(directory)

                with open(f'{full_path}', 'w') as repo_file:
                    repo_file.write(text)
                print(f'[+]File saved in {full_path}')
