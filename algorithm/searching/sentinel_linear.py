def sentinel_linear_search(arr, target):
   n = len(arr)

   # ambil sentinel variabel dan tambahkan ke akhir array
   arr.append(target)

   i = 0
   while arr[i] != target:
      i += 1

   # hapus sentinel variabel dari array
   arr.pop()

   if i < n:
      return i
   else:
      return "not found"
   
arr = [74, 6, 32, 213, 1, 22, 1]
print(sentinel_linear_search(arr, 213))
