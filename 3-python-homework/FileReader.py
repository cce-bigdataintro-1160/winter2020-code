import os

file_path = 'boston/housing.data'

if os.path.isfile(file_path):
    my_file = open(file_path)

    for line in my_file.readlines():
        stripped_line = line.strip()
        line_without_double_spaces = stripped_line.replace('  ', ' ').replace('  ', ' ')
        print(line_without_double_spaces.split(' '))

    my_file.close()
else:
    print('Please provide a valid file!')

