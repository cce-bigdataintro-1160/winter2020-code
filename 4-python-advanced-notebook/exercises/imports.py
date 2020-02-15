import sys
import random
import time

user = sys.argv[1]

for i in range(0,100):
    time.sleep(3)
    print(f'This is my message {random.randint(0,50)}: dear {user}')