#!/usr/bin/env python3
"""Setup musdl."""

import setuptools
from os import path
from warnings import warn

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open("musdl/__version__.py").read())

req_pkgs = [
    'yt-dlp>=2024.4.9',
    'mutagen',
    'itunespy',
    'requests',
    'colorama',
    'beautifulsoup4',
    'downloader-cli>=0.3.4',
    'pyxdg',
    'ffmpeg-python',
    'pysocks',
    'unidecode',
    'youtube-search-python',
    'pyDes',
    'urllib3',
    'simber==0.2.6',
    'rich',
    'musicbrainzngs',
    'ytmusicapi',
    'spotipy'
]


extra_features = {
    'noise-clean': ['inaSpeechSegmenter', 'tensorflow']
}


# Add the distributable files
file_map = [
    ('/etc/bash_completion.d', 'musdl.bash'),
    ('/usr/share/zsh/functions/Completion/Unix', 'musdl.zsh')
]

data_files = []
for dirname, filename in file_map:
    if not path.exists(filename):
        warn("%s does not exist, skipping." % filename)
    else:
        data_files.append((dirname, [filename]))

params = {
    'data_files': data_files,
}


if __name__ == '__main__':
    setuptools.setup(
        name="musdl",
        version=__version__,
        author="DFR/TN SPRN0\\A",
        description="Youtube Music Downloader",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/dfrctn-sprn0va/musdl",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Topic :: Multimedia :: Sound/Audio",
        ),
        python_requires=">=3.12",
        install_requires=req_pkgs,
        setup_requires=req_pkgs,
        extras_require=extra_features,
        entry_points={
            'console_scripts': [
                "musdl = musdl:entry"
            ]
        },
        **params
    )
