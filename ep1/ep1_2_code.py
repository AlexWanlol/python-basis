#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#获取字符的整数表示
print(ord('A'))

#整数转换成对应字符
print(chr(65))

#转换指定编码的 byte
print('御三家'.encode('utf-8'))
#中文无法转换
#print('御三家'.encode('ascii'))

#将字符编码解码
print(b'\xe5\xbe\xa1\xe4\xb8\x89\xe5\xae\xb6'.decode())

#获取字符长度
print(len('都我的文档'))
print(len(b'\xe5\xbe\xa1\xe4\xb8\x89\xe5\xae\xb6'))

#变量替代  %nd代表以10个最小定长来格式化变量
#变量的数值前为 % 分割需要输出的字符串，多个变量要用()框起来
# %s 表示输出字符串，兼容所有类型
print('Hi, %10s, you have $%1d.' % ('FreyWan', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#format() 使用 . 连接输出字符串和变量
# {0:XXXX.XX} 可适用格式化变量
print('你好,{0}就要到了，请给我${1:15.2f}钱钱'.format('11.11',1234567.12345))

#int() 强制转换
int('123313');

