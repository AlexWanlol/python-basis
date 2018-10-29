from functools import reduce
#map特性
#map(a,b)
#a为函数,b为序列
#功能为将b序列中每个元素一次作用在函数a，返回结果序列
def addTen(x):
    return x+10

print(list(map(addTen,(1,2,3,4,5,6,7))))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def styleFormatter(name):
    formatter = ''
    for index,element in enumerate(name):
        if index == 0 :
            formatter += element.upper()
        else :
            formatter += element.lower()
    return formatter

def styleFormatter2(name):
    return name[0].upper()+name[1:].lower()

print(list(map(styleFormatter2,['adam', 'LISA', 'barT'])))

#reduce特性
#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def fn(x,y):
    return x*y

def prod(list):
    return reduce(fn,list)

print(prod(list(map(int,[1,'2',3,'4']))))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def char2num(char):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return DIGITS[char]

def str2float(num):
    str = num.split('.')
    inter = str[0]
    floater = str[1]
    intvalue = reduce(lambda a,b:a*10+b,map(char2num,inter))
    print(intvalue)
    floatvalue = reduce(lambda a,b: a/10+b,map(char2num,floater[::-1]))
    floatvalue = floatvalue*0.1
    print(floatvalue)
    return intvalue+floatvalue

print(str2float('1232.434'))