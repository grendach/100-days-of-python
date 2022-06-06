# List comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)
results = [n for n in numbers if n % 2 == 0]
print(results)

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

file_results = [int(num) for num in file_1_data if num in file_2_data]
print(file_results)

# Dictionary comprehension
import random
names = ['Dmytro', 'Sergii', 'Igor', 'Yana']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
