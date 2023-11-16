def interpolation(arr, target):
   low, high = 0, len(arr) - 1
   while low <= high:
      mid = low + ((high - low) * (high - low) // (arr[high] - arr[low]))

      if arr[mid] == target:
         return mid
      elif arr[mid] < target:
         low = mid + 1
      else:
         high = mid - 1

   return "not found"

arr = [1, 2, 3, 4, 5, 6, 7]
arr.sort()
print(arr)
print(f"ada di index ke : {interpolation(arr, 5)}")