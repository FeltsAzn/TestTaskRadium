import asyncio
import pytest
from src.download_utils import download_page
from tests.utils.tools import load_html_page, clear_csrf_token
from tests.utils.datasets import *


@pytest.mark.parametrize(
    argnames="link, filename",
    argvalues=download_page_dataset)
def test_download_page(link: str, filename: str) -> None:
    result = clear_csrf_token(asyncio.run(download_page("https://gitea.radium.group", link)))
    expect_result = clear_csrf_token(load_html_page(filename))
    assert result == expect_result
