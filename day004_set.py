#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: day004_set.py
#   author: Jilin Xie
# datetime: 2021-1-26 14:22:00
#  effects: 学习Python-集合

# 一、建立集合
# 大括号或 set() 函数可以用来创建集合。
# 注意：想要创建空集合，你必须使用 set() 而不是 {}。
# 后者用于创建空字典。		
basket = {'apple', 'rice', 'banana', 'milk', 'rice'}
print(basket) # 你可以看到重复的元素被去除

print('rice' in basket)

# 演示对两个单词中的字母进行集合操作
a = set('abcdrfghgfrdcba')
b = set('congratulations')

print(a)	# a  去重
print(a - b)	# a有b无
print(a | b)	# a有或b有
print(a & b)	# ab都有
print(a ^ b)	# 不同是存在于ab