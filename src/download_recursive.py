import asyncio
import multiprocessing as mp
import os
import time

from bs4 import BeautifulSoup

from src.download_utils import download_page


class DownloadRepository:
    def __init__(self, address: str):
        self.files = []
        self.address = address
        self.queue = mp.Queue()
        self.process = mp.Process(target=self.start_download)

    async def start_collect(self, start_page: str) -> None:
        self.process.start()
        await self.search_repository(start_page)
        time.sleep(2)
        self.process.terminate()

    async def search_repository(self, url: str) -> None:
        raw_html = await download_page(self.address, url)
        is_file = self.check_page(raw_html)
        if not is_file:
            embedded_links = self.parse_html_code(raw_html)
            for link in embedded_links:
                await self.search_repository(link)

    def check_page(self, html_text: str) -> bool:
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
        asyncio.run(self.save_file())

    @staticmethod
    def create_temp_folder():
        if not os.path.exists('repository'):
            os.mkdir('repository')

    @staticmethod
    def create_saving_directory(path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def extract_paths(link: str) -> tuple[str, str]:
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
