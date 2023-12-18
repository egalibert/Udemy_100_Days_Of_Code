from logo import logo

board_up = "| 1 | 2 | 3 |"
board_mid = "| 4 | 5 | 6 |"
board_low = "| 7 | 8 | 9 |"
line =     "-------------"
open = []

# Printing the board out for players to see
def print_board():
	print(f"{board_up}\n{line}\n{board_mid}\n{line}\n{board_low}\n")

def play_X():
	print("Player X turn\n")
	print_board()
	#Checking number is a valid one and not already chosen
	number = input("Type a number between 1 and 9 to choose where to place your mark: ")
	number_as_int = int(number)

	if number_as_int < 1 or number_as_int > 9:
		print("Invalid choice, you lose your turn")

	if int(number) not in open:
		open.append(number)
		# Checking which spot player chose
		if number_as_int > 0 and number_as_int < 4:
			global board_up
			board_up = board_up.replace(number, 'X')

		elif number_as_int > 3 and number_as_int < 7:
			global board_mid
			board_mid = board_mid.replace(number, 'X')

		elif number_as_int > 6 and number_as_int < 10:
			global board_low
			board_low = board_low.replace(number, 'X')
	else:
		print("Place is taken, you lose your turn")

# Player O's move 
def play_O():
	print ("\nPlayer O turn\n")
	print_board()
	#Checking number is a valid one and not already chosen
	number = input("Type a number between 1 and 9 to choose where to place your mark: \n")
	number_as_int = int(number)

	if number_as_int < 1 or number_as_int > 9:
		print("Invalid choice, you lose your turn")

	if int(number) not in open:
		open.append(number)
		# Checking which spot player chose
		if number_as_int > 0 and number_as_int < 4:
			global board_up
			board_up = board_up.replace(number, 'O')
		elif number_as_int > 3 and number_as_int < 7:
			global board_mid
			board_mid = board_mid.replace(number, 'O')
		elif number_as_int > 6 and number_as_int < 10:
			global board_low
			board_low = board_low.replace(number, 'O')
	else:
		print("Place is taken, you lose your turn")

# Checking if there is 3 marks in a row and a winner is found
def check_winner(player_mark):
	# Check rows
	if (board_up.count(player_mark) == 3 or
			board_mid.count(player_mark) == 3 or
			board_low.count(player_mark) == 3):
		return True

	# Check columns
	for i in range(3):
		if (board_up[i * 4 + 2] == player_mark and
				board_mid[i * 4 + 2] == player_mark and
				board_low[i * 4 + 2] == player_mark):
			return True

	# Check diagonals

	if (board_up[2] == player_mark and
			board_mid[6] == player_mark and
			board_low[10] == player_mark):
		return True
	elif (board_up[10] == player_mark and
			board_mid[6] == player_mark and
			board_low[2] == player_mark):
		return True

	return False

# The rotation of the game
def play_game():
	print("Welcome to Tic Tac Toe\n")
	print(logo)
	print("\n")
	print_board()

	choice = input("Type start to begin: ").lower()

	if choice != "start":
		return

	print("X starts\n")
	while True:
		play_X()
		print("next player\n")

		if check_winner('X'):
			print("Player X wins!\n")
			print_board()
			break

		play_O()
		print("next player\n")

		if check_winner('O'):
			print("Player O wins!\n")
			print_board()
			break
		print("game is running")

play_game()
