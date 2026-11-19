from turtle import Turtle
from time import sleep

class Tamago(Turtle):
    def __init__(self, name):
        super().__init__(shape="turtle")
        self.name = name
        self.hunger = 0
        self.age = 0
        self.resizemode("user")
        self.shapesize(3, 3, 2)
        self.penup()
        self.food_target = None
        self.step_counter = 0

    def go_to_food(self, food):
        self.setheading(
            self.towards(
                food.xcor(),
                food.ycor()
        ))
        print(f"Heading: {self.heading()}")

        if food.taste > 4:
            speed = 50
        else:
            speed = 25

        distance_to_food = self.distance(food.xcor(), food.ycor())
        if  distance_to_food < speed:
            speed = distance_to_food

        self.forward(speed)
        self.step_counter += 1
        print(f"Steps: {self.step_counter}")


    def eat_food(self,food):
        replenish = food.hunger
        self.hunger -= replenish


    # Identify what is the closest
    # Identify what is the biggest or tastiest = set priorities

class Display(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.text = text
        self.hideturtle()
        self.penup()
        self.x_coord = x
        self.y_coord = y
        self.goto(self.x_coord, self.y_coord)
        self.last_value = None


    def add_text(self, value):
        self.clear()
        self.last_value = value
        textconcat = f"{self.text}: {value}"
        self.write(textconcat, align="center", font=("AMAZON", 24, "normal"))


    def update_text(self, value):
        if value == self.last_value:
            return

        self.add_text(value)
