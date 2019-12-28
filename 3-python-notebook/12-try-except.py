#!/usr/bin/env python3

provided_string = input("Please provide a number")

try:
    provided_int = int(provided_string)
except ValueError:
    print(f'You have to provide a number! Using 0 instead')
    provided_int = 0


print(f'The double of {provided_int} is {provided_int * 2}')