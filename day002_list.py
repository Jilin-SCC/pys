#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: day001_list.py
#   author: Jilin Xie
# datetime: 2021-1-22 18:45:00
#  effects: Python学习-列表
		
#列表建立
list_1 = [996, 10.123, 65535, 'lucky', 'i love you']
print(list_1)

#末尾添加元素
list_1.append(10001)
list_1.append("财运亨通")
print(list_1)

#任意位置添加元素
list_1.insert(0,-19.20) # 在列表索引 0 位置添加元素 
print(list_1)

#获取列表某个元素的数量
print("元素0出现的次数：",list_1.count(996))
print(list_1)

#删除指定元素
list_1.remove(996)
print(list_1)

#列表排序
#排序的前提是列表的元素是可比较的
#list_1.sort()  出错
#print(list_1) 出错

list_2 = [886, 263 ,1, 0.00398, -65536, 255, 95462145872]
print("原始列表：",list_2)
list_2.sort()
print("排序后：",list_2)

#删除指定位置元素
del list_1[-1]
print(list_1)

#反转整个列表
list_1.reverse()
print(list_1)

#列表用作栈和队列
print("原始列表：",list_1)
list_1.pop(0)
print("执行pop(0)后：",list_1)
list_1.pop(-3)
print("执行pop(-3)后：\n\n",list_1)

#列表推导式
print("=" * 50)
#原始列表生成
squares = []
for x in range(10):
	squares.append(x**2)
print(squares)

#注意这个 for 循环中的被创建（或被重写）的名为  x  的变量在循环完毕后依然存在。使用如下方法，我们可以计算 squares 的值而不会产生任何的副作用
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

#推导式
squares2 = [x**2 for x in range(10)]
print(squares2)

#列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个  for 子句，之后可以有零或多个  for  或  if  子句。结果是一个列表，由表达式依据其后面的 for  和  if  子句上下文计算而来的结果构成。
ls = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(ls)


combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x, y))
print(combs)
#值得注意的是在上面两个方法中的 for  和 if 语句的顺序。
#列表推导式也可以嵌套
a=[1,2,3]
z = [x + 1 for x in [x ** 2 for x in a]]
print(z)