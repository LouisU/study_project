# 如何实现用户的历史记录功能

# 浏览器可以查看最近访问的过的网页。
# 视频播放器可以查看最近播放过的视频文件。
# shell可以查看用户最近输入过的命令。

# 那么，如何在我们编写的程序中，实现用户的历史记录呢？

import pickle
from collections import deque
# deque是一个双端队列，可以从队列的左右侧弹出或者压入。

a = pickle.load(open('history', 'rb'))
print("a init: {}".format(a))
if len(a) == 0:
    a = deque([], 5)  # 定义了一个deque对象a, 对象a
a.append(1)
print(a)
a.append(2)  # 从队列右端压入
print(a)
a.append(3)
print(a)
a.appendleft(4)  # 从队列左端压入
print(a)
a.appendleft(5)
print(a)
a.append(6)  # 当队列满后，再从右端压入一个新元素，最左端的一个元素被弹出
print(a)
a.appendleft(7)  # 当队列满后，再从左端压入一个新元素，最右端的一个元素被弹出
print(a)

# deque对象中能保存最近的历史记录，但是只是保存在程序的内存中，如果程序关闭了，那么这个历史记录就消失了。
# 那如何实现程序关闭后，再次打开，依然还记得关闭之前的历史记录呢？

# 答案是使用pickle.

pickle.dump(a, open('history', 'wb'))  # pickle.dump将内存中数据，存入到磁盘文件中。
b = pickle.load(open('history', 'rb'))  # pickle.load 将磁盘文件中的内容读入到程序内存中。
print("{} {}".format(list(b), type(b)))   # pick.load 将磁盘中的文件读入程序内存后， 数据的值和类型都保持不变。



