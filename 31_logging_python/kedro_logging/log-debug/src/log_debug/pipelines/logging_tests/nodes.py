import logging

log = logging.getLogger("debug_logger")

def print_logs(msg:str) -> str:
    log.debug(msg)
    log.info(msg)
    log.warning(msg)
    log.error(msg)
    log.critical(msg)
    return 'dummy_string'
