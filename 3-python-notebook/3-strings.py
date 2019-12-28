# Strings are the type of any text in a Python script

# Creation of simple strings
first_name = 'John'
last_name = 'Doe'

# Printing Strings can be done in a few different ways:
print(first_name)
print(first_name + ' ' + last_name)

# We can also use f-strings or string formatting to compose strings with variables
print(f'My name is {first_name} {last_name}, nice to meet you!')
print('My name is {} {}, nice to meet you!'.format(first_name, last_name))
print('My name is {0} {1}, nice to meet you!'.format(first_name, last_name))

# String variables have a few special functions, let's see what they can do.
print(f'The upper/lower functions change your strings case: {first_name.upper()} {last_name.lower()}!')
print(f'The len method can show the length of your string {len(first_name)}')

# We can split a phrase into a list of words using the split function on an empty space
my_phrase = 'This is a long phrase'
print(f'{my_phrase}')
print(f'{my_phrase.split(" ")}')

# Strings are actually lists of characters. This means they can "sliced" using the following syntax
print(f'First letter of first_name {first_name[0]}')
print(f'Second letter of first_name {first_name[1]}')
print(f'Middle letters of first_name {first_name[1:3]}')
