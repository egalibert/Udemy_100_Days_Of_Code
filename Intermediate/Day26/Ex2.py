# In this list comprehension exercise you will practice using list comprehension to
# filter out the even numbers from a series of numbers.

# First, use list comprehension to convert the list_of_strings to a list of integers.

# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers.

list_of_strings = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_ints = [ int(num) for num in list_of_strings]

result = [num for num in list_of_ints if num % 2 == 0]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"


print(result)