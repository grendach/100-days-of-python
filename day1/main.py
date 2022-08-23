# Worknig with variables.
print("Day 1 - String Manipulation")
print("String Concatenation is done with the" + ' "+" sign.')
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n."))

# This code prints the number of characters in a user's name.
print(len(input("What is your name? ")))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
new_a = b
new_b = a

a = new_a
b = new_b



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#1. Create a greeting for your program.
print("Welcome to Band Name Generator.\n")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up it?\n")
print(city)
#3. Ask the user for the name of a pet.
pet_name = input("What's name of your pet? ")
print(pet_name)

#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet_name
print(band_name)