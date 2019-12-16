# 如何快速找到多个字典中的公共键(key)

from random import randint, sample
import time

# 数据准备
dict1 = {k: randint(1, 5) for k in sample('abcdefgh', randint(3, 5))}
print("dict1: {}".format(dict1))
dict2 = {k: randint(1, 5) for k in sample('abcdefgh', randint(3, 5))}
print("dict2: {}".format(dict2))
dict3 = {k: randint(1, 5) for k in sample('abcdefgh', randint(3, 5))}
print("dict3: {}".format(dict3))

# 要找到dict1, dict2, dict3的公共键
# 方法一：列表解析
start = time.time()
key_list = [key for key in dict1 if key in dict2 and key in dict3]
end = time.time()
print((end - start) * 1000)
print(key_list)

# 方法一的dict是已经了三个，我们需要一个对dict个数是未知的 更通用的 寻找多个字典中的公共键的方法。
# 方法二： map（） all() 列表解析
dict_list = [dict1, dict2, dict3]
start = time.time()
key_list = [key for key in dict_list[0] if all(map(lambda t: key in t, dict_list[1:]))]
end = time.time()
print((end - start) * 1000)
print(key_list)



# random.sample的用法： 在给点的样例集中随机选取指定次数的样例，形成列表。
# a = sample('ABCD', 2)
# a
# ['B', 'D']
# a = sample([1,2,3,4,5,6], 2)
# a
# [3, 5]


# map()函数的用法：map(function, iterable, …)，它的返回结果是一个列表。
# 参数function传的是一个函数名，可以是python内置的，也可以是自定义的。
# 参数iterable传的是一个可以迭代的对象，例如列表，元组，字符串这样的。
# a = map(str, [1,2,3])
# a
# <map object at 0x10288e6a0>
# list(a)
# ['1', '2', '3']
# a = map(lambda h: h*h, [1,2,3] )
# a
# <map object at 0x10288eb70>
# list(a)
# [1, 4, 9]


# all()函数的用法：
# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。
# all([1,2,3,4])
# True
# all(['a','b','c','d'])
# True
# all((0,1,2,3))
# False
# all([])
# True
# all(())
# True


