import logging
from config import project_config as conf
class Logging:
    def __init__(self,level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
def init_logger():
    logger = Logging().logger
    if logger.handlers:
        return logger
    file_handle = logging.FileHandler(
        filename=conf.log_root_path + conf.log_name,
        mode='w',
        encoding='UTF-8'
    )
    fmt = logging.Formatter("%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s")
    file_handle.setFormatter(fmt)
    logger.addHandler(file_handle)
    return logger
init_logger().info('999')
init_logger().error('999')
init_logger().warning('我是警告信息')