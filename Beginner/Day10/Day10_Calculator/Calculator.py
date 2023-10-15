from art import logo

def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def divide(n1, n2):
	return n1 / n2

def multiply(n1, n2):
	return n1 * n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

# function = operations["+"]

def calculator():
	print(logo)
	num1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)
	while(1):
		chosen_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		calculation_function = operations[chosen_symbol]
		answer = calculation_function(num1, num2)

		print(f"{num1} {chosen_symbol} {num2} = {answer}")
		continue_input = input(f"Type 'y' to continue with calculating with {answer} or type 'n' to start a new calculation.: ")
		if continue_input != 'y':
			calculator()
			break
		num1 = answer

calculator()


# chosen_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number: "))
# calculation_function = operations[chosen_symbol]
# second_answer = calculation_function(calculation_function(num1, num2), num3)

# print(f"{answer}, {chosen_symbol} {num3} = {second_answer}")