import math

def jump_search(arr, target):
   array = len(arr)
   step = int(math.sqrt(array))

   print(f"akar : {step}")

   previous_index = 0
   while arr[min(step, array) - 1] < target:
      previous_index = step
      step += int(math.sqrt(array))
      if previous_index >= array:
         return -1
      
   # linear search
   for index in range(previous_index, step):
      if arr[index] == target:
         return index
   
   return "not found"

arr = [1, 2, 3, 4, 5, 6, 7]
arr.sort()
print(arr)
print(f"ada di index ke : {jump_search(arr, 32)}")