# Lists are very powerful data structures capables of holding multiple values
numbers = [2, 3, 10, 5, 4, 7, 8, 6, 9, 1]
print(numbers)

# We can also assign new items to a list using the following syntax
numbers[5] = 'intruder'
print(numbers)

# Another way to modify list is to 'add' items to it using the .append method
numbers.append('add me!')
print(numbers)

# Lists can really hold any type of value, even another list! Try adding other lists to it
empty_list = []
empty_list.append([99, 98, 97])
empty_list.append([103, 43, 54])
empty_list.append('anything')
empty_list.append(True)
print(empty_list)
