#自定函数 使用def关键字
#此章节配合ep2.ep2_1_function食用

def eating(type):
    if type=='meat':
        return '肉'
    elif type=='soup':
        return '煲'
    elif type=='vegetable':
        return '蔬菜'

#定义占位的空函数
def emptyFunc():
    pass

#用于捕捉错误的函数
# def catchError(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError

#测试用的函数
def power(x,n=2):
    value = 1
    while n > 0:
        n = n - 1
        value = value * x
    return value

#可变参数
def strString(*list):
    words = 0
    for word in list:
        words = words + word * word
    print(words)

#关键字参数
def keywords(name,sex,**params):
    print(name,sex,params)

# *param为可变参数，可包含多个key=value样式的参数， age与city参数规定了*param参数列表中必须存在age,city两个参数关键字(key)
#可对age,city设置默认值跳过关键字校验
def changewords(name,sex,*params,age,city):
    print(name,sex,age,city)

#组合函数
def mix1(name,sex,*changewords,age,city,**keywords):
    print(name,sex,changewords,age,city,keywords)
def mix2(name,sex,*changewords,**keywords):
    print(name,sex,changewords,keywords)

#汉诺塔
#此数学问题论证如下
#以a为起点，c为终点，b为缓冲区
#一个阶段的完结的循环为,a->b,a->c,b->c
#此函数最终打印以三柱为原型移动n个堆叠块的路径和移动次数
def tower(n,a,b,c):
    if n == 1:
        print(a+"->"+c)
        return 1
    else:
        count1 = tower(n-1,a,c,b)
        count2 = tower(1,a,b,c)
        count3 = tower(n-1,b,a,c)
        return count1+count2+count3
