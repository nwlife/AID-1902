from multiprocessing import Queue
q = Queue(3)
# print(q.empty())
q.put(2,[False,timeout])
q.put(1,[False,1])
q.put(6,[False,1])
q.put(9,[False,1])
print(q.get([False,1]))
print(q.get([False,1]))
print(q.get([False,1]))
print(q.empty())


