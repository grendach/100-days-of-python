# Data Types
# Strings
print("Hello"[4])
print("123" + "456")

# Integers
print(123+456)
print(123_456_789 + 1) # _ ignored, just for more readability

# Float
print(3.4566)

#Bool
# true
# false


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
in_str = str(two_digit_number)
output = int(in_str[0]) + int(in_str[1])
print(output)


# Mathematical Operations
3 + 5
4 - 2
3 * 2
6 / 3
2 ** 3

# PEMDASLR
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)

# BMI index
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = int(weight)
bmi = weight / (height ** 2)
print(int(bmi))

# F String

score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning {isWinning}")

# Life in Weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
death_in_years = 90 - int(age)
days = death_in_years*365
weeks = death_in_years*52
months = death_in_years*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# TIP CALCULATOR
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? 12 "))
people = float(input("How many people to split the bill? "))

tip = bill * tip_percent/100
total_bill = bill + tip
bill_per_person = total_bill / people
final_result = round(bill_per_person, 2)
final_result = "{:.2f}".format(final_result)
print(f"Each person should pay: ${final_result}")
