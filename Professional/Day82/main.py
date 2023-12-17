def text_to_morse(text):
	morse_code_dict = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	'Y': '-.--', 'Z': '--..',
	
	'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
	'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
	
	'.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
	'/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
	';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
	'"': '.-..-.', '$': '...-..-', '@': '.--.-.',
	' ': '/'
	}
	new_string = ""
	for letter in text:
		new_string += morse_code_dict[letter]
	print(new_string)


print("Welcome to morse Translator")

while(1):
	text = input('Give a string to turn into morse: ').upper()
	text = "aaa".upper()
	text_to_morse(text)
	choice = input("Want to do another type yes to continue no to exit: ").lower()
	if choice == "no":
		break
	else:
		continue