# -*- coding:utf8 -*-
import logging
import os
from datetime import datetime


class Log:
    def __init__(self, log_name=None):
        # 指定log保存位置
        base_path = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(base_path, '..\\'))
        self.log_path = os.path.join(fpath, "Logs")

        # 文件的命名
        if log_name is None:
            self.logname = os.path.join(self.log_path, '%s.log' % datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        else:
            self.logname = os.path.join(self.log_path,
                                        '%s_%s.log' % (log_name, datetime.now().strftime('%Y_%m_%d_%H_%M_%S')))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - '
        #                                    'fuc:%(funcName)s- %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a',  encoding='utf-8')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    log = Log()
    log.info("---测试开始---")
    log.info("--------------")
    log.warning("---测试结束---")

