import example_module
import simplelogging

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
log.reduced_logging()
log.debug("a debug message")
log.info("an info")
log.warning("a warning")
log.error("an error")

log.error("---- full logging (welcome back debug and info messages) ----")
log.full_logging()
log.debug("a debug message")
log.info("an info")
log.warning("a warning")
log.error("an error")
