def merge_sort(arr):
   if len(arr) > 1:
      mid = len(arr)//2
      left_part = arr[0:mid]
      right_part  = arr[mid:]

      merge_sort(left_part)
      merge_sort(right_part)

      i = j = k = 0

      while i < len(left_part) and j < len(right_part):
         if left_part[i] < right_part[j]:
            arr[k] = left_part[i]
            i += 1
         else:
            arr[k] = right_part[j]
            j += 1
         k += 1

      # check jika ada element yang belum ke looping di while
      while i < len(left_part):
         arr[k] = left_part[i]
         i += 1
         k += 1
         
      while i < len(right_part):
         arr[k] = right_part[i]
         i += 1
         k += 1
   
   return arr


arr = [1,2,3,4]
result = merge_sort(arr)
print(f"result : {result}")