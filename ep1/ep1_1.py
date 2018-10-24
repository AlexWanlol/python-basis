#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal
from decimal import getcontext

print("hello world")

#输入
#name = input();
#print("name:",name);

#decimal四则运算，保持进度和准确性
print((Decimal('1.24')*Decimal('3.45')))
x = 1.54;
y = 5.467;
z = Decimal(str(x))*Decimal(str(y))
#字符串拼接
print(x,'*',y,'=',z)
w = x*y;
print(x,'*',y,'=',w)

#除法
print(10/3)
#整除
print(10//3)
#取余
print(10%3)
#r内部不转义
print(r'\\\t\\')