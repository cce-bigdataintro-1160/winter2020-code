import os

file_path = 'titanic/test.csv'

if os.path.isfile(file_path):

    # To read a file using python we'll use the method `open`
    my_file = open(file_path)

    for line in my_file.readlines():
        # Strip will remove any `extra` characters that might be misinterpreted when reading a string
        stripped_line = line.strip()
        print(f'Line has the content "{stripped_line}"')

    # It's important to close files after they've been used to avoid a `resources leak` on the os
    my_file.close()

else:
    print('Please provide a valid file!')

