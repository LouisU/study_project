# 问题：如何为元组中的每个元素命名，提高程序可读性？

# 问题描述：
# student = ('jim', 16, 'male', 160)
# 当我们需要知道学生年龄的时候用student[1]去获取
# 当我们需要知道学生的身高的时候用student[3]去获取
# 但是，当程序中大量的充斥着元组索引的时候，就影响了程序的可读性。

# 那么有什么办法可以给元组中的每个元素命名，达到提供程序的可读性的目的呢？

# ------------------------solution 1  定义数值常量

NAME, AGE, SEX, EMAIL = range(4)
student = ('LiLei', 14, 'male', 'lilei@qq.com')
print(student[NAME], student[AGE])
# 当需要定义teacher的时候，teacher = (30, "XiaoHong")  AGE=0, NAME=1, 这样就和上面的全局变量的顺序不符了。
# 这样的使用方法就需要维护很多的全局变量，添加了维护成本。

# ------------------------solution 2 枚举法
from enum import IntEnum  # 整数枚举类


class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    MAIL = 3


print(student[StudentEnum.NAME])
print(student[StudentEnum.AGE])
print(isinstance(StudentEnum.NAME, int))
print(isinstance(StudentEnum.AGE, int))
print(StudentEnum.NAME == 0)
# 实际上自定义了一个命名空间


# ------------------------solution 3 命名元组： 为元组的每个字段命名
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])  # 定义了元组每个字段的名字，我们称它为命名元组。
s1 = Student(name='louis', age=19, sex='male', email='101')  # 用已经定义的命名元组，初始化一个元组。
print(isinstance(s1, tuple))
print(s1)
print(s1.name)  # 元组的字段调用可以用字段名，使用起来就像是自定义类的属性一样
print(s1[0])  # 元组的字段调用可以用索引
print(s1.age)
print(s1.email)

# 这样， 在元组的初始化赋值的阶段 和 元组的字段的调用阶段， 程序的可读性都提高了。


# 问题：使用元组还是列表？
# 性能比较：
#   初始化的时间: 元组比列表快5倍
#   (study-project-env) ➜  study-project python -m timeit 'x=[1,2,3,4,5]'
#   5000000 loops, best of 5: 49.8 nsec per loop
#   (study-project-env) ➜  study-project python -m timeit 'x=(1,2,3,4,5)'
#   50000000 loops, best of 5: 9.74 nsec per loop
#   取值时间: 元组比列表差不多
#   (study-project-env) ➜  study-project python -m timeit -s 'x=[1,2,3,4,5]' 'y=x[3]'
#   10000000 loops, best of 5: 22.9 nsec per loop
#   (study-project-env) ➜  study-project python -m timeit -s 'x=(1,2,3,4,5)' 'y=x[3]'
#   10000000 loops, best of 5: 22.1 nsec per loop

# 存储空间的比较
# 例子一： 相同的数据，不同的空间
#   a = (1,2,3)
#   a.__sizeof__()
#   48
#   b = [1,2,3]
#   b.__sizeof__()
#   64
#   说明：
#       1. x.__sizeof__() 返回一个对象所占用的字节大小。1字节(Byte） = 8位(bit)
#       2. 存储相同的数据，列表比元组要多用16个字节的空间。
#       3. 由于列表是动态的，所以它需要存储指针，来指向对应的元素(指向表头或者表尾)。这需要用8个字节的空间。
#       4. 由于列表可变，所以需要额外空间存储已经分配的长度大小，这样才可以实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。这需要用8个字节的空间
#
# 例子二： 列表存储空间的分配过程
#   list = []
#   list.__sizeof__() // 空列表的存储空间为 40 字节40
#   list.append(1)
#   list.__sizeof__() 72 // 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
#   list.append(2)
#   list.__sizeof__()72 // 由于之前分配了空间，所以加入元素 2，列表空间不变
#   list.append(3)
#   list.__sizeof__() 72 // 同上list.append(4)list.__sizeof__() 72 // 同上
#   list.append(5)
#   list.__sizeof__() 104 // 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间
#       为了减小每次增加 / 删减操作时空间分配的开销，Python 每次分配空间时都会额外多分配一些，
#   这样的机制（over-allocating）保证了其操作的高效性：增加 / 删除的时间复杂度均为 O(1)
#   对于元组，情况就不同了。元组长度大小固定，元素不可变，所以存储空间固定。

# 总结
# * 列表和元组都是有序的，可以存储任意数据类型的集合。
# * 列表是动态的，长度可变，可以随意增加、删减、改变元素。
# * 元组是静态的，长度大小固定，不可对元素进行增加、删减、改变操作。
# * 列表的存储空间略大于元组，性能略逊于元组。元组相对列表更轻量级。
