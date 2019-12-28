#!/usr/bin/env python3

# Importing sys and os standard libraries
import sys
import os

# The argument 0 is always the name of running script itself
script_name = sys.argv[0]
is_file = os.path.isfile(script_name)
print(f'{script_name} is file? {is_file}')




# Importing time and random standard libraries
import time
import random

# We print 10 random numbers, sleeping for one second between every print
for i in range(0, 10):
    time.sleep(1)
    print(random.randint(0, 50))
