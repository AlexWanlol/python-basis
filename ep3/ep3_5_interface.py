#装饰器
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools
import time
import numpy

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        print('startTime:',start)
        func = fn(*args, **kw)
        end = time.time()
        print('endTime:', end)
        print('%s used %d ms' % (fn.__name__,(end - start)*1000))
        return func
    return wrapper

@metric
def createList():
    rangeOne = range(100000)
    print(list(rangeOne))

createList()