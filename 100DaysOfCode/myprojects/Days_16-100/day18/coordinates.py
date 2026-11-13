def get_upper_corner_position(brush, screen):
    brush.setpos((0, 0))
    xi, yi = brush.pos()
    x_length, y_length = get_dimensions_screen(screen)

    return (xi - x_length / 2), (yi + y_length / 2)

def get_dimensions_screen(screen):
    return screen.screensize()


def calculate_xy_coordinates(
        x_y_start: Tuple[float, float],
        screen_dimension: Tuple[float, float],
        size,
        gap
):
    x, y = x_y_start
    x_length, y_length = screen_dimension
    x_ticks = calculate_ticks_coordinates(
        start_pos_on_axis=x,
        length_axis=x_length,
        size=size,
        gap=gap
    )

    y_ticks_from_bottom = calculate_ticks_coordinates(
            start_pos_on_axis=-y,
            length_axis=y_length,
            size=size,
            gap=gap
        )

    y_ticks = [-ypos
        for ypos in y_ticks_from_bottom
    ]

    print(y)

    return x_ticks, y_ticks

def calculate_ticks_coordinates(
        start_pos_on_axis: float,
        length_axis: float,
        size: int,
        gap: int
):
    min = int(start_pos_on_axis + gap)
    max = int(start_pos_on_axis + length_axis - gap)

    gap_tick = int(size + gap)
    ticks = [pos for pos in range(min, max, gap_tick)]

    gap_left = int(abs(start_pos_on_axis - min))
    gap_right = int(abs(length_axis // 2 - ticks[len(ticks) - 1] - size))

    if gap_left != gap_right:
        new_gap = (gap_left + gap_right) // 2
        offset = new_gap - gap_left
        ticks = [pos + offset for pos in ticks]

    return ticks
