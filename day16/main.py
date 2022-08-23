from turtle import Turtle, Screen
from prettytable import PrettyTable # install it: pip3 install prettytable

timmy = Turtle()

my_screen = Screen()
timmy.shape("turtle")
timmy.color("coral")
timmy.fd(100)
print(timmy, my_screen.canvheight)
my_screen.exitonclick()

table1 = PrettyTable()
# 1st way to add table
table1.field_names = ["Pockemon name", "Type"]
table1.add_row(["Pikachu", "Elektric"])
table1.add_row(["Squirtle", "Water"])
table1.add_row(["Charmander", "Fire"])
table1.align = "l"

# 2nd way to add table
table2 = PrettyTable()
table2.add_column("Pockemon name", ["Pikachu", "Squirtle","Charmander" ])
table2.add_column("Type", ["Elektric","Water", "Fire"])

print(table1)
print(table2)
