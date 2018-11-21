# coding=utf-8
import time


class GetTime(object):

    def get_system_time(self):
        # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
        new_time = time.strftime('%Y-%m-%d %H%M%S', time.localtime())
        return new_time
