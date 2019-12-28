import os
from pathlib import Path

my_desktop=f'{Path.home()}/Desktop'

for item in os.listdir(my_desktop):
    if os.path.isfile(f'{my_desktop}/{item}'):
        print(f'{item} is a file')
    elif os.path.isdir(f'{my_desktop}/{item}'):
        print(f'{item} is a dir')
