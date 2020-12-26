# -*- coding: utf-8 -*-
import time
import os


class Timer:
    """计时器"""

    def __init__(self):
        self.val = 0

    def tick(self):
        """
        计时器开始
        :return:
        """
        self.val = time.time()

    def tock(self):
        """
        计时器结束
        :return:
        """
        return round(time.time() - self.val, 6)


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    url_list = []
    with open(list_file, 'r') as f:
        url_list = [line.strip() for line in f]

    return url_list[:]
