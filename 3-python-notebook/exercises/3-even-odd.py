even_odd = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

for x in even_odd:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(f'Evens: {even}')
print(f'Odds: {odd}')

print(f'Evens: {even_odd[1::2]}')
print(f'Odds: {even_odd[::2]}')

