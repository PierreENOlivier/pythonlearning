from turtle import Screen, Turtle
from random import choice, randint
import time

from .tamago import Tamago, Display

FOOD = {
    "strawberry": {
        "hunger":20,
        "taste": 5,
        "size":1,
        "shape": "triangle",
        "color": "red"
    },
    "salad":{
        "hunger":50,
        "taste": 2,
        "size":0.5,
        "shape": "circle",
        "color": "green"
    }
}

class Game:
    def __init__(self, name):
        self.screen = self.set_game_screen()
        self.tamago = Tamago(name)
        self.food_prob = self.generate_food_prob(FOOD)
        self.food_on_screen = []
        self.interval = 1

        # Update the timer
        self.last_update = time.monotonic()
        self.hunger_timer = 0
        self.growth_timer = 0

    def set_game_screen(self):
        screen = Screen()

        screen.setup(width=800, height=800)
        screen.title("Tamagoturtle")

        self.screen_height = screen.window_height()
        self.screen_width = screen.window_width()

        self.xmin = -int(self.screen_width // 2)
        self.xmax = int(self.screen_width // 2)
        self.ymin = -int(self.screen_height // 2)
        self.ymax = int(self.screen_width // 2)

        return screen


    def generate_food_prob(self, food_sources):
        food_prob = []
        for k,v in food_sources.items():
            if v["taste"] >= 5:
                food_prob.extend([k] * 2)
            elif v["taste"] >= 3:
                food_prob.extend([k] * 5)
            else:
                food_prob.extend([k] * 8)
        print(f"Food proba: {food_prob}")

        return food_prob

    def add_food(self, food, food_prob, n):
        while len(self.food_on_screen) < n:
            food_item = choice(food_prob)

            x_food = randint(self.xmin, self.xmax)
            y_food = randint(self.ymin, self.ymax)

            if self.tamago.distance(x_food, y_food) > 100:
                # Set the pen

                food = Turtle(shape=FOOD[food_item]["shape"])
                food.foodtype = food_item
                food.hunger = FOOD[food_item]["hunger"]
                food.foodsize = FOOD[food_item]["size"]
                food.foodcolor = FOOD[food_item]["color"]
                food.taste = FOOD[food_item]["taste"]
                print("Created:", id(food), food.foodtype)
                food.hideturtle()
                food.penup()

                food.goto(x_food, y_food)
                food.shapesize(food.foodsize)
                food.color(food.foodcolor)
                food.showturtle()
                self.food_on_screen.append(food)

    def find_closest_food(self):
        distances = [
            self.tamago.distance(food.xcor(), food.ycor())
            for food in self.food_on_screen
        ]

        print(f"Distances: {distances}")

        idx_closest = distances.index(min(distances))
        print(f"Closest food: IDX={idx_closest}, distance={distances[idx_closest]}"
              f"\n"
              f"Food: {self.food_on_screen[idx_closest].foodtype}")

        return self.food_on_screen[idx_closest]

    def search_food(self):
        print(f"Has target: {self.tamago.food_target}")
        if not self.tamago.food_target:
            self.tamago.food_target = self.find_closest_food()

            # TODO: What to do when food runs out
        else:
            closest_food = self.tamago.food_target
            self.tamago.go_to_food(closest_food)
            print(f"Is distance close: {self.tamago.distance(closest_food.xcor(), closest_food.xcor()) < 10}"
                  f"\n"
                  f"Distance: {self.tamago.distance(closest_food.xcor(), closest_food.xcor())}")

            if self.tamago.distance(closest_food.xcor(), closest_food.ycor()) < 10:
                print("Reached food")
                self.eat_food(closest_food)



    def eat_food(self, food):
        food.hideturtle()
        self.tamago.eat_food(food)
        print("Removed:", id(food), food.foodtype)
        self.tamago.food_target = None
        self.food_on_screen.remove(food)



    def update_displays(self):
        self.tamago.display_hunger.update_text(
            value=self.tamago.hunger
        )

    def game_loop(self):
        now = time.monotonic()
        delta_time = now - self.last_update
        self.last_update = now

        # Check hunger
        self.hunger_timer += delta_time
        self.growth_timer += delta_time
        while self.hunger_timer >= 1:
            # Makes sure that if the game freezes, we account for every full
            # seconds that elapsed
            self.tamago.hunger += 5
            self.hunger_timer -= 1

        while self.growth_timer >= 5:
            self.add_food(food=FOOD, food_prob=self.food_prob, n=2)
            self.growth_timer -= 5

        self.update_displays()

        if self.tamago.hunger > 50:
            self.search_food()
            self.update_displays()


        self.screen.ontimer(fun=self.game_loop, t=100)


    def run(self):
        print(f"Height: {self.screen_height} | Width: {self.screen_width}")
        self.add_food(food=FOOD, food_prob=self.food_prob, n=5)

        # Tamago
        self.tamago.display_hunger = Display(x=-200, y=200, text="Hunger: ")
        self.tamago.display_hunger.add_text(
            value=self.tamago.hunger
        )

        self.game_loop()

        self.screen.mainloop()
