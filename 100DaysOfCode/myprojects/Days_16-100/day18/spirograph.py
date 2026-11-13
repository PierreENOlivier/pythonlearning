import turtle
from turtle import Turtle, Screen, mainloop

from colors import random_color
from move import draw_spirograph



def main():
	screen = Screen()
	screen.colormode(255)

	draw_spirograph(1)

	screen.exitonclick()
	
main()
	



   