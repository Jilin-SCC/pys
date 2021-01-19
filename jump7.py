for x in range(1,101):
	if x%7 == 0 or int(x/70) == 0 or x%10 == 7:
		continue
	else:
		print(x)