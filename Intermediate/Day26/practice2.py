import random

names = ["Alex", "Beth", "Dave", "Caroline", "Eleanor", "Freddie"]

students_score = {student:random.randint(1, 100) for student in names}

print(students_score)

passed_students = {student:score for (student, score) in students_score.items() if score > 60}