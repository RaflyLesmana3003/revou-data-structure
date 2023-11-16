def flatten(list):
   flat_list = []

   for element in list:
      if type(element) is list:
         flat_list += flatten(element)
      else:
         flat_list += (element)

   return flat_list

print(flatten([[1,2,3],[4,5,6]]))