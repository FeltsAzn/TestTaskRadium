"""Main file to start script.

Functions:
- choose_mode: function to choose downloaded mode (recursive or archive)
"""

import asyncio

from src.extract_archive import Extractor
from src.download_archive import DownloadArchive
from src.download_recursive import DownloadRepository
from src.hash_sum import HashSum


def choose_mode():
    """Choose downloaded mode.

    Returns:
        a boolean value or exit the program
    """
    while True:
        help_string = 'Download mode:\n' \
                      '- Download archive(1)\n' \
                      '- Download recursive(2)\n' \
                      '- Quite(q)\n' \
                      'Choice: '
        answer = input(help_string)
        if answer == '1':
            return True
        elif answer == '2':
            return False
        else:
            exit(0)


if __name__ == '__main__':
    address = 'https://gitea.radium.group'
    main_page = '/radium/project-configuration'
    choice = choose_mode()
    if choice:
        asyncio.run(DownloadArchive(address, main_page).run_download())
        Extractor('.').start_extracting()
    else:
        asyncio.run(DownloadRepository(address).start_collect(main_page))
    HashSum('repository').start_analyze()
