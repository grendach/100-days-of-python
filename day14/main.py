## DAY 14 higher-lower game
import random
from re import A
from art import logo, vs
from game_data import data

# get random account data
def get_random_data():
    """ Get random accout data """
    return random.choice(data)

def format_account_data(account):
    """ Format account info """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"Account of: {name}, is {description}, from {country}"

    
def check_choise(guess, account_a, account_b):
    """ Check amount of account followers """
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    continue_game = True
    account_a = get_random_data()
    account_b = get_random_data()
    score = 0
    print(logo)
    

    while continue_game:
        account_a = account_b
        account_b = get_random_data()
        while account_a == account_b:
            account_b = get_random_data()
            
        print(f"A: {format_account_data(account_a)}")
        print(vs)
        print(f"B: {format_account_data(account_b)}")
        
        guess = input("Who has more followers, type A or B: ").lower()

        is_correct = check_choise(guess, account_a, account_b)
        if is_correct:
            score += 1
            print(f"That's correct. Your score: {score} ")
        else:
            continue_game = False
            print(f"You've lost. Your score: {score} ")
        
game()
