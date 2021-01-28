#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: day005_file.py
#   author: Jilin Xie
# datetime: 2021-1-27 11:53:00
#  effects: 学习Python的文件操作
import os
import random
import time

os.system('cls')
fs = open('A.txt') 
# print('=' * 70)
# print('=' * 23, "业余无线电资格考试练习", '=' * 23 )
#fs.readline()
# print('=' * 20, line_txt.strip(), '=' * 19)
# print('=' * 26, '退出请按Ctrl + C', '=' * 26)
# print('=' * 70)
save = open('save.txt','r')
nnnn = int(save.readline().strip())
for x in range(nnnn):
	for y in range(8):
		fs.readline()
save.close()
s = ['A:', 'B:', 'C:', 'D:']
done_num = 0
answer = []
for problem in range(nnnn,362):

	print('=' * 80)
	print('=' * 28, "业余无线电资格考试练习", '=' * 28 )
	print('=' * 27, '你已完成{:3d}题,总共:361题'.format(problem), '=' * 27)
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
	while an[:1] not in right_answer:
			an = input("回答错误，请重新回答：").upper()
	print('回答正确！开始下一题......')
	save = open('save.txt', 'w')
	save.write(str(problem +1))
	save.close()
	time.sleep(1)
	answer.clear()
	os.system('cls')

print("你居然做完了全部考题，真是佩服你！")
fs.close()
		