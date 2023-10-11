# After you have written your code, you should run your program and it should print the following:

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

print(f"Day 1 - Python Print Function")
print(f"The function is declared like this:")
print(f"print('what to print')")

# When you run your program, it should print the following:

# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash

print(f"Day 1 - String Manipulation")
print(f'String Concatenation is done with the "+" sign.')
print(f'e.g. print("Hello " + "world")')
print(f"New lines can be created with a backslash and n.")

# Write a program that prints the number of characters in a name.

name = input()
strlen = len(name)
print(f"{strlen}")

# This program takes two inputs. The first input is stored in a variable called a.
# The second input is stored in a variable called b.

# Write a program that switches the values stored in the variables a and b.

a = input()
b = input()

c = a
a = b
b = c