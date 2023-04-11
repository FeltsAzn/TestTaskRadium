from aiohttp import ClientSession
from bs4 import BeautifulSoup

from src.download_utils import download_page


class DownloadArchive:
    def __init__(self, address: str, path: str):
        self.address = address
        self.path = path

    async def run_download(self) -> None:
        html_text = await download_page(self.address, self.path)
        download_link = self.parse_html_code(html_code=html_text)
        await self.download_file('.', download_link)

    @staticmethod
    def parse_html_code(html_code: str) -> str:
        soup = BeautifulSoup(html_code, 'lxml')
        download_link = soup.find('button', attrs={'id': 'download-btn'})
        if download_link:
            return download_link.find('a')['href']

    async def download_file(self, folder: str, link: str) -> None:
        async with ClientSession(self.address) as session:
            async with session.get(link) as target_page:
                text = await target_page.read()
            filename = link.split('/')[-1]
            path = f'{folder}/{filename}'
            with open(path, 'wb') as open_file:
                open_file.write(text)
