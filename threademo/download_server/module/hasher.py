# -*- coding: utf-8 -*-
import hashlib
from scipy import signal
from PIL import Image
from .base import BaseModule
from module.executors import thread_pool_executor as tp


class Hasher(BaseModule):
    """哈希模块"""

    def _process(self, item):
        # 卷积
        # print("hash pic:{}".format(item))
        cov = [[[0.1], [0.05], [0.1]]]
        img = signal.convolve(item, cov)
        img = Image.fromarray(img.astype('uint8')).convert('RGB')
        # 哈希
        md5 = hashlib.md5(str(img).encode('utf-8')).hexdigest()
        return md5

    def _process_single_thread(self, list_):
        md5_list = []
        for img in list_:
            md5 = self._process(img)
            md5_list.append(md5)

        return md5_list

    def _process_multi_thread(self, list_):
        md5_list = []
        task_list = []
        for item in list_:
            task = tp.submit(self._process, (item))
            task_list.append(task)

        for task in task_list:
            img = task.result()
            md5_list.append(img)

        return md5_list
