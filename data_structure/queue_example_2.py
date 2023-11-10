class Queue:
   def __init__(self):
      self.queue = []

   def push(self, item):
      self.queue.append(item)

   def pop(self):
      if len(self.queue) == 0:
         print ("Stack is empty")
         return
      self.queue.pop(0)
   
   def display(self):
      print(self.queue)
   
my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.display()