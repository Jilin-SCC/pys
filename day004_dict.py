# 字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。
# 一对大括号 {} 创建一个空字典。初始化字典时，
# 在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。
# 我们使用键来检索存储在字典中的数据。

dicts = {'[Q1]':'你是谁？', '[A1]':'大大', '[Q2]':'她是谁？','[A2]':'不知道'}
print(dicts)

print(dicts['[Q1]'])

# 创建新的键值
dicts["[Q3]"] = '你叫什么名字？'
print(dicts)

#使用 del 关键字删除任意指定的键值对
del dicts['[Q1]']
print(dicts)

#使用 in 关键字查询指定的键是否存在于字典中
print('大' in dicts)


#必须知道的是，字典中的键必须是不可变类型，比如你不能使用列表作为键。
#
#dict() 可以从包含键值对的元组中创建字典
dict((('Indian','Delhi'),('Bangladesh','Dhaka')))

#遍历一个字典，使用字典的 items() 方法。
for x, y in dicts.items():
	print("{} - {}",format(x, y))