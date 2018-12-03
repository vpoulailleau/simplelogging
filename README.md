# Simple Logging

[![PyPI](https://img.shields.io/pypi/v/simplelogging.svg)](https://pypi.python.org/pypi/simplelogging)
[![Travis](https://img.shields.io/travis/vpoulailleau/simplelogging.svg)](https://travis-ci.org/vpoulailleau/simplelogging)
[![ReadTheDocs](https://readthedocs.org/projects/simplelogging/badge/?version=latest)](https://simplelogging.readthedocs.io/en/latest/?badge=latest)

Logging made simple, no excuse for any print call.

* Free software: BSD 3-Clause license
* Documentation: https://simplelogging.readthedocs.io.


## Features


* Simple logging setup
* Based on Python logging module

## Example

### example_module.py

```python
import simplelogging

log = simplelogging.get_logger()


def log_some_messages():
    log.debug("## some debug ##")
    log.info("## some info ##")
    log.warning("## some warning ##")
    log.error("## some error ##")
```

### main.py

```python
import simplelogging
import example_module

# log = simplelogging.get_logger(console_level=simplelogging.DEBUG)
# log = simplelogging.get_logger(file_name="log.txt")
log = simplelogging.get_logger()

a_variable = "a nice variable"
another_variable = 42

log.error("---- normal logging ----")
log.debug("a debug message")
log.info("an info")
log.warning("a warning")
log.error("%s and %d", a_variable, another_variable)

log.error("---- example_module writes to the log ----")
example_module.log_some_messages()

log.error("---- reduced logging (bye debug and info messages) ----")
simplelogging.reduced_logging(log)
log.debug("a debug message")
log.info("an info")
log.warning("a warning")
log.error("an error")

log.error("---- full logging (welcome back debug and info messages) ----")
simplelogging.full_logging(log)
log.debug("a debug message")
log.info("an info")
log.warning("a warning")
log.error("an error")
```

### Result in the console

```
2018-12-02 18:44:34,897 [ERROR  ]       main_simple.py( 11):<module>             :: ---- normal logging ----
2018-12-02 18:44:34,897 [INFO   ]       main_simple.py( 13):<module>             :: an info
2018-12-02 18:44:34,898 [WARNING]       main_simple.py( 14):<module>             :: a warning
2018-12-02 18:44:34,898 [ERROR  ]       main_simple.py( 15):<module>             :: a nice variable and 42
2018-12-02 18:44:34,898 [ERROR  ]       main_simple.py( 17):<module>             :: ---- example_module writes to the log ----
2018-12-02 18:44:34,899 [INFO   ]    example_module.py(  8):log_some_messages    :: ## some info ##
2018-12-02 18:44:34,899 [WARNING]    example_module.py(  9):log_some_messages    :: ## some warning ##
2018-12-02 18:44:34,899 [ERROR  ]    example_module.py( 10):log_some_messages    :: ## some error ##
2018-12-02 18:44:34,900 [ERROR  ]       main_simple.py( 20):<module>             :: ---- reduced logging (bye debug and info messages) ----
2018-12-02 18:44:34,900 [WARNING]       main_simple.py( 24):<module>             :: a warning
2018-12-02 18:44:34,901 [ERROR  ]       main_simple.py( 25):<module>             :: an error
2018-12-02 18:44:34,901 [ERROR  ]       main_simple.py( 27):<module>             :: ---- full logging (welcome back debug and info messages) ----
2018-12-02 18:44:34,901 [INFO   ]       main_simple.py( 30):<module>             :: an info
2018-12-02 18:44:34,902 [WARNING]       main_simple.py( 31):<module>             :: a warning
2018-12-02 18:44:34,902 [ERROR  ]       main_simple.py( 32):<module>             :: an error
```

More examples are provided in the documentation: https://simplelogging.readthedocs.io.

## Credits

This package is an extension of the logging package in the Python standard library.

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
