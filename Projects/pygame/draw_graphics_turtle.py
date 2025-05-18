# Drawing with Turtle program
import turtle
import time
fred = turtle.Pen()
fred.shape("turtle")

fred.speed(8)
line = 100
run = True
while run:
	for i in range(4):
		fred.forward(line) # draw for 100 px
		fred.left(90) # give angle
		
		

	#ans = input("Stop program? y/n")
#	if ans == "y":
#		run = False
	line -= 20
	time.sleep(0.5)
	
	if line < 10:
		run = False

fred.reset()


hex = "#34c0eb"
fred.color(hex)

run = True
line = 100
turns = 0

fred.speed(0)
while turns < 4:
	fred.fillcolor(hex)
	fred.begin_fill()
	
	for i in range(2):
		fred.circle(100) # radius
		fred.circle(-50)
		fred.up() # lift the pen
		fred.forward(line)
		fred.down() # bring tip to paper
	
		time.sleep(1)
	
	turns += 1
	
	fred.left(90)
	
	fred.end_fill()
	
# fred.speed(1) # 0-10 controls how farthe drawing takes, 0 just draws without animation

fred.reset()
fred = turtle.Pen()
fred.shape("turtle")

fred.speed(0)

for i in range(50):
	fred.circle(i * 10)
	fred.left(10)
	
# Control width and length circles
fred.reset()
fred.width(3)
fred.color("red")

for i in range(20):
	fred.circle(i * 3, 180) # 180° half circles
	fred.right(45) # 45°
	
time.sleep(10)
