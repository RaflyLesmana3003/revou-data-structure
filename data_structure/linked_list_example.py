class Node:
      def __init__(param,data) -> None:
            param.data = data
            param.next = None

      def print():
            print("self.data")
            return

class LinkedList:
      # constructor 
      def __init__(param) -> None:
            param.head = None
            param.revou = "revou mantap"

      def append(param, data):
            print(param.revou)
            new_node = Node(data)

            if param.head is None:
                  param.head = new_node
                  return
            
            current = param.head
            while current.next:
                  current = current.next
            current.next = new_node
            return

      def update(param, target_data, new_data):
            current = param.head
            while current:
                  if current.data == target_data:
                        current.data = new_data
                        return
                  current = current.next
      
my_linkedlist = LinkedList()
my_linkedlist.append(1)
my_linkedlist.append("revou")
my_linkedlist.append("rafly")

my_linkedlist.update("revou", "revou mantap")

