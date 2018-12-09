import simplelogging

log = simplelogging.get_logger()


def log_some_messages():
    log.debug("## some debug ##")
    log.info("## some info ##")
    log.warning("## some warning ##")
    log.error("## some error ##")
