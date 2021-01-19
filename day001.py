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

#元组定义和拆分
data = ("shiyanlou", "China", "Python")
name, country, language = data

#================================================
days = int(input("Enter days: "))
months = days // 30
days = days % 30
print("Months = {} Days = {}".format(months, days))

#==================================================
days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days, 30)))
# divmod(num1, num2) 返回一个元组，这个元组包含两个值，第一个是 num1 和 num2 相整除得到的值，
# 第二个是 num1 和 num2 求余得到的值，然后我们用 * 运算符拆封这个元组，得到这两个值。


#逻辑运算符 and 和 or 也称作短路运算符：它们的参数从左向右解析，一旦结果可以确定就停止。例如，如果 A 和 C 为真而 B 为假，A and B and C 不会解析 C 。作用于一个普通的非逻辑值时，短路运算符的返回值通常是能够最先确定结果的那个操作数。

#关系运算可以通过逻辑运算符 and 和 or 组合，比较的结果可以用 not 来取反意。逻辑运算符的优先级又低于关系运算符，在它们之中，not 具有最高的优先级，or 优先级最低，所以 A and not B or C 等于 (A and (notB)) or C。当然，括号也可以用于比较表达式。
#
5 and 4  # >>> 4
0 and 4  # >>> 0
False or 3 or 0  # >>> 3
2 > 1 and not 3>5 or 4  # >>> True

# 我们可以手动的执行类型转换。
# 类型转换函数 	转换路径
# int(string) 	字符串 -> 整数值
# str(integer) 	整数值 -> 字符串
# str(float) 	浮点值 -> 字符串