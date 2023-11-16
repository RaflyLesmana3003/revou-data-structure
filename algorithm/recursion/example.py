def iterative_sum(num):
   result = 0
   for i in range(1, num + 1):
      result += i
   return result
print(iterative_sum(10))

def recursive_sum(num):
   if num == 1:
      return 5
   return num + recursive_sum(num - 1)
print(recursive_sum(10))
