from art import logo
import random
import os
def clear():
	os.system("clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_playing = False

def deal_a_card():
	card = cards[random.randint(0, 12)]
	return card

def first_deals():
	player_hand.append(deal_a_card())
	player_hand.append(deal_a_card())
	dealer_hand.append(deal_a_card())

def print_scores():
	print(f"\tYour cards: {player_hand}, current score: {calculate_score(list=player_hand)}")
	print(f"\tComputer's first card: {dealer_hand}")

def final_print():
	print(f"\tYour final hand: {player_hand}, final score: {calculate_score(list=player_hand)}")
	print(f"\tComputer's final cards: {dealer_hand}, final score: {calculate_score(list=dealer_hand)}")

def calculate_score(list):
	if 11 in list and sum(list) > 21:
		list.remove(11)
		list.append(1)
	return sum(list)

def game_result():
	if sum(player_hand) > 21:
		print(f"You went over, you lose.")
	elif sum(dealer_hand) > 21:
		print(f"Opponent went over. You win!")
	elif sum(player_hand) < sum(dealer_hand):
		print(f"You lose..")
	elif sum(dealer_hand) == sum(player_hand):
		print(f"It's a draw")
	else:
		print("You win!")


while(1):
	keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
	if keep_playing != 'y':
		break

	clear()
	print(logo)

	player_hand = []
	dealer_hand = []
	first_deals()
	if sum(player_hand) == 21:
		print(f"Blackjack, you win!")
		continue
	print_scores()

	while(1):
		hit_or_fold = input("Type 'y' to get another card, type 'n' to pass: ")
		if hit_or_fold == 'n':
			break
		player_hand.append(deal_a_card())
		if sum(player_hand) > 21:
			break
		print_scores()
	while calculate_score(list=dealer_hand) < 17 and sum(dealer_hand) != 21:
		dealer_hand.append(deal_a_card())
	final_print()
	game_result()
