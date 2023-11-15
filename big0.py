import math

def jump_search(sorted_array, target):
      array_size = len(sorted_array)
      block_size = int(math.sqrt(array_size))
      
      # Finding the block where the element may be present
      previous_block_end = 0
      while sorted_array[min(block_size, array_size) - 1] < target:
         previous_block_end = block_size
         block_size += int(math.sqrt(array_size))
         if previous_block_end >= array_size:
               return -1
      
      # Linear search within the block
      for index in range(previous_block_end, min(block_size, array_size)):
         if sorted_array[index] == target:
               return index  # Element found
      
      return -1  # Element not found

arr=[1,2,3,4,5,6,7,8,9,10]

print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

