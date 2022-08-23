##### BMI 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight/(height**2)))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

### LEAP year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

## PIZZA 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0
if size == "S":
    price += 15    
elif size == "M":
    price += 20
else:
    price += 25
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")


## LOVE Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

two_names = (name1 + name2).lower()

t = two_names.count("t")
r = two_names.count("r")
u = two_names.count("u")
e = two_names.count("e")

fisrt_number = t + r + u + e

l = two_names.count("l")
o = two_names.count("o")
v = two_names.count("v")
e = two_names.count("e")

secont_nubmer = l + o + v + e

score = int(str(fisrt_number)+str(secont_nubmer))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
