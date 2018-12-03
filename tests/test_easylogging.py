#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `simplelogging` package."""

import logging

import pytest
import simplelogging


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_constants():
    """Test that simplelogging defines logging levels."""
    assert simplelogging.DEBUG == logging.DEBUG
    assert simplelogging.INFO == logging.INFO
    assert simplelogging.WARNING == logging.WARNING
    assert simplelogging.ERROR == logging.ERROR
    assert simplelogging.CRITICAL == logging.CRITICAL
