class Stack:
   def __init__(self):
      self.stack = []

   def push(self, item):
      self.stack.append(item)

   def pop(self):
      if len(self.stack) == 0:
         print ("Stack is empty")
         return
      return self.stack.pop()
   
   def display(self):
      print(self.stack)
   
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

my_stack.display()