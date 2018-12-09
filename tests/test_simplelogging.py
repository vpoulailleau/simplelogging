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


def test_default_logger_console_formatter():
    """Test default logger level stream formatter presence"""
    main_log = simplelogging.get_logger("__main__")
    assert main_log.handlers
    for handler in main_log.handlers:
        if isinstance(handler, colorlog.StreamHandler):
            if isinstance(handler.formatter, colorlog.ColoredFormatter):
                break
    else:
        assert 0, "No good console formatter found"


def test_default_logger_console_formatter_parameters():
    """Test default logger level stream formatter parameters"""
    main_log = simplelogging.get_logger("__main__")
    log_colors = {
        "DEBUG": "blue",
        "INFO": "black,bg_green",
        "WARNING": "black,bg_yellow",
        "ERROR": "white,bg_red",
        "CRITICAL": "red,bg_white",
    }

    secondary_log_colors = {}

    assert main_log.handlers
    for handler in main_log.handlers:
        if isinstance(handler, colorlog.StreamHandler):
            if isinstance(handler.formatter, colorlog.ColoredFormatter):
                formatter = handler.formatter
                assert formatter._fmt == simplelogging.DEFAULT_CONSOLE_FORMAT
                assert formatter.datefmt is None
                assert formatter.log_colors == log_colors
                assert formatter.secondary_log_colors == secondary_log_colors
                assert isinstance(formatter._style, logging._STYLES["%"][0])
                break
    else:
        assert 0, "No good console formatter found"


def test_default_logger_console_level():
    """Test default logger level stream formatter presence"""
    main_log = simplelogging.get_logger("__main__")
    assert main_log.handlers
    for handler in main_log.handlers:
        if isinstance(handler, colorlog.StreamHandler):
            if handler.level == simplelogging.INFO:
                break
    else:
        assert 0, "Not good console level"
