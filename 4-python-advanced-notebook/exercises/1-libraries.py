import time as tm
import random
import sys

argument = sys.argv[1]

for x in range(0,50):
    tm.sleep(3)
    print(f'my message {random.randint(0, 500)} user provided {argument}')

