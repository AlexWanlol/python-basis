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

