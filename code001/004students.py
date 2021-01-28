#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: 004students.py
#   author: Jilin Xie
# datetime: 2021-1-26 19:44:00
#  effects:这是一个判断学生成绩是否达标的程序，要求输
#  入学生数量，以及各个学生物理、数学、历史三科的成绩
#  ，如果总成绩小于 120，程序打印 “failed”，否则打印
#   “passed”。

n = int(input("请输入学生人数："))
data = {} # 空字典存储数据
subjects = '语文', "数学", "外语"
for i in range(0,n):
	name = input("输入第{}学生名字:".format(i + 1))
	marks = []
	for x in subjects:
		marks.append(int(input("录入学生 {} 的 {} 成绩:".format(name, x))))
	data[name] = marks
print(data)
for x, y in data.items():
	total = sum(y)
	print("{}的总分是:{}".format(x, total))
	if total < 180:
		print("{} 没通过考试！".format(x))
	else:
		print("{} 通过考试！".format(x))
