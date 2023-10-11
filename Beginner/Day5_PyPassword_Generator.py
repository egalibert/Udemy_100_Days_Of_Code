import random

print(f"Welcome to the PyPassword Generator!")
letter_count = int(input(f"How many letter would you like in your password?\n"))
symbol_count = int(input(f"How many symbols?\n"))
number_count = int(input(f"How many numbers?\n"))

# letter_count = 14
# symbol_count = 3
# number_count = 4

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

total_len = letter_count + number_count + symbol_count
string = ""
i = 0
while i < total_len:
	choice = random.randint(0, 2)
	if (choice == 0 and letter_count > 0):
		index = random.randint(0, len(letters) - 1)
		string += letters[index]
		letter_count -= 1
		i += 1
	elif (choice == 1 and number_count > 0):
		index = random.randint(1, len(numbers) - 1)
		string += numbers[index]
		number_count -= 1
		i += 1
	elif (choice == 2 and symbol_count > 0):
		index = random.randint(1, len(symbols) - 1)
		string += symbols[index]
		symbol_count -= 1
		i += 1
	print(f"value of i = {i}, random number is = {choice}")

print(f"{string}")
