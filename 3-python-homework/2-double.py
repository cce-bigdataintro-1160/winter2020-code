original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9][4:7]

# Solution using for and append in a new list
double_list = []
for i in original_list:
    double_list.append(i * 2)

# Solution using for comprehension
# double_list = [x * 2 for x in original_list]

# Solution using lambda function
# double_list = list(map(lambda x: x * 2, original_list))

print(double_list)
