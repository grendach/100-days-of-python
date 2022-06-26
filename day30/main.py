# Multiple error types are exiscts:

# FileError
# with open("data.txt", "r") as data_file:
#     data_file.write("dupa")

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Apple", "Pear", "Banana"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Try Except Else Finally Raise exception
# try:
#     file = open("dupa.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["keysdf"])
# except FileNotFoundError:
#     file = open("dupa.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("That is an error that I made up")

# Raise you own exceptions:
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")

# bmi = weight / height ** 2
# print(bmi)

# IndexError Handling
# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
    
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")

# make_pie(4)

# KeyError Handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
        
print(total_likes)
