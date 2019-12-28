# Lists are very powerful data structures capables of holding multiple values
numbers = [2, 3, 10, 5, 4, 7, 8, 6, 9, 1]
print(numbers)

# Lists can be "sliced" just like string, so that we can select parts of it
print(numbers[3])
print(numbers[3:8])

# Just like strings, we can check the length of a list
print(f'The len method can show the length of your list {len(numbers)}')

# Finally we can print all elements in a list one by one using a for-loop to iterate over each item
for n in numbers:
    print(f'The number is {n}')
