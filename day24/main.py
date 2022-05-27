PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

print(names)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as outgoing_email:
            outgoing_email.write(new_letter)
