# EX1
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math

def paint_calc(height, width, cover):

	result = (height * width) / cover
	# print(f"{result}, {math.ceil(result)}")
	print(f"You'll need {math.ceil(result)} cans of paint")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# EX2

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

def prime_checker(number):
	if number % number == 0:
		if number % 2 == 0:
			print(f"It's not a prime number.")
		elif number % 3 == 0:
			print(f"It's not a prime number.")
		elif number % 4 == 0:
					print(f"It's not a prime number.")
		else:
			print(f"It's a prime number.")

n = int(input())
prime_checker(number=n)