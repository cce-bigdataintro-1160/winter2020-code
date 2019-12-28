mylist = [1,2,3,4,5,6,7,8,9]

empty_list = []
for i in mylist:
    if i >= 4 and i <= 8:
        empty_list.append(2 * i)
print(empty_list)

print([x * 2  for x in [1,2,3,4,5,6,7,8,9] if (x >= 4 and x <= 8)])