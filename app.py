# 1.创建一个初始化日志的函数
import logging
from logging import handlers
import os
HEADERS = None
EMP_ID = None
DEPART_ID = None

def init_logging():
# 2.创建日志器
    logger = logging.getLogger()
# 3.设置日志等级
    logger.setLevel(logging.INFO)
# 4.创建处理器
    sh = logging.StreamHandler()
    filename = os.path.dirname(os.path.abspath(__file__)) + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="midnight", interval=1, backupCount=7, encoding="UTF-8")
# 5.创建格式化器
    fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
    formatter = logging.Formatter(fmt)
# 6.将格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

# 7.将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
