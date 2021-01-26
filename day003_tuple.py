#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: day003_tuple.py
#   author: Jilin Xie
# datetime: 2021-1-25 16:22:00
#  effects: Python学习-元组
		

#元组是由数个逗号分割的值组成
t = 'I', 'love', 'my', 'motherland', "!"
print(t[-1])
for x in t:
	print(x, end=" ")
print("\n")

#任何一个元组执行拆封操作并赋值给多个变量
divmod(15,2)
x, y = divmod(15,2)

#元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值
#如果你尝试这些操作，将会出错：
#>>> a = (1, 2, 3, 4)
#>>> del a[0]

#要创建只含有一个元素的元组，在值后面跟一个逗号。
a = (123)
print("a = (123) -->", type(a))
a = (123,)
print("a = (123,)-->", type(a))
b = 123,
print("b = 123,  -->", type(b))
