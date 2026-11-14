from turtle import Turtle, Screen
from move import *
from utils import *

tim = Turtle()
screen = Screen()

keys = KeyRecording(tim)

screen.getcanvas().bind("<KeyPress>", show_key)

# screen.onkeypress(key="Up", fun=lambda: move_forwards(tim, 20))
# screen.onkeypress(key="Down", fun=lambda: move_backwards(tim, 20))
# screen.onkeypress(key="Left", fun=lambda: rotate_left(tim))
# screen.onkeypress(key="Right", fun=lambda: rotate_right(tim))
# screen.onkeypress(key="x", fun=lambda: clear_brush(tim))

screen.onkeypress(key="Up", fun=lambda: keys.press("Up"))
screen.onkeyrelease(key="Up", fun=lambda: keys.release("Up"))
screen.onkeypress(key="Down", fun=lambda: keys.press("Down"))
screen.onkeyrelease(key="Down", fun=lambda: keys.release("Down"))

screen.onkeypress(key="Right", fun=lambda: keys.press("Right"))
screen.onkeyrelease(key="Right", fun=lambda: keys.release("Right"))
screen.onkeypress(key="Left", fun=lambda: keys.press("Left"))
screen.onkeyrelease(key="Left", fun=lambda: keys.release("Left"))

screen.onkey(key="x", fun=lambda: clear_brush(tim))
screen.onkey(key="-", fun=lambda: keys.decrease_step())
screen.onkey(key="+", fun=lambda: keys.increase_step())
screen.onkey(key="/", fun=lambda: keys.decrease_angle())
screen.onkey(key="*", fun=lambda: keys.increase_angle())
screen.onkey(key="r", fun=lambda: keys.reset())


screen.listen()
keys.print_attributes()

keys.update(ascreen=screen)

screen.exitonclick()
