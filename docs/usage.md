# Usage

## Quick start
To use Simple Logging in a project

```python
import simplelogging

log = simplelogging.get_logger()

# start logging
log.debug("## some debug ##")
log.info("## some info ##")
log.warning("## some warning ##")
log.error("## some error ##")
log.critical("## some critical error ##")

try:
    x = 1 / 0
except ZeroDivisionError as error:
    log.log_exception(error)
```

Note: `log` variable is a logger from the Python standard library's `logging` module.

## Configure the logger

The logger provided by `simplelogging.get_logger()` is already configured to be ready to use:

* Console output: info, warning, error and critical messages displayed
* No file output

The only logger that is configured is the one you have in your main script (i.e. not in an imported module). For imported module, log messages will be forwarded to the main logger.

To get a not yet configured logger, you can use:
```python
import simplelogging

log = simplelogging.get_logger(console=False)
```

### Console output

The console output is managed through a `logging.StreamHandler` configured by `simplelogging`.

#### Disabling the console output

As already said, you can avoid having a console output by doing this in your main script:
```python
import simplelogging

log = simplelogging.get_logger(console=False)
```

#### Changing message format on console

```python
import simplelogging

log = simplelogging.get_logger(
    console_format="%(asctime)s")
```

You can configure de message format according to https://docs.python.org/3/library/logging.html#logrecord-attributes.

#### Changing message level on console

```python
import simplelogging

log = simplelogging.get_logger(
    console_level=simplelogging.DEBUG)
```

The logger will display on the console only messages with the level set to provide value or above.

For example, the above code allows debug, info, warning and error messages to be displayed in the console.

`simplelogging.DEBUG` is `logging.DEBUG`, and same for `INFO`, `WARNING`, `ERROR`, `CRITICAL`. They are provided for convenience, avoiding to import `logging`.

See https://docs.python.org/3/library/logging.html#logging-levels and https://docs.python.org/3/howto/logging.html#when-to-use-logging for more detail.

### File output

The file output is managed through a `logging.handlers.RotatingFileHandler` configured by `simplelogging`.

#### Disabling and enabling the file output

File output is disabled by default. But you can enable logging to a file by giving the file path in your main script:
```python
import simplelogging

log = simplelogging.get_logger(
    file_name="log.txt")
```

#### Changing message format in the file

```python
import simplelogging

log = simplelogging.get_logger(
    file_format="%(asctime)s")
```

You can configure de message format according to https://docs.python.org/3/library/logging.html#logrecord-attributes.

#### Changing message level in the file

```python
import simplelogging

log = simplelogging.get_logger(
    file_level=simplelogging.DEBUG)
```

See above the explanations for console level, they are applicable for file level.

### Configuring logger level

The logger level applies to both console and file output. Since the logger is a standard `logging.Logger`, you can use the `setLevel` method.

During the initial configuration, you can provide the logger level.
```python
import simplelogging

log = simplelogging.get_logger(
    logger_level=simplelogging.DEBUG)
```

### Configuring an existing logger

## Default configuration

`simplelogging.get_logger()` is an easy way to configure a logging infrastructure. It accepts several parameters:

* name: name of the logger (default: None)
* logger_level: logging level (default: DEBUG)
* console: activation of console output (default: True)
* console_format: message format on console (default: DEFAULT_FORMAT)
* console_level: logging level of the console (default: INFO)
* file_name: name of the file in which the log will be written (default: None, i.e. no file)
* file_format: message format in the file (default: DEFAULT_FORMAT)
* file_level: logging level in the file (default: DEBUG)

`DEFAULT_FORMAT` is:
```python
DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)-7s] "
    "%(filename)20s(%(lineno)3s):%(funcName)-20s ::"
    " %(message)s"
)
```