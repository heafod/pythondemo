# -*- coding: utf-8 -*-

import requests
from PIL import ImageFile
import numpy as np
from .base import BaseModule
from module.executors import thread_pool_executor as tp


class Downloader(BaseModule):

    def __init__(self):
        super(Downloader, self).__init__()

    def _process(self, url):
        # print("download pic:{}".format(url))
        response = requests.get(url)
        content = response.content

        parser = ImageFile.Parser()
        parser.feed(content)
        img = parser.close()
        img = np.array(img)
        return img

    def _process_single_thread(self, list_):
        response_list = []
        for url in list_:
            img = self._process(url)
            response_list.append(img)

        return response_list

    def _process_multi_thread(self, list_):
        response_list = []
        task_list = []
        for url in list_:
            task = tp.submit(self._process, (url))
            task_list.append(task)

        for task in task_list:
            img = task.result()
            response_list.append(img)

        return response_list
