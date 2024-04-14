import logging
# 获取一个logging对象
logger = logging.getLogger()
# logging 可以输出比如：控制台，文件中
# 让logging将日志输出到控制台
# logger对象的addhandle可以添加一个handle对象，handle对象记录了具体将日志输出到什么地方，
# 如果想要将日志输出到控制台，那么需要一个控制台的handle对象
# 通过logging.StreamHandle()就可以获取到一个将日志输出到控制台的Handle对象
# stream_handler = logging.StreamHandler()
#如果想把日志输出到文件夹中，需要使用FileHandle
file_header = logging.FileHandler(
    filename='E:/ETL/logs/test.log',
    mode = 'a',
    encoding="UTF-8"
)

# 通过logging.Formatter()完成日志输出格式的控制
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
# 通过Handler的setFormatter方法，给stream_handle提供输出的格式控制
file_header.setFormatter(fmt)
# 通过logger对象的addhandler添加这个stream_handler，就可以将内容输出到控制台
logger.addHandler(file_header)
logger.setLevel(20)
logger.info('我是info信息')