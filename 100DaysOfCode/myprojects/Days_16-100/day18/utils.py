import math
import tkinter.font

from turtle import Turtle
from move import draw_square

def visualize_palette(palette: list[str], size: int = 10):
    """
    :param palette: A list of colors saved as an RGB string
    :param size: Size of the square visualizing the color
    :return: None
    """
    brush = Turtle()
    brush.speed(0)
    brush.hideturtle()

    gap = 15
    n_color = len(palette)
    n_row = math.ceil(n_color / 5)


    font = tkinter.font.Font(
        family="Arial",
        size=8,
        weight="normal"
    )
    width_text = font.measure(palette[0])
    height_text = font.metrics("linespace")
    margin_pos_x = max(size + gap, width_text + gap)
    height_position = height_text + size + gap


    x_pos = [x for x in range((-margin_pos_x * 2 ), (margin_pos_x * 2 + 1), margin_pos_x)]
    y_pos = [-1 * val
             for val in
             [y for y in range(0, (height_position * n_row + 1), height_position)]
             ]
    print(x_pos)
    print(y_pos)

    index = 0
    for x in x_pos:
        for y in y_pos:
            if index > len(palette) - 1:
                break
            brush.penup()

            brush.goto(x, y - (height_text + 5))
            color = palette[index]
            brush.write(
                color,
                align="left",
                font=(
                    font.actual("family"),
                    font.actual("size"),
                    font.actual("weight")
                )
            )

            brush.goto(x, y)

            brush.fillcolor(color)
            brush.pendown()

            brush.begin_fill()
            draw_square(brush, size)

            brush.end_fill()

            index += 1


