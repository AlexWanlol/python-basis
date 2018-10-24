#list的方法
#可变列表
#可多维叠加
namelist = [];
#insert 加入
namelist.insert(0,'Aber')
namelist.append('Bob')
namelist.insert(0,'Tracer')
print(namelist)
#pop 删除
namelist.pop()
namelist.pop(0)
print(namelist)
#变更
namelist[0]='deleted'
print(namelist)
#堆叠
s = ['python', 'java', ['asp', 'php'], 'scheme']
p = s[2]
print(p)

#rang 自动生成0-X的列表
print(list(range(11)))

#tuple的方法
# 不可变列表
staticlist = ('genji','hanzo');
#与可变列表的堆叠
staticlistwithlist = ('a', 'b', ['A', 'B'])