# 计算数列 1/x+1/(x+1)+1/(x+2)+ ... +1/n，我们设 x = 1，n = 10。
sum = 0
for i in range(1, 11):
    sum += 1.0 / i
    print("{:2d} {:6.4f}".format(i , sum))