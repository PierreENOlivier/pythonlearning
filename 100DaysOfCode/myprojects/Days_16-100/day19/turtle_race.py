from move import move_forwards
from utils import RaceTrack, generate_racers
from turtle import Turtle, Screen
from pprint import pprint

team = {
    "Floyd": "red",
    "Carlito": "DarkGoldenrod1",
    "Rex": "chartreuse1",
    "Plume": "blue4",
    "Rosa": "DeepPink4"
}

screen = Screen()
screen.setup(width=800, height=500)



race_track = RaceTrack(screen)

racers = generate_racers(team)

pprint(racers)

race_track.place_on_starting_line(racers, gap = 40)

race_track.start_race(racers)

screen.exitonclick()





