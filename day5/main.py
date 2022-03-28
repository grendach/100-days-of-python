# LOOPS
fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# Avarage Height
all_height = 0
for height in student_heights:
    all_height += height

all_students = 0
for student in student_heights:
    all_students += 1
    
print(round(all_height/all_students))

# Highest Score
max_score = 0
for score in student_scores:
    if score >= max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")


# Adding Even Numbers
even_numbers = 0
for number in range(2, 101, 2):
    even_numbers += number

print(even_numbers)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

your_password = []
your_letters = ""
your_numbers = ""
your_symbols = ""

  
for letter in range(1, nr_letters + 1):
    your_password.append(random.choice(letters))

for number in range(1, nr_numbers + 1):
    your_password.append(random.choice(numbers))

for symbol in range(1, nr_symbols +1):
    your_password.append(random.choice(symbols))

random.shuffle(your_password)
password = ""
for char in your_password:
  password += char
print(password)
