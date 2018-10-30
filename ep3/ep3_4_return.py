import gc
#return
def addNum():
    a = [0]
    def addNumFunc():
        a[0] = a[0] + 1
        return a[0]
    return addNumFunc

counterA = addNum()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = addNum()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda a: a%2==1, range(1, 20)))
print(L)