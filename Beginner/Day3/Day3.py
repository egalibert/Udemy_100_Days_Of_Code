# EX1
# Write a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.

number = int(input())

if (number % 2 == 0):
  print(f"This is an even number.")
else:
  print(f"This is an odd number.")

# EX2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

height = float(input())
weight = int(input())
result = weight / (height * height)
if result < 18.5:
  print(f"Your BMI is {result}, you are underweight")
elif result > 18.5 and result < 25:
  print(f"Your BMI is {result}, you have a normal weight.")
elif result >= 25 and result < 30:
  print(f"Your BMI is {result}, you are slightly overweight.")
elif result >= 30 and result < 35:
  print(f"Your BMI is {result}, you are obese.")
elif result > 35:
  print(f"Your BMI is {result}, you are clinically obese")

#   EX3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, 
# with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

year = int(input())

if (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print(f"Leap year")
    else:
      print(f"Not leap year")
  else:
    print(f"Leap year")
else:
  print(f"Not leap year")

# EX4
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

total = 0
if size == 'L':
  total += 25
elif size == 'M':
  total += 20
elif size == 'S':
  total += 15

if add_pepperoni == 'Y':
  if size == 'L':
    total += 3
  elif size == 'M':
    total += 3
  elif size == 'S':
    total += 2

if extra_cheese == 'Y':
  total += 1

print(f"Your final bill is: ${total}.")

# EX5
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name1 = name1.lower()
name2 = name2.lower()

total_1 = 0
total_2 = 0
word1 = "true"
word2 = "love"

total_1 += name1.count("t")
total_1 += name1.count("r")
total_1 += name1.count("u")
total_1 += name1.count("e")

total_1 += name2.count("t")
total_1 += name2.count("r")
total_1 += name2.count("u")
total_1 += name2.count("e")

total_2 += name1.count("l")
total_2 += name1.count("o")
total_2 += name1.count("v")
total_2 += name1.count("e")

total_2 += name2.count("l")
total_2 += name2.count("o")
total_2 += name2.count("v")
total_2 += name2.count("e")

string = str(total_1) + str(total_2)
result = int(string)

if result < 10 or result > 90:
	print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
	print(f"Your score is {result}, you are alright together.")
else:
	print(f"Your score is {result}.")

