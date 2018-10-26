#py已经封装好的一些高级特性
from collections import Iterable
import os
#遍历范围内的值
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#normal
for tag in range(3):
    print(L[tag])
#good
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

#是否可迭代性
print(isinstance(L,Iterable))

#快速生成循环列
print([m + n for m in 'ABC' for n in 'XYZ'])
print([x * x for x in range(1, 5)])

print([d for d in os.listdir('.')])

# 杨辉三角
# n阶
def triangle(n):
    #创建存放列表
    trilist = [];
    #定值为1
    if n == 1:
        trilist.append([1])
        print([1])
        return trilist
    # 定值为2
    elif n == 2:
        trilist.append([1])
        trilist.append([1,1])
        print([1])
        print([1,1])
        return trilist
    # 当大于2阶时的通解
    elif n > 2:
        trilist.append([1])
        trilist.append([1, 1])
        for count in range(n - 2):
            addList = [1]
            for n in range(len(trilist)-1):
                addList.append(trilist[-1][n]+trilist[-1][n+1])
            addList.append(1)
            trilist.append(addList)
        return trilist

print(triangle(5))

#使用yield输出杨辉三角
def triangles():
    # 定义最初的数据 1 ，存到列表中
    lt = [1]
    # 进入循环
    while True:
        # 使用yield语句产生一个生成器，返回当前列表
        yield lt
        # 列表后追加元素 0
        lt.append(0)
        # 列表生成式：原列表中前一项与后一项相加
        lt = [lt[i - 1] + lt[i] for i in range(len(lt))]

n = 0
for i in triangles():
    print(i)
    n += 1
    if n == 10:
        break
# rList = [[1],[1,1]]
# print(rList[-1])
# print(len(rList[-1]))
# print(range(len(rList[-1])-1))