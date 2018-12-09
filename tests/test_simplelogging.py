#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `simplelogging` package."""

import logging

import colorlog
import pytest

import simplelogging


def test_constants():
    """Test that simplelogging defines logging levels."""
    assert simplelogging.DEBUG == logging.DEBUG
    assert simplelogging.INFO == logging.INFO
    assert simplelogging.WARNING == logging.WARNING
    assert simplelogging.ERROR == logging.ERROR
    assert simplelogging.CRITICAL == logging.CRITICAL


def test_logger_is_from_logging():
    """Test logger class"""
    log = simplelogging.get_logger()
    assert isinstance(log, logging.Logger)


def test_default_logger_level():
    """Test default logger level"""
    main_log = simplelogging.get_logger("__main__")
    assert main_log.getEffectiveLevel() == simplelogging.DEBUG


def test_default_logger_console():
    """Test default logger level stream handler presence"""
    main_log = simplelogging.get_logger("__main__")
    assert main_log.handlers
    for handler in main_log.handlers:
        if isinstance(handler, colorlog.StreamHandler):
            break
    else:
        assert 0, "No console handler found"
