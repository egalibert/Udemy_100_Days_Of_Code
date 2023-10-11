import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

p1_choice = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player = int(p1_choice)
computer = random.randint(0, 2)
choices = [rock, paper, scissors]
print(f"You chose:")
print(f"{choices[player]}")

print(f"Computer chose:")
print(f"{choices[computer]}")

if player == 0 and computer == 2:
	print(f"You win!")
elif computer == 0 and player == 2:
	print(f"You lose..")
elif player >= 3 or player < 0:
	print(f"You typed an invalid command, you lose")
elif player > computer:
	print(f"You win!")
elif computer > player:
	print(f"You lose..")
elif player == computer:
	print(f"It's a draw")