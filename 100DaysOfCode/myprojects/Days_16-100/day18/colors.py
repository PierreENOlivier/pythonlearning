from random import randint, choice

COLORS = [
    "#502419",
    "#7ea172",
    "#c7cb85",
    "#e7a977",
    "#ebbe9b",
    "#9b5de5",
    "#f15bb5",
    "#fee440",
    "#00bbf9",
    "#827191",
    "#84dcc6",
    "#C2E812",
    "#ffa69e",
    "#ff686b",
    "#813405",
    "#d45113",
    "#f9a03f",
    "#f8dda4",
    "#ddf9c1"

]

def random_color():

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    print(f"R: {r}, G: {g}, B: {b}")

    return (r, g, b)
