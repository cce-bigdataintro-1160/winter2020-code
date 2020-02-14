original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Solution using for and append in a new list
evens = []
odds = []
for i in original_list:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

# Solution using slicing
# evens = original_list[1::2]
# odds = original_list[::2]

# Solution using filter function
# evens = list(filter(lambda x: x % 2 == 0, original_list))
# odds = list(filter(lambda x: x % 2 != 0, original_list))

print(f'evens: {evens}')
print(f'odds: {odds}')
