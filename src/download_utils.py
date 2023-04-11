"""Common functions for download.

Functions:
- download_page: download html code from page
"""


from aiohttp import ClientSession


async def download_page(address: str, link: str) -> str:
    """Download all page.

    Args:
        address (str): root of website
        link (str): path to download page

    Returns:
         a string of html code
    """
    async with ClientSession(address) as session:
        async with session.get(link) as target_page:
            html_code = await target_page.text()
    return html_code
