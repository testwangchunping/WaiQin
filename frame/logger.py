# _*_ coding: utf-8 _*_
import logging
from frame.get_time import GetTime


class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 获取logger实例，如果参数为空则返回root logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 定义写入日志文件的位置和日志文件名
        rq = GetTime().get_system_time()
        # log_name = './Logs/' + rq + '.log'
        log_name = 'H:/WaiQin/Logs/' + rq + '.log'

        # 创建一个handler，用于输出到文件
        fh = logging.FileHandler(log_name, encoding='utf-8')
        # 设置指定日志的最低输出级别，默认为WARN级别
        fh.setLevel(logging.DEBUG)
        # 设置输出格式
        fh.setFormatter(formatter)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        # 设置指定日志的最低输出级别，默认为WARN级别
        ch.setLevel(logging.DEBUG)
        # 设置输出格式
        ch.setFormatter(formatter)

        # 把handler对象绑定在logger上
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

    # 程序结束后终止logging进程
    def realse(self):
        logging.shutdown()
