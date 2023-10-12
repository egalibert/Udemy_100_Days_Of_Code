import random
from Hangman_art import logo, stages
from Hangman_words import word_list
import os
def clear():
	os.system("clear")

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
display_list = []
guess_list = []
index = 0
word_legth = len(chosen_word)
lives = 6
game_over = False

for i in range(word_legth):	
	display_list.append("_")
	
# print(f"{logo}\n")

print(f"Welcome to Hangman game. You have 6 lives to guess the mystery word!\n")

while(game_over != True):
	print(f"{logo}\n")
	print(f"You have {lives} lives left!\n")
	print(f"{stages[lives]}")
	# print(f"{chosen_word}")
	guess = input(f"Guess a letter: ").lower()
	clear()
	guess_list.append(guess)
	if (guess == "stop"):
		break
	for position in range(word_legth):
		letter = chosen_word[position]
		if guess == letter:
			display_list[position] = letter
			print(f"Correct!\n")
			
	print(f"Current situation: {display_list}\n")
	print(f"Letters guessed {guess_list}\n")
	
	if guess not in chosen_word:
		lives -= 1
		print(f"The letter is not in the word..")
		# print(f"{stages[lives]}")
		if lives == 0:
			game_over = True
			print(f"{logo}\n")
			print(f"You're out of lives, you lose. GG.")
			print(f"The mystery word was {chosen_word}")


	if "_" not in display_list:
		print(f"You solved the mystery word! Congratualtions!")
		game_over = True