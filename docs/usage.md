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

#### Disabling the console output

As already said, you can avoid having a console output by doing this in your main script:
```python
import simplelogging

log = simplelogging.get_logger(console=False)
```
