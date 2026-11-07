import time
from prettytable import PrettyTable

from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html
# https://docs.python.org/3/library/turtle.html#turtle-methods-and-functions

# ernesto = Turtle()
# ernesto.shape("turtle")
# ernesto.color("cyan2")
#
# print(ernesto)
#
# my_screen = Screen()
# time.sleep(1)
# print(my_screen.canvheight) # access attribute
# ernesto.forward(100)

# my_screen.exitonclick()

table = PrettyTable()
times = []
for i in range(5):
    times.append(time.strftime("%H:%M:%S"))
    time.sleep(3)

pokemon_names = ["Pikachu", "Squirtle", "Charmander"]
pokemon_types = ["Electric", "Water", "Fire"]

table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", pokemon_types)
table.vrules = False
table.align  = "l"
print(table)