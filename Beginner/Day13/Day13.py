# EX1

# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

number = int(input()) # Which number do you want to check?

if number % 2 == 0: # This was with one = sign.
  print("This is an even number.")
else:
  print("This is an odd number.")

# EX2

year = int(input()) # This had no Int in it

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year.")
		else:	
			print("Not leap year.")
	else:
		print("Leap year.")
else:
	print("Not leap year.")

# EX3

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: # or instead of and
    print("FizzBuzz")
  elif number % 3 == 0: # all if statements no elif's
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) # Had brackets around number