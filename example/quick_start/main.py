import simplelogging

# log = simplelogging.get_logger(console_level=simplelogging.DEBUG)
# log = simplelogging.get_logger(file_name="log.txt")
log = simplelogging.get_logger()

a_string_variable = "hello"
an_integer_variable = 42
a_floating_point_variable = 3.14

log.debug("some debug")
log.info("some info")
log.info(
    "some variables: %s, %d, %f",
    a_string_variable,
    an_integer_variable,
    a_floating_point_variable,
)
log.warning("some warning")
log.error("some error")
log.critical("some critical error")

try:
    x = 1 / 0
except ZeroDivisionError as error:
    log.exception(error)
