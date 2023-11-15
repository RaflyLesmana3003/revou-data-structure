def heapify(arr, heap_size, root_index):
      largest = root_index
      left_child = 2 * root_index + 1
      right_child = 2 * root_index + 2

      if left_child < heap_size and arr[left_child] > arr[largest]:
         largest = left_child

      if right_child < heap_size and arr[right_child] > arr[largest]:
         largest = right_child

      if largest != root_index:
         arr[root_index], arr[largest] = arr[largest], arr[root_index]
         heapify(arr, heap_size, largest)

def heap_sort(arr):
         n = len(arr)

         for i in range(n, -1, -1):
            heapify(arr, n, i)

         for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
         

arr = [7, 6, 5, 4, 3, 2, 1]
heap_sort(arr)
print(arr)