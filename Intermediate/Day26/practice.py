# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

# print(numbers, new_numbers)

# name = "Elliot"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n * 2 for n in range(1, 5)]

# print (new_list)

names = ["Alex", "Beth", "Dave", "Caroline", "Eleanor", "Freddie"]

new_list = [name.upper() for name in names if len(name) > 4 ]
print (new_list)