sticks = 21

print("-" * 50)
print(" " * 21,"棍子游戏"," " * 21)
print("这里有21根木棍，用户和电脑一次选的棍子总数只能是5")
print("谁拿到最后一根就算输。")
print("-" * 50,"\n\n")

while True:
	print("棍子剩下: {:5d} 根".format(sticks),"\n")
	if sticks == 1:
		print("你拿到了最后一根，你失败了！")
		break
	sticks_taken = int(input("你要拿出几根(1-4)："))
	if sticks_taken >=5 or sticks_taken == 0:
		print("拿出的数量不对哦！")
		continue
	print("电脑拿出 {} 根棍子。".format(5 - sticks_taken),"\n")
	sticks -= 5;
