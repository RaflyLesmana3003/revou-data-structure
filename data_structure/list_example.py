my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list)

for i in [2, 3, 6]:
      print(my_list[i])

my_list.sort()
print("\n sort :", my_list)

my_list.reverse()
print("\n reverse :", my_list)

my_list.sort(reverse=True)
print("\n sort reverse  :", my_list)

print("\nslice :", my_list[1:6])

print("\nstep slice :", my_list[::-1])

