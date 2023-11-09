class Node:
      def __init__(self,data) -> None:
            self.data = data
            self.next = None

      def print():
            return

class LinkedList:
      def __init__(self) -> None:
            self.head = None

      def append(self, data):
            new_node = Node(data)

            # if linked list is empty
            # then make the new node as head
            if self.head is None:
                  self.head = new_node
                  return
            
            # if linked list is not empty
            # then traverse till the last node and add the new node there
            current = self.head
            while current.next:
                  current = current.next
            current.next = new_node
            return

      def update(self, target_data, new_data):
            current = self.head

            # traverse till the last node
            # and update the data if the target is found
            while current:
                  if current.data == target_data:
                        current.data = new_data
                        return
                  current = current.next
      
      def display(self):
            current = self.head

            # iteration = loop 
            while current:
                  print(current.data, end="->")
                  current = current.next
            print("None")

      def search(self, target):
            current = self.head

            while current:
                  if current.data == target:
                        return current
                  current = current.next
            return None
      
      def insert_after(self, target_data, data):
            current = self.head
            new_node = Node(data)

            while current:
                  if current.data == target_data:
                        new_node.next = current.next
                        current.next = new_node
                        return
                  current = current.next

      def delete(self, target_data):
            if not self.head:
                  return
            
            if self.head.data == target_data:
                  self.head = self.head.next
                  return

            current = self.head
            while current:
                  if current.next.data == target_data:
                        current.next = current.next.next
                        return
                  current = current.next
      
my_linkedlist = LinkedList()
my_linkedlist.append(1)
my_linkedlist.append("revou")
my_linkedlist.append("rafly")
my_linkedlist.append([0.0])

my_linkedlist.update("revou", "revou mantap")


result = my_linkedlist.search("revou mantap")
print(result)

my_linkedlist.insert_after("revou mantap", "revou mantap 2")

my_linkedlist.delete("revou mantap 2")

my_linkedlist.display()
