"""Top-level package for Simple Logging."""

__author__ = """Vincent Poulailleau"""
__email__ = "vpoulailleau@gmail.com"
__version__ = "0.4.0"

import inspect
import logging
from logging import DEBUG, ERROR, INFO, WARNING
from logging.handlers import RotatingFileHandler

DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)-7s] "
    "%(filename)20s(%(lineno)3s):%(funcName)-20s ::"
    " %(message)s"
)


def get_logger(
    name=None,
    logger_level=logging.DEBUG,
    console=True,
    console_format=DEFAULT_FORMAT,
    console_level=logging.INFO,
    file_name=None,
    file_format=DEFAULT_FORMAT,
    file_level=logging.DEBUG,
):
    if name:
        caller_name = name
    else:
        caller_frame = inspect.stack()[1]
        caller_module = inspect.getmodule(caller_frame[0])
        caller_name = caller_module.__name__
    if caller_name != "__main__":
        logger = logging.getLogger(caller_name)
    else:
        logger = logging.getLogger()
        configure_main_logger(
            logger,
            logger_level,
            console,
            console_format,
            console_level,
            file_name,
            file_format,
            file_level,
        )
    return logger


def configure_main_logger(
    logger,
    logger_level=logging.DEBUG,
    console=True,
    console_format=DEFAULT_FORMAT,
    console_level=logging.INFO,
    file_name=None,
    file_format=DEFAULT_FORMAT,
    file_level=logging.DEBUG,
):
    logger.setLevel(logger_level)

    console_formatter = logging.Formatter(console_format)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(console_level)
    logger.addHandler(console_handler)

    if file_name:
        file_formatter = logging.Formatter(file_format)
        file_handler = RotatingFileHandler(file_name, "a", 1024 * 1024, 3)
        file_handler.setLevel(file_level)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)


def reduced_logging(logger):
    logger.setLevel(logging.WARNING)


def full_logging(logger):
    logger.setLevel(logging.DEBUG)
