#!/usr/bin/env python3
"""
Setup script for Terminal Games Collection
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="terminal-games-collection",
    version="1.0.0",
    author="Terminal Games Collection",
    author_email="",
    description="A collection of classic games for the Linux terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "terminal-games=games.launcher:main",
        ],
    },
)
