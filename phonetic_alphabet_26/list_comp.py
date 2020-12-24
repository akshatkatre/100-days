import random

students = ['Alex', 'Kamal', 'Joe', 'Don', 'Ramesh']

student_scores = {student: random.randint(1, 100) for student in students}

print(student_scores)

passed_students = {key: score for key,score in student_scores.items() if score >= 50}

print(passed_students)
