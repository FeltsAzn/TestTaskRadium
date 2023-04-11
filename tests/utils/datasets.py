download_file_dataset = [
    ("/radium/project-configuration/archive/master.zip", "master.zip"),
    ("/radium/project-configuration/archive/master.tar.gz", "master.tar.gz"),
    ("/radium/project-configuration/archive/master.bundle", "master.bundle")
]

parse_html_code_archive_dataset = [
    ("page.html", "/radium/project-configuration/archive/master.zip"),
    ("nitpick.html", None),
    ("LICENSE.html", None),
    ("README.md.html", None)
]

check_page_dataset = [
    ('page.html', False),
    ('nitpick.html', False),
    ('LICENSE.html', True),
    ('README.md.html', True)
]

parse_html_code_recursive_dataset = [
    ('page.html', ['/radium/project-configuration/src/branch/master/nitpick',
                   '/radium/project-configuration/src/branch/master/LICENSE',
                   '/radium/project-configuration/src/branch/master/README.md']),
    ('nitpick.html', ['/radium/project-configuration/src/branch/master/nitpick/all.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/darglint.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/editorconfig.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/file-structure.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/flake8.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/isort.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/pytest.toml',
                      '/radium/project-configuration/src/branch/master/nitpick/styleguide.toml']),
    ('LICENSE.html', []),
    ('README.md.html', [])
]

create_temp_folder_dataset = [
    ('repository', True),
    ('directory', False),
    ('folder', False)
]

create_saving_directory_dataset = [
    ('temp/repo/dir1/dir2', True),
    ('temp/repo', True),
    ('temp/repo/dir1', True),
]

extract_paths_dataset = [
    (
        '/radium/project-configuration/src/branch/master/README.md',
        (
            'repository/project-configuration//README.md',
            'repository/project-configuration/'
        )
    ),
    (
        '/radium/project-configuration/src/branch/master/LICENSE',
        (
            'repository/project-configuration//LICENSE',
            'repository/project-configuration/'
        )
    ),
    (
        '/radium/project-configuration/src/branch/master/nitpick/editorconfig.toml',
        (
            'repository/project-configuration/nitpick/editorconfig.toml',
            'repository/project-configuration/nitpick'
        )
    ),
    (
        '/radium/project-configuration/src/branch/master/nitpick/pytest.toml',
        (
            'repository/project-configuration/nitpick/pytest.toml',
            'repository/project-configuration/nitpick'
        )
    )
]

download_page_dataset = [
    ("/radium/project-configuration", "page.html"),
    ("/radium/project-configuration/src/branch/master/nitpick", "nitpick.html"),
    ("/radium/project-configuration/src/branch/master/LICENSE", "LICENSE.html"),
    ("/radium/project-configuration/src/branch/master/README.md", "README.md.html")
]

find_zipfile_dataset = [
    ('repository', 'custom_name.zip'),
    ('html', "zipfilefile.zip")
]

decompress_zip_dataset = [
    ('repository', 'custom_name.zip'),
    ('html', "zipfilefile.zip")
]

find_files_dataset = [
    (
        'data_for_tests/html',
        [
            ('README.md.html', 'data_for_tests/html/README.md.html'),
            ('page.html', 'data_for_tests/html/page.html'),
            ('nitpick.html', 'data_for_tests/html/nitpick.html'),
            ('LICENSE.html', 'data_for_tests/html/LICENSE.html')
        ]
    ),
    (
        'data_for_tests/repository',
        [
            ('README.md', 'data_for_tests/repository/README.md'),
            ('LICENSE', 'data_for_tests/repository/LICENSE'),
            ('flake8.toml', 'data_for_tests/repository/nitpick/flake8.toml'),
            ('darglint.toml',
             'data_for_tests/repository/nitpick/darglint.toml'),
            ('styleguide.toml',
             'data_for_tests/repository/nitpick/styleguide.toml'),
            ('file-structure.toml',
             'data_for_tests/repository/nitpick/file-structure.toml'),
            ('editorconfig.toml',
             'data_for_tests/repository/nitpick/editorconfig.toml'),
            ('pytest.toml', 'data_for_tests/repository/nitpick/pytest.toml'),
            ('all.toml', 'data_for_tests/repository/nitpick/all.toml'),
            ('isort.toml', 'data_for_tests/repository/nitpick/isort.toml')
        ]
    )
]

calculate_files_hash_dataset = [
    (
        [
            ('README.md', 'data_for_tests/repository/README.md'),
            ('LICENSE', 'data_for_tests/repository/LICENSE'),
            ('flake8.toml', 'data_for_tests/repository/nitpick/flake8.toml'),
            ('darglint.toml',
             'data_for_tests/repository/nitpick/darglint.toml'),
            ('styleguide.toml',
             'data_for_tests/repository/nitpick/styleguide.toml'),
            ('file-structure.toml',
             'data_for_tests/repository/nitpick/file-structure.toml'),
            ('editorconfig.toml',
             'data_for_tests/repository/nitpick/editorconfig.toml'),
            ('pytest.toml', 'data_for_tests/repository/nitpick/pytest.toml'),
            ('all.toml', 'data_for_tests/repository/nitpick/all.toml'),
            ('isort.toml', 'data_for_tests/repository/nitpick/isort.toml')
        ],
        {
            'LICENSE': {'hash_sum': 'f2ec607f67bb0dd3053b49835b02110d5cd0f8eb6da3aac4dc0b142a6b299be9',
                        'path': 'data_for_tests/repository/LICENSE'},
            'README.md': {'hash_sum': '8cf77a685a9b2b729f3b3ff4941e5efdbd07888ccfa96923fd1036dffe25314f',
                          'path': 'data_for_tests/repository/README.md'},
            'all.toml': {'hash_sum': '700f111c1037259067f406c063c3286d1a32e76b9106931bd931ead61975c100',
                         'path': 'data_for_tests/repository/nitpick/all.toml'},
            'darglint.toml': {'hash_sum': 'e9d9941a4f06cacbfb2df1c9ede98db32177ef2a1c641324a46f573a8953ff64',
                              'path': 'data_for_tests/repository/nitpick/darglint.toml'},
            'editorconfig.toml': {'hash_sum': '7e94c7f4bdfb46be0781c3d734da8389b921254b8fbaad261297cf09d4120383',
                                  'path': 'data_for_tests/repository/nitpick/editorconfig.toml'},
            'file-structure.toml': {'hash_sum': '92441118662c296b3a385be8950681bbf0a6795ccd7d854106f3c69dd39c6234',
                                    'path': 'data_for_tests/repository/nitpick/file-structure.toml'},
            'flake8.toml': {'hash_sum': '3f9995629450d6c4d40abd79c5be785cf6a665de48b7688994f17135e03562ae',
                            'path': 'data_for_tests/repository/nitpick/flake8.toml'},
            'isort.toml': {'hash_sum': 'ef2258e7bbbbf51e3bd1012c23a0006233babca23d5c6bf38bad689d8f2f92e1',
                           'path': 'data_for_tests/repository/nitpick/isort.toml'},
            'pytest.toml': {'hash_sum': '3830c00d8141fa6b3409abffd357a9caaab54953f0dbacafc3a9fc9b9ceaae98',
                            'path': 'data_for_tests/repository/nitpick/pytest.toml'},
            'styleguide.toml': {'hash_sum': 'c6c1eaf9d2a84a02474221969810f8485278eaef4653e9db2f1220f0989d556d',
                                'path': 'data_for_tests/repository/nitpick/styleguide.toml'}
        }
    ),
    (
        [
            ('README.md.html', 'data_for_tests/html/README.md.html'),
            ('page.html', 'data_for_tests/html/page.html'),
            ('nitpick.html', 'data_for_tests/html/nitpick.html'),
            ('LICENSE.html', 'data_for_tests/html/LICENSE.html')
        ],
        {
            'LICENSE.html': {'hash_sum': 'db73d5b6f6d549525160417bb88945427de21c422f63264f5cbe0b50cf112bf1',
                             'path': 'data_for_tests/html/LICENSE.html'},
            'README.md.html': {'hash_sum': 'd71b5b670b689d08c9cd6fe0e8faa4e4c2f53596e8da37c660ae7ed5f0c3e866',
                               'path': 'data_for_tests/html/README.md.html'},
            'nitpick.html': {'hash_sum': '1f1d3adcc191a44763e7eaf0b35d0a55b540494571cd455f051e67a9756f3723',
                             'path': 'data_for_tests/html/nitpick.html'},
            'page.html': {'hash_sum': '243d40cf3edf688edf0c64341c9769e188cd374a0ff1943197f5922b34f45487',
                          'path': 'data_for_tests/html/page.html'}
        }
    )
]

hash_sum_dataset = [
    (
        'data_for_tests/repository/LICENSE',
        'f2ec607f67bb0dd3053b49835b02110d5cd0f8eb6da3aac4dc0b142a6b299be9'
    ),
    (
        'data_for_tests/repository/nitpick/pytest.toml',
        '3830c00d8141fa6b3409abffd357a9caaab54953f0dbacafc3a9fc9b9ceaae98'
    ),
    (
        'data_for_tests/repository/nitpick/isort.toml',
        'ef2258e7bbbbf51e3bd1012c23a0006233babca23d5c6bf38bad689d8f2f92e1'
    ),
    (
        'data_for_tests/repository/nitpick/darglint.toml',
        'e9d9941a4f06cacbfb2df1c9ede98db32177ef2a1c641324a46f573a8953ff64'
    ),
    (
        'data_for_tests/repository/README.md',
        '8cf77a685a9b2b729f3b3ff4941e5efdbd07888ccfa96923fd1036dffe25314f'
    ),

]

save_calculated_hash_dataset = [
    (
        {
            'LICENSE.html': {'hash_sum': 'db73d5b6f6d549525160417bb88945427de21c422f63264f5cbe0b50cf112bf1',
                             'path': 'data_for_tests/html/LICENSE.html'},
            'README.md.html': {'hash_sum': 'd71b5b670b689d08c9cd6fe0e8faa4e4c2f53596e8da37c660ae7ed5f0c3e866',
                               'path': 'data_for_tests/html/README.md.html'},
            'nitpick.html': {'hash_sum': '1f1d3adcc191a44763e7eaf0b35d0a55b540494571cd455f051e67a9756f3723',
                             'path': 'data_for_tests/html/nitpick.html'},
            'page.html': {'hash_sum': '243d40cf3edf688edf0c64341c9769e188cd374a0ff1943197f5922b34f45487',
                          'path': 'data_for_tests/html/page.html'}
        },
        '9a2f58d685c2a2917b32d658c3f0c6cfb45815997bb4771e781592e6d19c9c27'
    ),
    (
        {
            'flake8.toml': {'hash_sum': '3f9995629450d6c4d40abd79c5be785cf6a665de48b7688994f17135e03562ae',
                            'path': 'data_for_tests/repository/nitpick/flake8.toml'},
            'isort.toml': {'hash_sum': 'ef2258e7bbbbf51e3bd1012c23a0006233babca23d5c6bf38bad689d8f2f92e1',
                           'path': 'data_for_tests/repository/nitpick/isort.toml'},
            'pytest.toml': {'hash_sum': '3830c00d8141fa6b3409abffd357a9caaab54953f0dbacafc3a9fc9b9ceaae98',
                            'path': 'data_for_tests/repository/nitpick/pytest.toml'},
            'styleguide.toml': {'hash_sum': 'c6c1eaf9d2a84a02474221969810f8485278eaef4653e9db2f1220f0989d556d',
                                'path': 'data_for_tests/repository/nitpick/styleguide.toml'}
        },
        '8b73a27c199ef71702ccdf8f754535438b22cab1651c43de2411fcc57b0dcb9b'
    ),
    (
        {
            'LICENSE': {'hash_sum': 'f2ec607f67bb0dd3053b49835b02110d5cd0f8eb6da3aac4dc0b142a6b299be9',
                        'path': 'data_for_tests/repository/LICENSE'},
            'README.md': {'hash_sum': '8cf77a685a9b2b729f3b3ff4941e5efdbd07888ccfa96923fd1036dffe25314f',
                          'path': 'data_for_tests/repository/README.md'},
            'all.toml': {'hash_sum': '700f111c1037259067f406c063c3286d1a32e76b9106931bd931ead61975c100',
                         'path': 'data_for_tests/repository/nitpick/all.toml'},
            'darglint.toml': {'hash_sum': 'e9d9941a4f06cacbfb2df1c9ede98db32177ef2a1c641324a46f573a8953ff64',
                              'path': 'data_for_tests/repository/nitpick/darglint.toml'}
        },
        'a4d37813021031fa3a4d85210a4d2c449aadffcbb022393fb5b76a93644ab93d'
    )
]
