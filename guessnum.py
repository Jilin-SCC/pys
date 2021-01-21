# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com

import random
goal = random.randint(1,101)
minnum,maxnum = 1 , 100
print("这个数在1和100之间.")
while 1:
	num = int(input("猜猜这个数是多少？"))
	if num == goal:
		print("你真棒！就是数字{}。".format(num))
		break
	elif num < goal:
		minnum = num
		print("再试试，数字再{}和{}之间。".format(minnum,maxnum))
	elif num > goal:
		maxnum = num
		print("再试试，数字再{}和{}之间。".format(minnum,maxnum))
	else:
		print("看到这条信息肯定是程序出错了。")