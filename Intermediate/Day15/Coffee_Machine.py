from resources import MENU, resources

def report():
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}ml")
	print(f"Money: {resources['money']}$")

def calculate_quarters(amount):
	total_value = amount * 0.25
	return total_value

def calculate_dimes(amount):
	total_value = amount * 0.10
	return total_value

def calculate_nickels(amount):
	total_value = amount * 0.05
	return total_value

def calculate_pennies(amount):
	total_value = amount * 0.01
	return total_value

def calculate_coins():
	total_coins = 0
	total_coins += calculate_quarters(amount = int(input(f"How many quarters?: ")))
	total_coins += calculate_dimes(amount = int(input(f"How many dimes?: ")))
	total_coins += calculate_nickels(amount = int(input(f"How many nickels?: ")))
	total_coins += calculate_pennies(amount = int(input(f"How many pennies?: ")))
	return total_coins

def check_ingredients(coffee):
	if coffee == "espresso":
		if MENU[coffee]["ingredients"]["water"] > resources["water"]:
			print("Sorry there is not enough water")
			return False
		elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
			print("Sorry there is not enough coffee")
			return False
		else:
			return True
	else:
		if MENU[coffee]["ingredients"]["water"] > resources["water"]:
			print("Sorry there is not enough water")
			return False
		elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
			print("Sorry there is not enough coffee")
			return False
		elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
			print("Sorry there is not enough milk")
			return False
		else:
			return True


def coffee_machine():
	good_to_make = True
	while 1:
		choice = input(f"What would you like? (espresso/latte/cappucino): ")
		if choice == "off":
			exit()
		if choice != "report":
			good_to_make = check_ingredients(coffee=choice)
		if good_to_make == False:
			continue
		if choice == "report":
			report()
		elif choice == 'espresso' or choice == "latte" or choice == "cappucino":
			total = calculate_coins()
			# print(total)
			if total < MENU[choice]["cost"]:
				print(f"Sorry that's not enough money. Money refunded.")
				continue
			else:
				print(f"Here is ${MENU[choice]['cost'] - total} in change.")
				print(f"Here is your {choice} ☕. Enjoy!")
				resources["money"] += MENU[choice]["cost"]
				if choice == "espresso":
					resources["water"] -= MENU[choice]["ingredients"]["water"]
					resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
					continue
				else:
					resources["water"] -= MENU[choice]["ingredients"]["water"]
					resources["milk"] -= MENU[choice]["ingredients"]["milk"]
					resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
					continue


coffee_machine()