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

