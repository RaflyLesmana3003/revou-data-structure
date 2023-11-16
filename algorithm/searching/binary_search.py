def binary_search(arr, target):
   left = 0
   right = len(arr) - 1

   while left <= right:
      mid = (left + right) // 2

      if arr[mid] == target:
         return mid # return index dari target
      elif arr[mid] > target:
         right = mid - 1
      else:
         left = mid + 1

   return "target not found"

def quick_sort(arr):
   if len(arr) <= 1:
      return arr

   pivot = arr[0]
   left_part = [x for x in arr[1:] if x <= pivot]
   right_part = [x for x in arr[1:] if x > pivot]

   return quick_sort(left_part) + [pivot] + quick_sort(right_part)


arr = [1, 2, 3, 4, 5, 6, 7]

print(arr)
print(arr.index(7))