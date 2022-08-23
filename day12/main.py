########### Scope ############

# apples = 1 # Global scope

# def how_many_apples():
#     # apples = 2 # Local scope 
#     global apples # changing global variable
#     apples = 10
#     print(f"You have {apples} apples")

# how_many_apples()  
# print(f"You have {apples} apples")

###### guess number game ##########
import random
from art import logo
print(logo)
print(
"""Welcome to Guess Number game
I'm thinking about number from 1 to 100     
""")

NUMBER = random.randint(0, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5
print(f"Pss.. your number is: {NUMBER}")

def set_difficulty():
    user_choise = input("Choose your lever: type 'easy' or 'hard': ")
    if user_choise == "easy":
        return EASY_LEVEL 
    elif user_choise == "hard":
        return HARD_LEVEL

def game():
    attemps = set_difficulty()
    while attemps > 0:
        print(f"You have {attemps} attemps lef")
        user_input = int(input("Make a guess: "))
        if user_input > NUMBER:
            attemps -= 1
            print("Too high")
        elif user_input < NUMBER:
            attemps -= 1
            print("Too low")
        elif user_input == NUMBER:
            print("You've won!!!")
            break
    print("YOu don't have any more chanses")       

game()

######### Solution suggested by tutor #####
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()
