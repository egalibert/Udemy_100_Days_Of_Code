# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]

file1_list = []
file2_list = []

with open("file1.txt", "r") as file1:
	for item in file1:
		file1_list.append(item.strip())

with open("file2.txt", "r") as file2:
	for item in file2:
		file2_list.append(item.strip())

print(file1_list)
print(file2_list)

result = [int(num) for num in file1_list if num in file2_list]
print(result)