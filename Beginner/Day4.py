# EX1

# You are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails".

import random

number = random.randint(0, 1)
if number == 0:
	print(f"Heads")
else:
	print(f"Tails")

# EX2

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

import string
import random
names = string.split(", ")

import random

rand_number = random.randint(0, len(names) - 1)
print(f"{names[rand_number]} is going to buy the meal today!")

# EX3
# You are going to write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0]

if letter == "A":
	index = 0
elif letter == "B":
	index = 1
elif letter == "C":
	index = 2

number_index = int(position[1]) - 1
map[number_index][index] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")