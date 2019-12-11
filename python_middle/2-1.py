# 如何在列表、字典、集合中根据条件筛选数据




from random import randint


# 针对列表  推荐使用列表解析
# 1. 列表解析：
# 先随机生成一个列表，列表的元素为60-100的数值
data = [randint(60, 100) for _ in range(20)]  # for循环中如果不使用循环的值，那么可以写成_
print("data:{}".format(data))
result = [x for x in data if x >= 90]  # 筛选出大于90的值。
print(result)
# 2. filter函数：
result = list(filter(lambda x: x > 90, data))
print(result)

# 针对字典  推荐使用字典解析
# 1. 字典解析：
data = {'student{}'.format(i): randint(50, 100) for i in range(1, 21)}
print("data:{}".format(data))
result = {k: v for k, v in data.items() if v >= 90}  # 筛选出大于90的字段键值对
print(result)
# 2. filter函数：
result = dict(filter(lambda item: item[1] >= 90, data.items()))  # 筛选出大于90的字段键值对
print(result)

# 针对元组
# 1. 元组解析:
data = {randint(50, 100) for _ in range(20)}
print("data:{}".format(data))
result = {x for x in data if x >= 90}
print(result)
# 2. filter函数:
result = set(filter(lambda x: x >= 90, data))
print(result)
