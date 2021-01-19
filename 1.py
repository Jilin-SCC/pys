# --coding : utf-8
a = int(input("请输入一个数："))

if a>10:
 	print("a>10")
elif a == 10:
 	print("a==10")
else:
 	print("a<10") 

namelist = ['Sophia','Emma','Olivia','Ava','Mia','Isabella','Zoe','Lily','Emily','Madison','Jackson','Aiden','Liam','Lucas','Noah','Mason','Ethan','Caden','Logan','Jacob']
# 点名册
for i in namelist:
    print(i)


a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    if a == 8:
    	break
    print(a)