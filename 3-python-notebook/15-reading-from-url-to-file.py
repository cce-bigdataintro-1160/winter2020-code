#!/usr/bin/env python3

import urllib.request

# https://github.com/public-apis/public-apis

# url = 'https://www.theweathernetwork.com/ca/weather/quebec/montreal/'
# url = 'http://donnees.ville.montreal.qc.ca/dataset/6502942d-788a-43ff-b935-eb7b7d8b58cd/resource/01f91df2-6ed9-47b2-ba85-e6bc9236ac73/download/compteur-eau.csv'
# url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'
# url = 'http://donnees.ville.montreal.qc.ca/dataset/5866f832-676d-4b07-be6a-e99c21eb17e4/resource/2cfa0e06-9be4-49a6-b7f1-ee9f2363a872/download/requetes311.zip'
url = 'https://dog.ceo/api/breeds/image/random'


response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

my_file = open('output_file', 'w+')

my_file.write(text + '\n')

# It's important to close files after they've been used to avoid a `resources leak` on the os
my_file.close()

