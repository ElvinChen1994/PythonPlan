# -*- coding:utf-8 -*-
# @Time: 2021/10/14 下午7:52
# @Author: Elvin

import logging

# logging.error('error message')
#
# logger = logging.getLogger('test')
# logger.setLevel(logging.ERROR)
# logger.warning('warn message')
# logger.error('error message')

'''
FileHandler StreamHandler 输出日志信息
'''
# logger  = logging.getLogger('test')
# file_handler = logging.FileHandler("test.log")
# file_handler.setLevel(logging.ERROR)
# logger.addHandler(file_handler)
#
# logger.setLevel(logging.DEBUG)
# logger.error('error')
# logger.critical('critical')

'''
StreamHandler 将日志输出到流中
'''
import sys


# stream_handler = logging.StreamHandler(sys.stdout)
# stream_handler.setLevel(logging.WARNING)
# logger.addHandler(stream_handler)
#
# logger.error('error message')
# logger.critical('critical message')

'''
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名|
%(funcName)s 调用日志输出函数的函数名|
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮点数表示|
%(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数|
%(asctime)s 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s 用户输出的消息

'''

# myloger = logging.getLogger('mylog')
# file_handler = logging.FileHandler('test.log')
# file_handler.setLevel(logging.ERROR)
#
# #设置格式
# formater = logging.Formatter(fmt='%(asctime)s %(process)d %(thread)d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                              datefmt='%Y-%m-%d %H:%M:%S')
#
# file_handler.setFormatter(formater)
# myloger.addHandler(file_handler)
#
# myloger.error('error message')
# myloger.critical('critical message')

'''
输出json格式信息
'''
import json
from collections import OrderedDict #字典对象自动排序

class JsonFormat(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse()

    def parse(self):
        #，分割日志信息
        self.fields = self._fmt.split(",")

    def format(self, record):
        """
        返回json格式字符串
        :param record:
        :return:
        """
        log_record = OrderedDict()
        for field in self.fields:
            if field == 'timestamp':
                log_record[field] = self.formatTime(record, self.datefmt)
            else:
                log_record[field] = record.__dict__.get(field, "")
        log_record = json.dumps(log_record, ensure_ascii=False)
        return log_record

logger = logging.getLogger('my_log')                # 创建logger
file_handler = logging.FileHandler("test.log")      # 创建文件handler
file_handler.setLevel(logging.ERROR)                # 设置日志级别
formater = JsonFormat(fmt='timestamp,filename,lineno,levelname,msg', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.WARNING)
logger.addHandler(stream_handler)

# 添加处理器

logger.setLevel(logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
logger.error("返回正常")

'''
filter
'''
class JsonFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse()

    def parse(self):
        # self._fmt 就是 'timestamp,filename,lineno,levelname,msg'
        self.fields = self._fmt.split(",")

    def format(self, record):
        """
        重载format方法,返回json格式字符串
        :param record:
        :return:
        """
        log_record = OrderedDict()
        for field in self.fields:
            if field == 'timestamp':
                log_record[field] = self.formatTime(record, self.datefmt)
            else:
                log_record[field] = record.__dict__.get(field, "")

        log_record = json.dumps(log_record, ensure_ascii=False)
        return log_record


class LogLevelFilter(logging.Filter):
    def __init__(self, name='', level=logging.INFO):
        super().__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

logger = logging.getLogger('my_log')                # 创建logger
file_handler = logging.FileHandler("test.log")      # 创建文件handler
file_handler.setLevel(logging.INFO)                 # 设置日志级别
formater = JsonFormatter(fmt='timestamp,filename,lineno,levelname,msg', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formater)
file_handler.addFilter(LogLevelFilter(level=logging.INFO))
logger.addHandler(file_handler)                     # 添加处理器

logger.setLevel(logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

'''
LoggerAdapter对logger对象进行扩展
'''
from logging import LoggerAdapter

class JsonFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse()

    def parse(self):
        # self._fmt 就是 'timestamp,filename,lineno,levelname,msg'
        self.fields = self._fmt.split(",")

    def format(self, record):
        """
        重载format方法,返回json格式字符串
        :param record:
        :return:
        """
        log_record = OrderedDict()
        print(record.__dict__)
        for field in self.fields:
            if field == 'timestamp':
                log_record[field] = self.formatTime(record, self.datefmt)
            else:
                log_record[field] = record.__dict__.get(field, "")

        log_record = json.dumps(log_record, ensure_ascii=False)
        return log_record


class LogLevelFilter(logging.Filter):
    def __init__(self, name='', level=logging.INFO):
        super().__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

logger = logging.getLogger('my_log')                # 创建logger
file_handler = logging.FileHandler("test.log")      # 创建文件handler
file_handler.setLevel(logging.INFO)                 # 设置日志级别
formater = JsonFormatter(fmt='timestamp,ip,filename,lineno,levelname,msg', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formater)
file_handler.addFilter(LogLevelFilter(level=logging.INFO))
logger.addHandler(file_handler)                     # 添加处理器
logger.setLevel(logging.DEBUG)

la = LoggerAdapter(logger, {'xxx'})

la.debug('debug message')
la.info('info message')
la.warning('warn message')
la.error('error message')
la.critical('critical message')