import logging
from config import project_config as conf

class Logging:
    def __init__(self,level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
# 构建一个方法，我们可以通过这个方法返回所需的logger对象
def init_logger():
    # 初始化刚刚自己定义的logger类，得到类中的logger对象
    logger = Logging().logger
    if logger.handlers:
        return logger
    # 对logger对象设置属性，比如输出到文件以及输出格式的设置
    file_handle = logging.FileHandler(
        filename = conf.log_root_path + conf.log_name,
        mode='a',
        encoding='UTF-8'
    )
    # 设置一个format输出格式
    fmt = logging.Formatter("%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s")
    file_handle.setFormatter(fmt)
    # 将文件输出的Handle设置给logger对象
    logger.addHandler(file_handle)
    return logger


# print(type(init_logger()))
# init_logger().info('666')