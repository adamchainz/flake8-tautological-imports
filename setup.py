#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup


def get_version(filename):
    """
    Return package version as listed in `__version__` in `filename`.
    """
    init_py = open(filename).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('flake8_tidy_imports.py')


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='flake8_tidy_imports',
    version='1.0.0',
    description="A flake8 plugin that helps you write tidier imports.",
    long_description=readme + '\n\n' + history,
    author="Adam Johnson",
    author_email='me@adamj.eu',
    url='https://github.com/adamchainz/flake8-tidy-imports',
    entry_points={
        'flake8.extension': [
            'I20 = '
            'flake8_tidy_imports:ImportChecker',
        ],
    },
    py_modules=['flake8_tidy_imports'],
    include_package_data=True,
    install_requires=[
        'flake8',
    ],
    license="ISCL",
    zip_safe=False,
    keywords='flake8_tidy_imports',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)