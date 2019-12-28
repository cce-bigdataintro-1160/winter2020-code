# Numbers in Python can be of two types: Integers and Floats

# They're very important as many ML algorithms can only deal
# with numbers and will ignore/crash on any other kind of input
# because they're based complex math algorithms

# Integers have unbound size in Python 3!
lucky_number = 13
universe_number = 42

# Floats are numbers that have a decimal point!
pi = 3.14
a_third = 0.333

# We can do basic math calculations using the operators / + - * % and **
times_two = lucky_number * 2
square = universe_number ** 2
mod = 3 % 2 # results in the remainder of the division of 3 by 2 (1 in this case)

# In the example below we calculate the area of a circle
radius = 50
area_of_circle = pi * (radius ** 2)

print(area_of_circle)
