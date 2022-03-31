# FUNCTION with input
def greet(name):
    print(f"hello {name}")
    print(f"how do you do {name} ?")
    print("How is the weather today ?")

greet("Dmytro")

# Functioin with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"{name} located in {location}")
# using positional argument
greet_with("Yana", "Zhdany")
# using keyword argument
greet_with(location="Kyiv", name="Dmytro")

#Write your code below this line 👇

import math
def paint_calc(height, width, cover):
    cans = math.ceil((height*width)/cover)
    print(f"You'll need {cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
