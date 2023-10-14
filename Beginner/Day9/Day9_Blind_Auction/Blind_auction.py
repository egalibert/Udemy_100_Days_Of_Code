from art import logo
import os
def clear():
	os.system("clear")
	
bidders = {}
game_over = True
winner = ""
biggest = 0
	
print(logo)
print("Welcome to the secret auction program!")

while (game_over):
    name = input("What is your name: ")
    bid = input("what's your bid?: ")
    bidders[name] = int(bid)

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "yes":
        clear()
        # continue
    else:
        for key in bidders:
            if bidders[key] > biggest:
                winner = key
                biggest = bidders[key]
        game_over = False
        print(f"The winner is {winner} with a bid of ${biggest}\n")
        print(f"Thank you for playing!")