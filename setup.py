#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

try:
    with open("HISTORY.md") as history_file:
        history = history_file.read()
except FileNotFoundError:
    history = ""  # TODO remove, bug with tox?

requirements = ["colorlog==4.0.2"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Vincent Poulailleau",
    author_email="vpoulailleau@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    description="Logging made simple, no excuse for any debug print call.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="simplelogging",
    name="simplelogging",
    packages=find_packages(include=["simplelogging"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/vpoulailleau/simplelogging",
    project_urls={
        "Documentation": "https://simplelogging.readthedocs.io/en/latest/",
        "Source": "https://github.com/vpoulailleau/simplelogging/",
        "Tracker": "https://github.com/vpoulailleau/simplelogging/issues",
    },
    version="0.9.0",
    zip_safe=False,
)
