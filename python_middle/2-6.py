# 如何让字典保持有序
# 字典通常都是无序的，数据进入字典的顺序和迭代字典的顺序通常是不同的。
# 那么问题是： 如何使字典保持有序，如何使字典的输入顺序就是字典的迭代顺序。

from collections import OrderedDict
# 按输入顺序 迭代的字典

from random import shuffle
# shuffle可以打乱列表中的顺序

from itertools import islice

# islice为可迭代对象制作切片

# >>>a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
# >>>a[2:3]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: unhashable type: 'slice'
# >>>list(islice(a, 2, 5))
# ['c', 'd', 'e']

if __name__ == '__main__':

    # 生成一个student按成绩排名顺序输入的字典
    s = 'abcdefg'
    student = list(s)
    shuffle(student)
    student_order_dic = OrderedDict()
    for order, name in enumerate(student, 1):
        student_order_dic[name] = order
    print(student_order_dic)


    # 按名字查询排名
    def query_by_name(d, name):
        return d[name]


    print(query_by_name(student_order_dic, 'a'))


    # 那么如何按排名查询名字呢？并且按给定的排名范围返回学生名字。
    def query_by_order(d, left, right=None):
        left -= 1
        if right is None:
            right = left + 1

        return list(islice(d, left, right))


    print(query_by_order(student_order_dic, 3, 6))
