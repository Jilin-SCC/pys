#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: day005_file.py
#   author: Jilin Xie
# datetime: 2021-1-27 11:53:00
#  effects: 学习Python的文件操作
import os
import random
import time
# import atexit
# def save_info(): 
# 	save = open('save.txt', 'w')
# 	global done_num
# 	save.write(str(done_num))
# 	save.close()
# atexit.register(save_info)

os.system('cls')

done_num = 0

save = open('save.txt','r')
done_num = int(save.readline().strip())
save.close()

fs = open('A.txt') 
for x in range(done_num):
	for y in range(8):
		fs.readline()

s = ['A:', 'B:', 'C:', 'D:']
answer = []
for problem in range(done_num,362):

	print('=' * 80)
	print('=' * 28, "业余无线电资格考试练习", '=' * 28 )
	print('=' * 27, '你已完成{:3d}  题,总共:361题'.format(problem), '=' * 25)
	print('=' * 31, '退出请按Ctrl + C', '=' * 31)
	print('=' * 80)

	fs.readline()#空行
	num = fs.readline()
	question = fs.readline()
	print('题号：' + num[3:] + "问题：" + question[3:])
	random.shuffle(s)
	answer.append(s[0] + fs.readline()[3:])
	answer.append(s[1] + fs.readline()[3:])
	answer.append(s[2] + fs.readline()[3:])
	answer.append(s[3] + fs.readline()[3:])
	fs.readline()# [P]行
	right_answer = s[0]
	answer.sort()
	for x in answer:
		print(x)
	an = input("请回答：").upper()
	#while an not in right_answer:
	#		an = input("回答错误，请重新回答：").upper()
	#print('回答正确！开始下一题......')
	if an in right_answer:
		print('回答正确！开始下一题')
		time.sleep(1)
	else:
		print('回答错误！正确答案：{}  ,你的答案是：{}'.format(right_answer[:1] , an))
		print('准备下一题......')
		time.sleep(3)
	done_num = problem + 1
	answer.clear()
	os.system('cls')
	save = open('save.txt', 'w')
	save.write(str(done_num))
	save.close()

print("你居然做完了全部考题，真是佩服你！")
fs.close()
		