def insertion_sort(arr):
   for i in range (1,len(arr)):
      # element yang mau di compare
      key = arr[i]

      j = i - 1

      print(f"{j} {key}  ")
      while j >= 0 and key < arr[j]:
         # swap element
         arr[j + 1] = arr[j]
         j -= 1
      
      arr[j + 1] = key

   return arr

arr = [64, 34, 25, 12, 22, 11, 90]
result = insertion_sort(arr)
print(result)




