def quick_sort(arr):
   if len(arr) <= 1:
      return arr

   pivot = arr[0]
   left_part = [x for x in arr[1:] if x <= pivot]
   right_part = [x for x in arr[1:] if x > pivot]

   print(f"pivot point:{pivot}")
   print(f"left :{left_part}")
   print(f"right :{right_part}")
   print("=======")
   return quick_sort(left_part) + [pivot] + quick_sort(right_part)

arr=[4,5,3,2,1]
print(quick_sort(arr))