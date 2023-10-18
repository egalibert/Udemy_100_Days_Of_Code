from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# def calculate_coins():
# 	total = 0
# 	total += int(input(f"How many quarters?: ")) * 0.25
# 	total += int(input(f"How many dimes?: ")) * 0.1
# 	total += int(input(f"How many nickels?: ")) * 0.05
# 	total += int(input(f"How many pennies?: ")) * 0.01
# 	return (total)

foodlist = Menu()
c_machine = CoffeeMaker()
m_machine = MoneyMachine()

print(f"Welcome to the Coffee Machine!")
while(1):
	choice = input(f"Choose a drink. Type {foodlist.get_items()}: ")
	if choice == "report":
		c_machine.report()
		m_machine.report()
	if choice == "off":
		exit()
	coffee = foodlist.find_drink(choice) # Coffee becomes MenuItem
	if c_machine.is_resource_sufficient(coffee) == False:
		print(f"Not enough ingredients, Sorry!")
		continue
	m_machine.make_payment(coffee.cost)
	c_machine.make_coffee(coffee)

	# print(coffee.name)