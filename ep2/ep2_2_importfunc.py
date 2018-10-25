#外部调用已经定义好的function
from ep2.ep2_1_function import eating
from ep2.ep2_1_function import power
from ep2.ep2_1_function import strString
from ep2.ep2_1_function import changewords
from ep2.ep2_1_function import keywords
from ep2.ep2_1_function import mix1
from ep2.ep2_1_function import mix2

#调用function
print(eating('meat'))

print(power(5))

print(power(5,6))

strString(21312,2134.2)

keywords('FreyWan','male',age=25,city='Wuxi')
changewords('FreyWan','male',age=25,city='Wuxi')
mix1('FreyWan','male','whatever',age=25,city='Wuxi')
mix2('FreyWan','male','whatever',age=25,city='Wuxi')
