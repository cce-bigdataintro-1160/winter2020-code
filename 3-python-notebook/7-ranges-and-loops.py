# A very quick way to create a list is to use a range
my_list = range(0, 100)

# We now print each value in the list
for i in my_list:
    print(f'Now looping through the {i} element')

# We can loop through lists of any kind of elements
for fruit in ['apple', 'banana', 'pear', 999]:
    print(f'Now looping through the fruit: {fruit}')
