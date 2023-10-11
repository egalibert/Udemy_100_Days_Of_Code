import random

p1_choice = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
computer = random.randint(0, 2)

print(f"Computer choice {computer}")