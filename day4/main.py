import random
import my_module

#RANDOM INT and FLOAT
rand_int = random.randint(1, 100)
print(rand_int)

print(my_module.pi)

random_float = random.random() * 5
print(random_float)

choise = random.randint(0, 1)

if choise == 1:
    print("Heads")
else:
    print("Tails")

# List

regions_of_ukraine = ["Poltava", "Kyiv", "Vinnytsya", "Zhytomyr"]

print(regions_of_ukraine[-2])
regions_of_ukraine[1] = "Lviv"
regions_of_ukraine.append("Kyiv")
regions_of_ukraine.extend(["Kharkiv", "Dnipro"])

print(regions_of_ukraine)

# List of lists
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
colomn = int(position[0])
row = int(position[1])

map[row-1][colomn-1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
