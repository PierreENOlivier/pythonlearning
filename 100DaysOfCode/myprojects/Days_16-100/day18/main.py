import turtle
from turtle import Turtle, Screen
from move import *
from utils import *
# import heroes
import time

skip_shape = True
skip_dash = True
skip_sides = True
skip_random_walk = False
reset_screen = False

timy = Turtle()
# timy.name = heroes.gen()
# print(timy.name)
screen = Screen()

if not skip_shape:
    draw_square(timy,100)

if not skip_dash:
    draw_dash_line(timy, 100, 10)
    time.sleep(2)
    timy.reset()
    pos = random_position_nearby(timy)

    timy.goto(pos.x, pos.y)


if not skip_sides:
    for i in range(3, 9):
        draw_n_side_shape(timy, i, 100)
    time.sleep(2)
    timy.reset()

if not skip_random_walk:
    timy.speed(8)
    turtle.colormode(255)
    random_walk(timy, 200, has_random_color= True, walk=30)
    time.sleep(2)
    if reset_screen:
        timy.reset()


screen.exitonclick()

