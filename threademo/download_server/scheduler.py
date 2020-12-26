# -*- coding: utf-8 -*-
import prettytable

from module.downloader import Downloader
import utils
import os
from module.hasher import Hasher
from module.storager import Storager
from const import CalcType


class Scheduler:
    """调度模块"""

    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storager = Storager()

    def _wrap_path(self, md5):
        filename = "{}.jpg".format(md5)
        STORAGE_PATH = os.path.join('.', 'images')
        path = os.path.join(STORAGE_PATH, filename)
        return path

    def set_calc_type(self, type_c):
        self.downloader.set_calc_type(type_c)
        self.hasher.set_calc_type(type_c)
        self.storager.set_calc_type(type_c)

    def process(self):
        time_statictics = {}
        time_statictics["cpu_time"] = []
        time_statictics["network_time"] = []
        time_statictics["disk_time"] = []
        timer = utils.Timer()

        # 1 加载图片连接列表
        url_list = utils.urllist()
        # 2 加载下载模块
        timer.tick()
        content_list = self.downloader.process(url_list)
        time_cost = timer.tock()
        time_statictics["network_time"].append(time_cost)
        # 3. 调度哈希模块
        timer.tick()
        md5_list = self.hasher.process(content_list)
        for md5 in md5_list:
            print(md5)
        time_cost = timer.tock()
        time_statictics["cpu_time"].append(time_cost)
        # 4.调度存储模块
        timer.tick()
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        else:
            self.storager.process(item_list)
            time_cost = timer.tock()
            time_statictics["disk_time"].append(time_cost)

        return time_statictics

    def statictics(self, single_log, multi_log):
        table = prettytable.PrettyTable(['类型', '单线程总耗时', '多线程总耗时', '提升率'])
        network_row = ["network"]
        cpu_row = ['cpu']
        disk_row = ['disk']
        # 单线程数据
        network_row.append(single_log['network_time'][0])
        cpu_row.append(single_log['cpu_time'][0])
        disk_row.append(single_log['disk_time'][0])

        # 多线程数据
        network_row.append(multi_log['network_time'][0])
        cpu_row.append(multi_log['cpu_time'][0])
        disk_row.append(multi_log['disk_time'][0])

        time_ = single_log['network_time'][0] - multi_log['network_time'][0]
        life_rate = time_ / single_log['network_time'][0] * 100
        network_row.append(life_rate)

        time_ = single_log['cpu_time'][0] - multi_log['cpu_time'][0]
        life_rate = time_ / single_log['cpu_time'][0] * 100
        cpu_row.append(life_rate)

        time_ = single_log['disk_time'][0] - multi_log['disk_time'][0]
        life_rate = time_ / single_log['disk_time'][0] * 100
        disk_row.append(life_rate)

        table.add_row(network_row)
        table.add_row(cpu_row)
        table.add_row(disk_row)
        print(table)


if __name__ == '__main__':
    scheduler = Scheduler()

    # 单线程运行
    scheduler.set_calc_type(CalcType.SingleThread)
    single_time = scheduler.process()

    # 多线程运行
    scheduler.set_calc_type(CalcType.MultiThread)
    multi_time = scheduler.process()

    # 耗时计算
    scheduler.statictics(single_time, multi_time)

