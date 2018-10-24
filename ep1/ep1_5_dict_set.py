#字典 dict
dicts = {'Frey':'Leader','Xiao':'Secretary','Chen':'Chief Planner'}

print(dicts['Frey'])

#增加或覆盖
dicts['Frey'] = 'Coder'
print(dicts['Frey'])

#判断字典是否存在
print('Fre' in dicts)
print('Frey' in dicts)
#通过get方式存在即获取，不存在返回None或者自定返回
print(dicts.get('Fre'))
print(dicts.get('Fre',False))
print(dicts.get('Frey',False))

#无序集合 set
lists = [1,2,3,4]
sets = set(lists)
print(sets)
#add 添加进集合
sets.add(5)
print(sets)
#remove 从集合移除
sets.remove(2)
print(sets)

#交集&并集
set1 = set([1,2,3,4,5])
set2 = set([3,5,7,9])
print(set1 | set2)
print(set1 & set2)
