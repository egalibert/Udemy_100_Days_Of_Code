# EX1

# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0

for i in range(0, len(student_heights)):
  total += student_heights[i]

print(f"total height = {total}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(total / len(student_heights))}")

# EX2

# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

best = 0
for i in range(0, len(student_scores)):
  if student_scores[i] > best:
    best = student_scores[i]

print(f"The highest score in the class is: {best}")

# EX3

# You are going to write a program that calculates the sum of all the even numbers from 1 to X.
# If X is 100 then the first even number would be 2 and the last one is 100:

target = int(input()) # Enter a number between 0 and 1000
total = 0

for number in range(0, target + 1, 2):
  total += number

print(f"{total}")

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"