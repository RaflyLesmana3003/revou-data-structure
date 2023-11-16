def linear_search(arr, target):
   for index in range(len(arr)):
      if arr[index] == target:
         return index
   return "not found"

arr = [74, 6, 32, 213, 1, 22, 1]
print(linear_search(arr, 213))