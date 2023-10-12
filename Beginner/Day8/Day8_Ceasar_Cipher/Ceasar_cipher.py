from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", "!", "?", "@", ",", "."]
print(logo)
print(f"Welcome to Cesar Cipher!")

def caesar(direction, text, shift):
	cipher_text = ""
	if direction == "decode":
		shift *= -1
	for letter in text:
		if letter in numbers:
			cipher_text += letter
		else:
			position = alphabet.index(letter)
			new_position = position + shift
			if new_position > len(alphabet):
				new_position -= len(alphabet)
			cipher_text += alphabet[new_position]
		
	print(f"Here's the {direction}d result: {cipher_text}")

should_continue = True
while should_continue:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n")
	if direction == "exit":
		break
	elif direction != "encode" and direction != "decode":
		print(f"Invalid input!")
		continue
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(direction, text, shift)
	
	result = input("Do you wish to continue? type 'yes' or 'no: ")
	if result == "no":
		should_continue = False
		print(f"Goodbye!")