from turtle import Turtle
from random import choice

def clear_brush(brush):
    brush.clear()
    brush.penup()
    brush.home() # reset position, needs to have pen up otherwise draws
    brush.pendown()

def show_key(event):
    print(event.keysym)

class RaceTrack:
    def __init__(self, screen):

        self.screen = screen

        self.height = self.screen.window_height()
        self.width = self.screen.window_width()

        self.half_height = self.height // 2

        self.half_width = self.width // 2

        print(f"Width: {self.width} | Height: {self.height}")

        self.x_finish = int(self.half_width - (self.width * 15 / 100))
        self.x_start = int(-self.half_width + (self.width * 15 / 100))

    def place_on_starting_line(self, racers, gap=None):
        n_racers = len(racers)
        limits = 40
        width_track = (self.height - limits * 2) # height, because horizontal
        if gap:
            gap = int(width_track // (n_racers - 1))
            gap_was_set = True
        else:
            gap = 20
            gap_was_set = False

        edge_left = int(self.half_height - limits)
        edge_right = -edge_left

        print(f"edge_left: {edge_left} | edge_right: {edge_right} | gap: {gap}")
        if gap_was_set:
            if edge_right < 0:
                gap = -gap

            start_position = [y_pos for y_pos in range(edge_left, edge_right, gap)]
            start_position.append(edge_right)
        else:
            # if n_racers % 2 == 0:
            left_starts = [0 + gap * i for i in range(n_racers//2, 0, -1)]
            right_starts = [0 - gap * i for i in range(0, n_racers - n_racers//2)]
            start_position = []
            start_position.extend(left_starts)
            start_position.extend(right_starts)
            print(start_position)

            # if  n_racers % 2 != 0:
                # n_position_on_side =

            # TODO: adjust the gaps to center around 0


        if len(start_position) != n_racers:
            raise IndexError

        for index, racer in enumerate(racers):
            racer.penup()
            racer.setpos(self.x_start, start_position[index])
            positions = racer.pos()
            position_x_y = (positions[0] - 30, positions[1] + 10)

            racer.pendown()
            print(f"Racer: {racer.color}"
                  f"Position: {racer.pos()}"
                  )

            write_text(position_x_y, racer.name)

        self.draw_finish_line()


    def draw_finish_line(self):
        line = Turtle()
        line.hideturtle()
        line.speed(8)
        line.pensize(5)
        line.color("black")
        line.penup()
        line.goto(self.x_finish, self.half_height)
        line.pendown()
        line.goto(self.x_finish, -self.half_height)



    def has_reach_finish(self, racer):
        if racer.pos()[0] > self.x_finish:
            return True
        else:
            return False

    def check_bet(self, user_bet, winner):
        print("Check bet: ", user_bet)

        if user_bet == winner.name:
            msg="Congrats!"
        else:
            msg="You lost..."

        announcer = Turtle()
        announcer.hideturtle()
        announcer.penup()
        announcer.goto(0, 0)
        announcer.write(
            msg,
            align="center",
            font=("Arial", 20, "bold")
        )

    def start_race(self, racers):
        name_racers = [racer.name for racer in racers]
        name_mapping = {
            number: name
            for number, name in enumerate(name_racers, start=1)
        }

        options = [f"{num}: {name}" for num, name in name_mapping.items()]
        options_str = " | ".join(options)

        bet_num = self.screen.numinput(
            prompt=(
                "Choose a racer." +
                f"Options: {options_str}:"
            ),
            title="RaceTrack"
        )

        bet = name_mapping[bet_num]
        print(f"{bet_num} | {bet}")


        race_over = False

        while not race_over:
            for racer in racers:
                step = choice([20, 30, 40, 50, 60])
                racer.forward(step)

                if self.has_reach_finish(racer):
                    race_over = True
                    winner = racer

        self.check_bet(user_bet=bet, winner=winner)

@staticmethod
def write_text(pos, text):
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(pos)
    pen.write(text, align="center", font=("Arial", 20, "bold"))



def generate_racers(team):
    racers = []
    for k, colour in team.items():
        racer = Turtle()
        racer.name = k
        racer.color(colour)
        racer.pencolor(colour)
        racer.shape("turtle")
        racers.append(racer)

    return racers


