#logging日志模块
#要想满足复杂的日志输出需求，不能使用print （）函数，
# 可以使用logging模块，它是Python的内置模块。

import logging

#getLogger()函数创建自己的日志器对象
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logging.debug('这是DEBUG级别信息。')
logging.info('这是INFO级别信息')
logging.warning('这是warning级别信息')
logging.error('这是Error级别信息')
logging.critical('这是critical级别信息')



