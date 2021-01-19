# 第一天学习Python
# 建议遵守以下约定：
#
# 	使用 4 个空格来缩进
# 	永远不要混用空格和制表符
# 	在函数之间空一行
# 	在类之间空两行
# 	字典，列表，元组以及参数列表中，在 , 后添加一个空格。对于字典，: 后面也添加一个空格
# 	在赋值运算符和比较运算符周围要有空格（参数列表中除外），但是括号里则不加空格：a = f(1, 2) + g(3, 4)
# 	总是在 # 后跟一个空格，然后再写注释
# 	# FIXME -- fix these code later
# 	# TODO -- in future you have to do this

# 一、关键字
# 二、不需要为变量指定数据类型
a = 1
b = 1.01
txt = '我是字符串'
txt_2 = "我也是字符串"
txt_3 = '''我
		仍然是
		字符串
		'''
txt_4 = "转义符号\'s"

# 一般没有输入，但也可用input()函数来输入
a = int(input("请输入一个数："))
if a>10:
 	print("a>10")
elif a == 10:
 	print("a==10")
else:
 	print("a<10") 


# 开始动手吧
# 两个实例
# 1.求N个数的平均值  averagen.py
# 2.华氏温度与摄氏温度转换 temperature.py
# 
# 单行定义多个变量
a, b = 50, 60

#元组第一和拆分
data = ("shiyanlou", "China", "Python")
name, country, language = data