import turtle
import time
import random
import math

fred = turtle.Pen()

fred.speed(1)
fred.color("#264653")
fred.shape("turtle")

colors = ["red", "blue", "green",
 "#42f5e0", "#4245f5", "#cb42f5"]
 

time.sleep(1)

def square(size):
	for i in range(4):
		fred.forward(size)
		fred.left(90)

def equitriangle(size):
	for i in range(3):
		fred.forward(100)
		fred.left(90 + 90 - 60)
		
equitriangle(100)
		
def angletriangle(angle):
	angleB = 90 + 90 - angle
	return angleB

def righttriangle(base, angle):
	# SOH CAH TOA
	# use TOA
	radians = angle * math.pi / 180
	tanA = math.tan(radians)
	
	opposite = tanA * base
	
	angleB = 180 - 90 - angle
	
	hypothenus = math.sqrt( opposite ** 2 + base ** 2 )
	
	fred.forward(base)
	fred.left(angletriangle(angle))
	fred.forward(hypothenus)
	fred.left(angletriangle(angleB))
	fred.forward(opposite)
	fred.left(90)

righttriangle(100, 30)

time.sleep(2)

fred.forward(100)

square(100)

# Control coordinates
# Default (0,0) (x,y)
fred.speed(0)
for i in range(100):
	x = random.randrange(-200, 200)
	y = random.randrange(-200, 200)
	size = random.randrange(10, 100)
	
	color = random.choice(colors)
	fred.color(color)
	
	fred.up()
	fred.goto(x, y) # Move to coordinates
	fred.down()
	square(size) 

time.sleep(10)

