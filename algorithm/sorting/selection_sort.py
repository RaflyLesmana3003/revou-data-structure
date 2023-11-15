def selection_sort(arr):
   for i in range(len(arr)):
      smallest_index = i
      for j in range(i,len(arr)):
         if arr[j] < arr[smallest_index]:
            smallest_index = j

      arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

   return arr

arr = [5,4,3,2,1]
print(selection_sort(arr))