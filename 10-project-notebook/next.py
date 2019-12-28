import random
import time

presenters = [
'CRISTIAN NITU',
'Hakim Tamgalt',
'Hurryramsingh Hurchand',
'Jonathan Costiniano Galindez',
'Jun Liu',
'Katayoun Baharvandfard',
'Lucia Christina Di Sclafani',
'Samer Kareshe',
'Sebastien Church',
'Shiva Elhamian',
'Stephane Ngo',
'Thiago Marques Ferreira Crespo',
'Thioro Sarr Faty',
'Vasanth Sadasivan',
'Yifan Wu',
'Zachary Zemokhol'
]

cheer = [
    'Good Luck!!!',
    'Loud and Proud.',
    'Best of luck!!',
    'Break a leg!!!!',
    'You were made for this!',
    'Remember me when you’re famous!',
    'May the force be with you!',
    'You got this.',
    'Good presentation!'
]

print('Choose presenter...')
time.sleep(1)
print('Adding some tension...')
time.sleep(1)
print('And the chosen is... drum rolls...')
time.sleep(1)

random_presenter = presenters[random.randint(0, len(presenters) - 1)]
random_cheer = cheer[random.randint(0, len(cheer) - 1)]

print(f'{random_presenter}!!! {random_cheer}')
