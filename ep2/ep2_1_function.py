#自定函数 使用def关键字
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