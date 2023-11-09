from collections import deque

queue = deque()

queue.append("antrian 1")
queue.append("antrian 2")
queue.append("antrian 3")
queue.append("antrian 4")

print(queue)

queue.popleft()
queue.popleft()
queue.popleft()
print("queue after popleft:")
print(queue)
