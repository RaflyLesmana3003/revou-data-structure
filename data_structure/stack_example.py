from collections import deque

stack = deque()

stack.append("buku 1")
stack.append("buku 2")
stack.append("buku 3")
stack.append("buku 4")

print(stack)

stack.pop()
stack.pop()
stack.pop()
print("stack after pop:")
print(stack)
