import logging
logger = logging.getLogger()
file_handle = logging.FileHandler(
    filename='E:/ETL/logs/test.log',
    mode='a',
    encoding='UTF-8'
)
fmt = logging.Formatter(
"%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
file_handle.setFormatter(fmt)
logger.addHandler(file_handle)
logger.setLevel(20)
logger.info('rrr')