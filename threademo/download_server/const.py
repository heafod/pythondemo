# -*- coding: utf-8 -*-

from enum import Enum


class CalcType(Enum):
    SingleThread = 0
    MultiThread = 1
    MultiProcess = 2
    PyCoroutine = 3
