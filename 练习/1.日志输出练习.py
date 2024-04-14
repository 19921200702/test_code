import logging
logger = logging.getLogger()
stream_handler = logging.StreamHandler()
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
stream_handler.setFormatter(fmt)
logger.addHandler(stream_handler)
logger.setLevel(10)
logger.info('888')