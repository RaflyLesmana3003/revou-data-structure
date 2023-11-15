def bubble_sort(arr):
   n = len(arr)

   for i in range(n):
      print(f" jumlah looping {n} - {i} - 1 : {n - i - 1}")
      print("======")
      for j in range(n - i - 1):
         # kalau element di index n > element di index n+1, maka tukar posisi nya
         if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
   
   print("function selesai")
   return arr



arr = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(arr)
print(result)