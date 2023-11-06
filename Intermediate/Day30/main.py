# EX1

# We've got some buggy code. Try running the code.
# The code will crash and give you an IndexError. 
# This is because we're looking through the list of fruits for an
# index that is out of range.

# Objective
# Use what you've learnt about exception handling to
# prevent the program from crashing. If the user enters 
# something that is out of range just print a default output of "Fruit pie".

fruits = eval(input())

def make_pie(index):
	try:
		fruit = fruits[index]
		print(fruit + " pie")
	except IndexError:
		print("fruitpie")

make_pie(4)

# EX2

# We've got some buggy code, try running the code. 
# The code will crash and give you a KeyError. 
# This is because some of the posts in the facebook_posts don't have any "Likes".

# Objective
# Use what you've learnt about exception handling to prevent the program from crashing.

facebook_posts = eval(input())

total_likes = 0
for post in facebook_posts:
	try:
		total_likes = total_likes + post['Likes']
	except KeyError:
		pass
	
print(total_likes)