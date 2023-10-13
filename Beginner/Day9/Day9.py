# EX1

# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
	# print(key, student_scores)
	if student_scores[key] >= 91:
		student_grades[key] = "Outstanding"
	elif student_scores[key] >= 81:
		student_grades[key] = "Exceeds Expectations"
	elif student_scores[key] >= 71:
		student_grades[key] = "Acceptable"
	else:
		student_grades[key] = "Fail"

print(student_grades)

# EX2

# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Your job is to create a function that can add new countries to this list.

# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
	new_dict = {}
	new_dict["country"] = country
	new_dict["visits"] = visits
	new_dict["cities"] = list_of_cities
	travel_log.append(new_dict)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")