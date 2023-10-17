from art import logo, vs
from game_data import data
import random

import os
def clear():
	os.system("clear")

print(logo)

def check_result(answer, compare_a, compare_b):
	result = False
	if answer == 'a' and compare_a['follower_count'] > compare_b['follower_count']:
		return True
	elif answer == 'a' and compare_a['follower_count'] < compare_b['follower_count']:
		return False
	elif answer == 'b' and compare_a['follower_count'] < compare_b['follower_count']:
		return True
	elif answer == 'b' and compare_a['follower_count'] > compare_b['follower_count']:
		return False

def choose_new_item():
	number = random.randint(0, len(data) - 1)
	return (data[number])

def game():
	score = 0
	compare_a = choose_new_item()
	compare_b = choose_new_item()
	while(1):
		result = False

		print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']} ")
		print(vs)
		print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']} ")

		answer = input("Who has more followers? Type 'A' or 'B': ").lower()
		result = check_result(answer, compare_a, compare_b)
		if result == True:
			score += 1
			clear()
			print(logo)
			print(f"You're right! Current score: {score}")
			compare_a = compare_b
			compare_b = choose_new_item()
		else:
			break
	
	clear()
	print(logo)

	print(f"Sorry that's wrong. Final score: {score}")

game()