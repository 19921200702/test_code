import logging
class Logging:
    def __init__(self,level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
def init_logger():
    logger = Logging().logger
    file_handle = logging.FileHandler(
        filename='E:/ETL/logs/11.log',
        mode='a',
        encoding='utf8'


    )
    fmt = logging.Formatter("%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s")
    file_handle.setFormatter(fmt)
    logger.addHandler(file_handle)
    return logger
init_logger().info('huigbiuvi')
init_logger().error('独坐敬亭山，众鸟高飞尽')