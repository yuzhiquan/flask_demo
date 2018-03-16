import logging
import sys

LOG_LEVEL = logging.DEBUG

def init_log():
    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)
    console = logging.StreamHandler(sys.stderr)
    console.setLevel(LOG_LEVEL)
    fmt = "[%(levelname)s][%(asctime)s][%(process)d]" \
        "logger=%(name)s|tag=%(funcName)s:%(filename)s:%(lineno)d|" \
        "content=%(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S %z"
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    console.setFormatter(formatter)
    log.addHandler(console)
    return log

log = init_log()