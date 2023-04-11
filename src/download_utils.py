from aiohttp import ClientSession


async def download_page(address: str, link: str) -> str:
    async with ClientSession(address) as session:
        async with session.get(link) as target_page:
            html_code = await target_page.text()
    return html_code
