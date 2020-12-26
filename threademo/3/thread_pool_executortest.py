# -*- coding: utf-8 -*-
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def _task():
    for i in range(2):
        print('this is a _task.i={}.thread id={}\n'.format(i, threading.get_native_id()))
        time.sleep(1)

    return time.time()

# 1
tp = ThreadPoolExecutor(10)
# for i in range(10):
#     tp.submit(_task)

# 2
# 如果有返回结果的处理
# for i in range(10):
#     # future 对象
#     future = tp.submit(_task)
#     print(future.result())  # 此时并行变成了串行

# 优化
futures = []
for i in range(10):
    # future 对象
    future = tp.submit(_task)
    futures.append(future)

for future in futures:
    print(future.result())

