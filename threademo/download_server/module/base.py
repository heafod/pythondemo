# -*- coding: utf-8 -*-
from const import CalcType


class BaseModule:
    """
    抽象模块
    """

    def __init__(self):
        self.calc_type = CalcType.SingleThread

    def set_calc_type(self, type_):
        self.calc_type = type_

    def _process(self, url):
        pass

    def _process_single_thread(self, list_):
        pass

    def _process_multi_thread(self, list_):
        pass

    def process(self, list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_single_thread(list_)
        elif self.calc_type == CalcType.MultiThread:
            return self._process_multi_thread(list_)
