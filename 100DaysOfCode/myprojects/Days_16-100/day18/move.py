import time
from turtle import Turtle
from random import randint, choice
from dataclasses import dataclass

from colors import COLORS, random_color
from coordinates import (
    get_upper_corner_position,
    calculate_xy_coordinates,
    get_dimensions_screen
)

def paint_every_n(brush, n_times, by):
    """

    :param brush: An instance of the Turtle class with color, shapes and other attributes
    :param n_times: Number of times to paint each brush
    :param by: An integer representing gap between two paint
    :return: None
    """

    for i in range(n_times):
        time.sleep(1)
        brush.pendown()
        brush.circle(5)

        brush.penup()

        brush.forward(by)

def draw_square(brush: Turtle, length: int):
    """

    :param brush: A Turtle instance
    :param length: An integer representing the size of the sides of the square
    :return:
    """
    brush.pendown()
    for _ in range(4):
        brush.forward(length)
        brush.left(90)

    brush.penup()

def draw_n_side_shape(brush: Turtle, n_side, length  = 10):
    brush.pendown()
    angle = 360 / n_side

    brush.color(choice(COLORS))

    for i in range(n_side):
        brush.left(angle)
        brush.forward(length)

    brush.penup()
    brush.color("gray0")

def draw_dash_line(brush, length, gap):
    n_times = length // gap

    for i in range(n_times):
        brush.pendown()
        brush.forward(gap)
        brush.penup()
        brush.forward(gap)

    brush.penup()

@dataclass
class Position:
    x: int
    y: int

def random_position_nearby(brush):

    x_shift_range = range(10, 101, 10)
    y_shift_range = range(10, 101, 10)

    x = choice(x_shift_range) + brush.pos()[0]
    y = choice(y_shift_range) + brush.pos()[1]


    return Position(x, y)

SHARP_ANGLE_AVAILABLE = [angle for angle in range(-90, 91, 30)]
ANGLE_AVAILABLE_TURNBACK = [angle for angle in range(-180, 181, 90)]
ANGLE_AVAILABLE = [angle for angle in range(0, 360, 90)]
LENGTH_AVAILABLE = [length for length in range(15, 60, 15)]

def random_walk(brush, steps = 20, has_random_color: bool = True, walk: int = None):
    old_settings = brush.pen()
    brush.pensize(10)

    for _ in range(steps):
        if has_random_color:
            brush.color(random_color())
        else:
            brush.color(choice(COLORS))
        brush.setheading(ang := choice(ANGLE_AVAILABLE))
        if walk is None:
            walk = choice(LENGTH_AVAILABLE)
        brush.forward(walk)

        print(f"Step: {_} | Angle: {ang} | Walk: {walk}")


    brush.pen(old_settings)


def draw_spirograph(angle_shift):
	
	tim = Turtle()
	print("test")
	tim.speed(0)
	
	n = int(360 // angle_shift)
	
	for _ in range(n):
		
		tim.pencolor(random_color())
		tim.circle(100)
		pos = tim.heading()
		print(pos)
		tim.setheading(pos - angle_shift)


def draw_damien_hirst(
        colors,
        screen,
        size,
        gap,
        strict_gap
):
    """

    :param colors: A list of colors to use for the drawing
    :param screen: A screen object for coordinate calculations
    :param size: Size of the circle
    :param gap: Spacing between the circle
    :param strict_gap: if True, the gap is added from the edge of the circle.
        If False, the gap is added from the center of the circle to allow overlaps.
    :return: None
    """
    brush = Turtle()
    brush.speed(0)
    bg = (255, 253, 237)
    screen.bgcolor(bg)

    # Circles are drawn from header at center position
    # Consider the right and left radius of left and right circles
    if strict_gap:
        size_object = size * 2
    else:
        size_object = size

    x, y = calculate_xy_coordinates(
        x_y_start=get_upper_corner_position(brush, screen),
        screen_dimension=get_dimensions_screen(screen),
        size=size_object,
        gap=gap
    )

    for xpos in x:
        for ypos in y:
            i_color = choice(colors)
            if brush.pen()['pendown'] == True:
                brush.penup()

            # Circles are drawn from header
            # To get the center, move y by the radius
            brush.goto((xpos, ypos))

            brush.color(i_color)
            brush.fillcolor(i_color)

            brush.pendown()
            brush.begin_fill()

            brush.circle(size)

            brush.end_fill()


    print("done")