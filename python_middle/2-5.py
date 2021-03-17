# 如何快速找到多个字典中的公共键(key)

from random import randint, sample
from functools import reduce
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
dict_list = [dict1, dict2, dict3]  # 以下编程假设列表长度未知
start = time.time()
key_list = [key for key in dict_list[0] if all(map(lambda t: key in t, dict_list[1:]))]
end = time.time()
print((end - start) * 1000)
print(key_list)

# 方法三： 用集合。 map() reduce()
dict_list = [dict1, dict2, dict3]  # 以下编程假设列表长度未知
start = time.time()

# key_list = reduce(lambda a, b: a & b, map(lambda dic: dic.keys(), dict_list))
key_list = reduce(lambda a, b: a & b, map(dict.keys(), dict_list))  # 上面这行可以简化，用内置函数代替自定义的lambda函数

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


# reduce()函数的用法：reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
#       用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# li = [1,2,3,4]
# reduce(lambda a,b: a+b, li)
# 10


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

# lambda函数
# 匿名函数lambda的用法
#
# Python中，lambda函数也叫匿名函数，及即没有具体名称的函数，它允许快速定义单行函数，类似于C语言的宏，可以用在任何需要函数的地方。这区别于def定义的函数。
# lambda与def的区别：
# 1）def创建的方法是有名称的，而lambda没有。
# 2）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。
# 3）lambda只是一个表达式，而def则是一个语句。
# 4）lambda表达式” : “后面，只能有一个表达式，def则可以有多个。
# 5）像if或for或print等语句不能用于lambda中，def可以。
# 6）lambda一般用来定义简单的函数，而def可以定义复杂的函数。
# 6）lambda函数不能共享给别的程序调用，def可以。
# lambda语法格式：
# lambda 变量 : 要执行的语句
# 冒号前面是参数，可以有多个，用逗号分隔，冒号右边是返回值。
# 使用例子：
#
# g = lambda x: x * x   # 冒号左边是入参，后面的表达式是输出
# g(3)
# 9
#
# g = lambda x, y, z : (x + y) ** z    # 冒号左边的入参可以是多个
# g(1,2,2)
# 9
#
# list_a = [lambda a: a**3, lambda b: b**3]   # lambda可以嵌套在里面
# list_a[0]
# <function <lambda> at 0x106e58e18>
# list_a[0](3)
# 27
