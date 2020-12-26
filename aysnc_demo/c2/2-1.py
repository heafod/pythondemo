# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor as Executor

def worker(data):
    for i in data:
        print(i)


data = [i for i in range(1, 11)]

with Executor(max_workers=10) as exe:
    future = exe.submit(worker, data)

