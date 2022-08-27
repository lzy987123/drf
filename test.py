# lis = [1,2,3,4]
# su = sum(lis)
# print(su)
#
#
# num = sorted(lis)
# nums = num[-2]
# print(nums)
import json
import threading
import time


# def test(*args,**kwargs):
# 	pass
	# print(list(range(10,-1,-1)))
	# m = max(max([[1, 2, 3], [5, 1], [4]], key=lambda v: max(v)))
	# print(m)
	# lis = [1,2,3,4,5,6,7,8,9,10]
	# lis = [3,4,1,2,5,8,6,9,7]
	# lis.sort()
	# print(lis)
	# lis_len = len(lis) // 2
	# print(lis_len)
	
	# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
	# print(A0)
	# if 1 in A0:
	# 	print("存在")
	# a1 = range(10)
	# print(a1)
	# ass = [i for i in range(10) if i in A0]
	# # A2 = sorted([i for i in range(10) if i in A0])
	# print(ass)
	# a2 = sorted()
	# ax = max(m)
	# print(m)
	# print(A2)
	#
	
	# A3 = sorted([A0[s] for s in A0])
	# print(A3)
	#
	# A4 = [i for i in range(10) if i in A3]
	# print(A4)
	#
	# A5 = {i: i * i for i in range(10)}
	# print(A5)
	#
	# A6 = [[i, i * i] for i in range(10)]
	# print(A6)
	#
	# data = json.loads()
	# str1 = "helloworld"
	# str2 = "wordlhelll"
	# if len(str1) == len(str2) and str1 is not None and str2 is not None:
	# 	if sorted(str1) == sorted(str2):
	# 		return True
	# 	else:
	# 		return False
	# else:
	# 	return "数据不一致"
	# 生成器
	# data = (x for x in range(10))
	# print(data)
	# return data
# 	for i in range(10):
# 		yield i
#
#
# for i in test():
# 	print(i)
#
# if __name__ == '__main__':
# 	test()
	
# import threadingss
# import time
# import _thread
# def job():
# 	print("这是一个需要执行的任务。。。。。")
# 	print("当前线程的个数:", threading.active_count())
# 	print("当前线程的信息:", threading.current_thread())
# 	time.sleep(10)
#
#
# if __name__ == '__main__':
# 	# bools = test()
# 	# print(bools)
# 	# 创建多线程时， 需要制定该线程执行的任务
# 	_thread.start_new_thread(job, ())
# 	_thread.start_new_thread(job, ())
# 	job()

# def func(oldfunc):
# 	def newfunc():
# 		oldfunc()
# 	return newfunc
#
# @func
# def add():
# 	print("abc")
#
#
# add()




# 生成器
# def builder():
# 	for i in range(10):
# 		yield i
#
# for i in builder():
# 	print(i)


# 装饰器

# def func(oldfunc):
# 	def newfunc():
# 		print("+++++++++")
# 		oldfunc()
# 		print("++++++++++")
# 	return newfunc

#
#
# def hello():
# 	thears_list = [i for i in range(10)]
# 	return thears_list
#
#
# def test(params):
# 	print("线程%s" % params)
# 	time.sleep(3)



# def thears():
# 	thears_list = []
# 	for i in hello():
# 		print(i)
# 		thears_list.append(
# 			threading.Thread(target=test, args=(i,))
# 		)
#
# 	for thear in thears_list:
# 		thear.start()
#
# 	for thear in thears_list:
# 		thear.join()
#
# if __name__ == '__main__':
# 	thears()

# class Person:
# 	def set_name(self,name):
# 		self.name = name
#
# 	def get_name(self):
# 		return self.name
#
# 	def greet(self):
# 		print("Hello, I'm %s" % (self.name))
#
# person = Person()
# person.set_name("Ella")
# print(person.get_name())
# person.greet()


# def function(oldfunc):
# 	def newfunc():
# 		print("执行装饰器前面")
# 		oldfunc()
# 		print("执行装饰器后面")
# 	return newfunc
#
#
# @function
# def add():
# 	print("执行逻辑")
#
#
# if __name__ == '__main__':
# 	add()


# def func():
# 	for i in range(10):
# 		yield i
#
# for i in func():
# 	print(i)

#
# lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,100]
#
#
# def func(ls):
# 	for i in ls:
# 		print("第 %s 条数据" % i)
#
#
# def thear():
# 	threas_list = []
# 	threas_list.append(
# 		threading.Thread(target=func, args=(lis,))
# 	)
#
# 	for threas in threas_list:
# 		threas.start()
#
# 	for threas in threas_list:
# 		threas.join()
#
#
# if __name__ == '__main__':
# 	thear()

#
# class Test:
# 	def test1(self, name):
# 		self.name = name
#
# 	def test2(self):
#
# 		print("Hello I'm %s" % self.name)
#
# 	def test3(self):
# 		return self.name
#
# 	def test4(self):
# 		print("我是test4方法")
#
#
# class Charttest(Test):
# 	def test6(self):
# 		print("test6")
#
#
# ct = Charttest()
# ct.test1("Lee")
# ct.test2()
# ct.test6()
# ct.test4()


class Test:
	def __init__(self):
		print("构造方法已经执行")
	
	def calcual(self,expression):
		self.value = eval(expression)
		
	def printResult(self):
		print('result: %s ' % self.value)
		
	def printtest(self):
		print("super父类测试")
		
class MyPrint:
	def printResult(self):
		print('计算结果:%s' % self.value)


class NewCal(Test, MyPrint):
	pass
class CalOld(MyPrint, Test):
	pass

# newcal = NewCal()
# # newcal.calcual('1+2*3')
# # newcal.printResult()
#
# calold = CalOld()
# calold.calcual('1*9')
# calold.printResult()

class Mystes(Test):
	def __init__(self,name):
		super().__init__()
		super().printtest()
		self.name = name
		print("mytes%s" % self.name)

	def tessts(self):
		print("打印超链接%s" % self.name)
		

		
mystes = Mystes(name="Lee")
mystes.tessts()




