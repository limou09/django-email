#1、a = “abbbccc”，用正则匹配为 abccc,不管有多少 b，就出现一次？
# import re

# a = "abbbccc"
# print(re.sub('b+','b',a))


#2、有一个多层嵌套列表A=[1,2,[3.4["434",[...]]]]请写一段代码遍历A中的每一个元素并打印出来
# def func(nums):
# 	res = []
# 	for i in nums:
# 		print("i:",i)
# 		if isinstance(i, (list,tuple)):
# 			res.extend(func(i))
# 		else:
# 			res.append(i)
# 	return res

# a = [1,2,["3","4",[{"q":"w"},(5,6)]]]
# print(func(a))


#3、请使用 map 函数将[1,2,3,4]处理成[1,0,1,0]
# #	方法一：
# def func(x):
# 	if x % 2 == 0:
# 		x = 0
# 	else:
# 		x = 1
# 	return x
# print(list(map(func, [1,2,3,4])))

# #	方法二：
# print(list(map(lambda x:0 if x % 2 == 0 else 1, [1,2,3,4])))


#4、请使用 filter 函数将[1,2,3,4]处理成[2,4]
# #	方法一：
# def func(x):
# 	if x % 2 == 0:
# 		return x
# print(list(filter(func, [1,2,3,4])))
# #	方法二：
# print(list(filter(lambda x:x if x % 2 == 0 else None, [1,2,3,4])))


#5、生成一个斐波那契数列
# def func(n):
# 	a,b = 0,1
# 	while n > 0:
# 		a,b = b,a+b
# 		n -= 1
# 		yield a

# for i in func(10):
# 	print(i)


#6、用 Python 语言写一个函数，输入一个字符串，返回倒序结果
# def func(str1):
# 	return sorted(str1, reverse=True)
# print(func(input("请输入一个字符串:")))


# 7、写出 list 的交集与差集的代码 b1 =[1,2,3] b2=[2,3,4]
# b1 = [1,2,3]
# b2 = [2,3,4]

# print(list(set(b1) & set(b2)))#	交集
# print(list(set(b1) ^ set(b2)))#	差集


# 8、Python 如何实现单例模式
# class Singleton(object):

# 	def __new__(cls, *args, **kwargs):
# 		if not hasattr(cls, '_instance'):
# 			cls._instance = object.__new__(cls)
# 		return cls._instance

# s1 = Singleton()
# s2 = Singleton()
# s3 = Singleton()

# s1.name = "张三"
# s2.name = "李四"

# print(s1.name, s2.name, s3.name)
# print(id(s1), id(s2), id(s3))

# 9、冒泡排序
# def func(nlist):
# 	n = len(nlist)
# 	for i in range(0, n-1):
# 		for j in range(0, n-1-i):
# 			if nlist[j] > nlist[j+1]:
# 				nlist[j],nlist[j+1] = nlist[j+1],nlist[j]

# 	return nlist
# nlist = [8,1,78,66,49,51,10]
# print(func(nlist))


# 10、定义一个函数实现闹钟的功能
import time

my_hour = input("请输入时：")
my_minute = input("请输入分：")
flag = 1
while flag:
	#	获取当前时间纪元值
	#time.struct_time(tm_year=2019, tm_mon=6, tm_mday=5, tm_hour=15, tm_min=32, tm_sec=7, tm_wday=2, tm_yday=156, tm_isdst=0)
	t = time.localtime()
	fmt = "%H %M"
	now = time.strftime(fmt,t)
	now = now.split(" ")

	hour = now[0]
	minute = now[1]

	if my_hour == hour and my_minute == minute:
		print("林志玲叫你起床了！")
		print("林志玲叫你起床了！")
		print("林志玲叫你起床了！")
		flag = 0

