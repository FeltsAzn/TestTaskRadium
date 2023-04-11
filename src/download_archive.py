"""Download repository.

Classes:
- DownloadArchive - class which accumulate methods for download repository
"""

from aiohttp import ClientSession
from bs4 import BeautifulSoup

from src.download_utils import download_page


class DownloadArchive:
    """Class for download repository archive.

    Methods:
    - run_download: main handler to start
    - download_file: download and save file from repository
    - parse_html_code: find specify attributes on page
    """

    def __init__(self, address: str, path: str):
        self.address = address
        self.path = path

    async def run_download(self) -> None:
        """Start main process."""
        html_text = await download_page(self.address, self.path)
        download_link = self.parse_html_code(html_code=html_text)
        await self.download_file('.', download_link)

    def parse_html_code(self,  html_code: str) -> str:
        """Parse page by tags.

        Args:
            html_code (str): page html code

        Returns:
            a string link for next pages
        """
        soup = BeautifulSoup(html_code, 'lxml')
        download_link = soup.find('button', attrs={'id': 'download-btn'})
        if download_link:
            return download_link.find('a')['href']

    async def download_file(self, folder: str, link: str) -> None:
        """Download repository archive and save local.

        Args:
            folder (str): folder to save archive
            link (str): path to download file from webpage
        """
        async with ClientSession(self.address) as session:
            async with session.get(link) as target_page:
                text = await target_page.read()
            filename = link.split('/')[-1]
            path = f'{folder}/{filename}'
            with open(path, 'wb') as open_file:
                open_file.write(text)
