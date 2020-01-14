# The library used to manipulate files in Python is called os
import os

# This command displays the current working directory
print(f'My current working directory is {os.getcwd()}')

# os can be used to validate whether a file really exists and if it is really a file
is_file = os.path.isfile('titanic/test.csv')
print(f'The path titanic/test.csv contains a file: {is_file}')

# This command lists all files that exist inside a directory
print(os.listdir('titanic'))

# This command created a new directory at the specified path
os.makedirs('newdir', exist_ok=True)

# This command renamed (or moves, it is the same thing) a file in python
os.rename('newdir','newdir2')

# This command deletes an existing directory at the specified path
os.rmdir('newdir2')


