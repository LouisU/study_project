# 如何统计序列中的元素的频度（意思即统计序列中多个元素的频度或者全部元素的频度）

# 实际应用：
#   1. 计算某个序列中，各个元素出现的次数。
#   2. 计算一篇英文文章中，单词频率最高的10个单词是哪些，这10个单词分别出现了多少次。


from random import randint
from collections import Counter  # 推荐使用
import heapq
import time

# 方案一： 将序列转换成{元素:频度}，根据字典值进行排序。

data = [randint(0, 100) for _ in range(1000)]  # 创建一个在0-20之间随机取值的30个元素的列表，这其中必然会有重复的值。
# print(data)
# 将随机列表的元素当成键，值为0，生成字典。
#   因为是字典，虽然随机序列里面的元素有重复的，但是字典里面的键不会重复
data_dict = dict.fromkeys(data, 0)
# print(data_dict)
for i in data:
    data_dict[i] += 1
# print(data_dict)

# ------------ 列表解析
d = [(v, k) for k, v in data_dict.items()]
# print(d)
result = sorted(d, reverse=True)
# print(result)

# ------------ 生成器解析， 生成器比列表初始化时间短而且内存空间少
d = ((v, k) for k, v in data_dict.items())
result = sorted(d, reverse=True)
# print(result)

d = ((v, k) for k, v in data_dict.items())
start = time.time()
print(start)
result = sorted(d, reverse=True)[:3]
end = time.time()
print(end)
print(end - start)
print(result)

# 问题：d = ((v, k) for k, v in data_dict.items()) 中的d有十万个元素，
# 但是只要取排序后的前三个元素，那么对十万个元素排序生成列表就很耗内存和时间。
# 因此我们可以使用堆。（当在大量的元素中，取少数几个值得时候，通常都使用堆。）
d = ((v, k) for k, v in data_dict.items())
start = time.time()
print(start)
result = heapq.nlargest(3, d)
end = time.time()
print(end)
print(end - start)
print(result)

# 方案二：使用标准库collections中的Counter对象。
counter = Counter(data)
print(counter)
print(counter.most_common(3))
