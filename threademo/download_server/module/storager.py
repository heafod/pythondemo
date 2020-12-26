# -*- coding: utf-8 -*-

from module.base import BaseModule
from PIL import Image
from module.executors import thread_pool_executor as tp


class Storager(BaseModule):
    """
    存储模块
    """

    def _process(self, item):
        # print("save pic:{}".format(item))
        content, path = item
        content = Image.fromarray(content.astype('uint8')).convert('RGB')
        content.save(path)

    def _process_single_thread(self, list_):
        for item in list_:
            self._process(item)

    def _process_multi_thread(self, list_):
        task_list = []
        for item in list_:
            task = tp.submit(self._process, (item))
            task_list.append(task)

        for task in task_list:
            task.result()
