# We'll use a module called random to generate a random integer
import random
random_number = random.randint(0, 100)

# We then use conditionals to print different results according to the generated number
if random_number == 100:
    print('You won the great prize')
elif random_number >= 50:
    print('You won a small prize')
elif random_number > 25:
    print('You didn\'t get anything! But play again for free!')
else:
    print('You won nothing')
