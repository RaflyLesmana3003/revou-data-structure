import array as arr
from ast import List

a = arr.array('u',["🔥","🍁","🤣","😄","😇"])

# print(type(a))
for i in a:
   print(i, end=" ")

# print(a)
print(a[5]) #O(1)

# update array element
a[4] = "😡"

print("\nafter update")
for i in a:
   print(i, end=" ")

# add array in last index
a.append("🪐")

print("\nafter append")
for i in a:
   print(i, end=" ")

# add items in last index
a.extend(["🍓","🍑","🎊"])

print("\nafter extend")
for i in a:
   print(i, end=" ")

# insert items in specific index
a.insert(2,"🍎")
a.insert(2,"🍎")

print("\nafter insert")
for i in a:
   print(i, end=" ")

# remove items from array
a.remove("🍎")

print("\nafter remove")
for i in a:
   print(i, end=" ")

# pop items from array
deleted_element = a.pop(9)

print("\ndeleted element is: ", deleted_element)
print("\nafter pop")
for i in a:
   print(i, end=" ")

# find specific index of element
print("\n 🍓 have index:", a.index("🍓"))

a.insert(2,"🍎")
a.insert(2,"🍎")
print("\n 🍎 have index:", a.index("🍎"))

print("\nafter inserting two apple")
for i in a:
   print(i, end=" ")

print("\n count of 🍎 :",a.count("🍎"))
myarray:List[int] = [1,2,3,4,5,6,7,8,9,10]