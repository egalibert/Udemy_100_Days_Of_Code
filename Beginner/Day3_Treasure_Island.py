print("""\
____________________________________________________________________
/ \-----     ---------  -----------     -------------- ------    ----\
\_/__________________________________________________________________/
|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
|  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
| | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
|  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
|~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
|  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
|~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
|    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
| ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
|  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
|~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
| ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
|~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
| ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
|~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
| ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
/ \----- ----- ------------  ------- ----- -------  --------  -------\
\_/__________________________________________________________________/
	  		""")

print(f"Welcome to the Treasure Island!")
print(f"Your mission is to find the hidden treasure")
decision_1 = input(f"You find yourself at an intersection. Which way do you wish to go? Type 'LEFT' or 'RIGHT'\n")
if (decision_1.upper() == "LEFT"):
	decision_2 = input(f"You survived. Now you see a goat and a rabbit. Which one do you pet? Type 'RABBIT' or 'GOAT'\n")
	if (decision_2.upper() == "GOAT"):
		final_decision = input(f"The goat brings you to two people. Messi and Ronaldo. Which one do you give the goat to? Type 'MESSI' or 'RONALDO'\n")
		if (final_decision.upper()  == "RONALDO"):
			print(f"Well done! Ronaldo gives you his keys his Bugatti and you can espace and keep it!\n")
		else:
			print(f"You chose poorly. Messi stabs you. You die. Ggs.")
	else:
		print(f"The rabbit was sick and bit you. You died. Ggs.")

else:
	print(f"Oh no a venoumos snake bit you. You died. Ggs.")

