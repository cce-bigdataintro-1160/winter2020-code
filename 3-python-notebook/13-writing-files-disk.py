file_path = 'file_to_write.txt'

# To write a file using python we'll use the method `open`, here's the list of opening modes
# r   Open text file for reading.  The stream is positioned at the
#     beginning of the file.
#
# r+  Open for reading and writing.  The stream is positioned at the
#     beginning of the file.
#
# w   Truncate file to zero length or create text file for writing.
#     The stream is positioned at the beginning of the file.
#
# w+  Open for reading and writing.  The file is created if it does not
#     exist, otherwise it is truncated.  The stream is positioned at
#     the beginning of the file.
#
# a   Open for writing.  The file is created if it does not exist.  The
#     stream is positioned at the end of the file.  Subsequent writes
#     to the file will always end up at the then current end of file,
#     irrespective of any intervening fseek(3) or similar.
#
# a+  Open for reading and writing.  The file is created if it does not
#     exist.  The stream is positioned at the end of the file.  Subse-
#     quent writes to the file will always end up at the then current
#     end of file, irrespective of any intervening fseek(3) or similar.
my_file = open(file_path, 'w+')

my_file.write('Line1\n')
my_file.write('Line2\n')
my_file.write('Line3\n')

# It's important to close files after they've been used to avoid a `resources leak` on the os
my_file.close()

