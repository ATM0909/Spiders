import queue
que = queue.Queue(5) # 队列 先入先出
que = queue.LifoQueue(5) # 栈 后入先出
for i in range(5):
    que.put(i)

print(que.empty())  # 判断队列是否为空
print(que.full())  # 判断队列是否为满
print(que.qsize())  # 判断队列的内容大小

print(que.get())  # 取出队列最后一个数据

print(que.empty())
print(que.full())
print(que.qsize())
que.put(2)
que.put(3, block=True)
print(que.get())