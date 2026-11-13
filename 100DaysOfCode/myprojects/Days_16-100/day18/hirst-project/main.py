###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from pathlib import Path
import sys
path_parent = str(Path(__file__).resolve().parent.parent)
print(path_parent)
sys.path.append(path_parent)

import turtle
from turtle import Turtle, Screen, onclick

from utils import visualize_palette, reset_screen_click_on_turtle
from coordinates import get_upper_corner_position
from move import draw_damien_hirst

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


print(rgb_colors)

turtle.colormode(255)
screen = Screen()

# visualize_palette(rgb_colors[:10])

draw_damien_hirst(
    colors=rgb_colors,
    screen=screen,
    size=30,
    gap=0,
    strict_gap=False

)

onclick(fun=reset_screen_click_on_turtle(screen))




screen.mainloop()
