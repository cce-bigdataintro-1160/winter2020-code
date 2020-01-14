file_path = 'file_to_write.txt'

# To write a file using python we'll use the method `open` with the w+ modifier
my_file = open(file_path, 'w+')

my_file.write('Line1\n')
my_file.write('Line2\n')
my_file.write('Line3\n')

# It's important to close files after they've been used to avoid a `resources leak` on the os
my_file.close()

