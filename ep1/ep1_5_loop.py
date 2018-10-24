#for
names = ['a','b','c']
for name in names:
    print(name)

n = 0
while n!=2:
    print(names[n])
    n = n + 1

#循环语句自动判别所属的循环区间
#例如下面语句为死循环
while n!=2:
    print(names[n])
n = n + 1

#break continue方法无变化