from art import logo
import random

player_lives = 0
hidden_number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
	player_lives = 10
else:
	player_lives = 5

while player_lives > 0:
	print(f"You have {player_lives} attempts remaining to guess the number.")
	guess = int(input("Make a guess: "))
	if hidden_number == guess:
		print(f"You got it! The answer was {hidden_number}!")
		exit()
	elif hidden_number > guess:
		print("Too low.")
		print("Guess again")
	else:
		print("Too high.")
		print("Guess again")
	player_lives -= 1

print("You've run out of guesses, you lose")