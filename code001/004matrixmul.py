#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: 004matrixmul.py
#   author: Jilin Xie
# datetime: 2021-1-26 20:06:00
#  effects: 这个例子里我们计算两个矩阵的 Hadamard 乘积。
#  要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）。
n = int(input("输入矩阵行数："))
print("输入矩阵A的值")
a = []
for i in range(n):
	a.append([int(x) for x in input().split()])
print("输入矩阵B的值")
b = []
for i in range(n):
	b.append([int(x) for x in input().split()])
c = []
for i in range(n):
	c.append([a[i][j] * b[i][j] for j in range(n)])
print("矩阵相乘")
print("-" * 7 * n)
for x in c:
	for y in x:
		print(str(y).rjust(5),end='	')
	print()
print("-" * 7 * n)

# str.rjust(width[, fillchar])
# 返回一个原字符串右对齐,并使用fillchar填充至长度 width 的新字符串。
# 如果指定的长度小于字符串的长度则返回原字符串