import logging
logger = logging.getLogger()
file_handler = logging.FileHandler(
    filename='E:/ETL/logs/测试.log',
    mode='a',
    encoding='UTF-8'
)
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
file_handler.setFormatter(fmt)
logger.addHandler(file_handler)
logger.setLevel(20)
logger.info('888')
