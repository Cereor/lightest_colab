import os
import logging


def setup_logging(loglevel):
    if loglevel is None:
        loglevel = os.environ.get("SD_STARTFK_LOG_LEVEL")

    if loglevel:
        log_level = getattr(logging, loglevel.upper(), None) or logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s %(levelname)s [%(name)s] + "n" %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

