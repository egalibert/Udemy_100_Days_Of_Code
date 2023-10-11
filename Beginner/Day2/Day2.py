# EX1
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

str_a = str(two_digit_number)
num1 = int(str_a[0])
num2 = int(str_a[1])

result = num1 + num2
print(f"{result}")

# EX2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input()
weight = input()

result = int(weight) / (float(height) ** 2)
print(f"{int(result)}")

# EX3
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.

age = input()
age_as_int = int(age)

years_left = 90 - age_as_int
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left.")

# EX4