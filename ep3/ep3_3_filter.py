#filter
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

#求序列素数
#创建一个奇数序列（偶数序列一定不是素数
def createList():
    i = 1
    while True:
        i = i + 2
        yield i
#判断是否为素数
def primeFilter(num):
    return lambda x: x%num != 0

#不断返回素数
def primeFunc():
    yield 2
    primeList = createList()
    while True:
        prime = next(primeList)
        yield prime
        primeList = filter(primeFilter(prime),primeList)

#打印k范围内的所有素数
# k = 100
# for n in primeFunc():
#     if n < k:
#         print(n)
#     else:
#         break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

#方法1
#判断回数入口
def jugdeNum():
    roundList = createRoundList();
    while True:
        round = next(roundList)
        yield round
        roundList = filter(roundNum,roundList)

#判断回数
def roundNum(num):
    strNum = str(num)
    k = len(strNum)
    for i in range(k//2):
        if strNum[i] != strNum[k-1-i]:
            return False
    return True

#创建列表
def createRoundList():
    i = 10
    while True:
      i += 1
      yield i

#方法2
def judgeRound():
    numList = createList()
    while True:
        num = next(numList)
        strNum = str(num)
        if strNum == strNum[::-1]:
            yield num

#打印k范围内所有回数
# k = 10000
# for n in judgeRound():
#     if n < k:
#         print(n)
#     else:
#         break