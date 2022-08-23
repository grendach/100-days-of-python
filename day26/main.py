# List comprehension
#1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)
#2
results = [n for n in numbers if n % 2 == 0]
print(results)

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()
#3
file_results = [int(num) for num in file_1_data if num in file_2_data]
print(file_results)

# Dictionary comprehension
#1
import random
names = ['Dmytro', 'Sergii', 'Igor', 'Yana']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

#2
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
#3
sentence = "What is the Airspeed Velocity of an Unladen Swallow ?"
result = {word:len(word) for word in sentence.split()}
print(result)
#4
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c*9/5) for (day, temp_c) in weather_c.items()}
print(weather_f)
