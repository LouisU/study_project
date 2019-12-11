# 如何根据字典中值的大小，对字典中的项排序

# 方案1：将字典中的项转化为(值，键）元组。（列表解析或zip）
# 知识点：
# 1. 内置函数sorted() 用C实现的，所以性能很高
# 2. sorted函数不能对字典进行排序。
# 3. 那么将字典转化成为元组，因为元组可以比较大小  (3,4) > (1,2)  (1,4)>(2,2)
# (3,4)>(1,5) True  先比较第0个位子的值，3>1为真，那么结果为True
# (1,4)>(1,2) True  先比较第0个位子的值，1=1，那么比较第1个位子的值，4>2为真，那么结果为True
# (3,4)>(4,3) False 先比较第0个位子的值，3>4为假，结果为False
# 4. 列表解析
# 5. zip的使用
# 6. enumerate()函数：用于将一个可遍历的数据对象（list、tuple、string)组合为一个索引序列。可以自定义索引的开始值
# q = [(94, 'c'), (85, 'a'), (84, 'h'), (77, 'd'), (65, 'g'), (63, 'b'), (62, 'e'), (61, 'f')]
# list(enumerate(q))
# >>>[(0, (94, 'c')), (1, (85, 'a')), (2, (84, 'h')), (3, (77, 'd')), (4, (65, 'g')), (5, (63, 'b')), (6, (62, 'e')), (7, (61, 'f'))]
# list(enumerate(q, start=1))
# >>>[(1, (94, 'c')), (2, (85, 'a')), (3, (84, 'h')), (4, (77, 'd')), (5, (65, 'g')), (6, (63, 'b')), (7, (62, 'e')), (8, (61, 'f'))]


from random import randint

p = {k: randint(60, 100) for k in 'abcdefgh'}
print(p)
q = [(v, k) for k, v in p.items()]
print(q)
q = sorted(q)
print(q)
q = sorted(q, reverse=True)
print(q)

p = {k: randint(60, 100) for k in 'abcdefgh'}
print(p)
q = list(zip(p.values(), p.keys()))
print(q)
q = sorted(q)
print(q)
q = sorted(q, reverse=True)
print(q)

# 方案2：传递sorted函数的key参数
p = {k: randint(60, 100) for k in 'abcdefgh'}
print(p)
q = sorted(p.items(), key=lambda item: item[1], reverse=True)
print(q)

print(list(enumerate(q, start=1)))
for i, (k, v) in enumerate(q, start=1):
    print(i, k, v)

for i, (k, v) in enumerate(q, start=1):
    p[k] = (i, v)
print(p)
# {'a': (3, 89), 'b': (4, 81), 'c': (1, 99), 'd': (2, 99), 'e': (7, 68), 'f': (8, 61), 'g': (5, 77), 'h': (6, 69)}
# 此时字典中的值带有了排序的值。