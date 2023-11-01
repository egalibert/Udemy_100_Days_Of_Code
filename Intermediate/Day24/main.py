# with open("my_file.txt") as file:
# 	content = file.read()
# 	print(content)

# with open("my_file.txt", "w") as file:
# 	file.write("New text.")

with open("my_file.txt", "a") as file:
	file.write("New text.")