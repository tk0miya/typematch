# -*- coding: utf-8 -*-
import os
import re

from setuptools import find_packages, setup


def get_version(filename):
    """
    Return package version as listed in `__version__` in `filename`.
    """
    with open(filename) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


with open('README.rst') as readme_file:
    readme = readme_file.read()


extras_require = {
    ':python_version<"3.5"': [
        'typing'
    ],
    'test': [
        'pytest',
        'flake8',
        'flake8-import-order',
    ],
}

setup(
    name='typematch',
    version=get_version(os.path.abspath('typematch/__init__.py')),
    description='',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
    author='Takeshi KOMIYA',
    author_email='i.tkomiya at gmail.com',
    url='https://github.com/tk0miya/typematch',
    license='Apache License 2.0',
    keywords='python typing',
    packages=find_packages(exclude=['tests']),
    extras_require=extras_require,
)
