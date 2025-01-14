import logging


def demo_log():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

demo_log()

