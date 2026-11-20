from entity import *
from turtle import Screen

class Game:
	def __init__(self):
		self.screen = Screen()
		
		self.tower = Tower(
			health=100, 
			position=(0,0),
			damage=10,
			burst=2
		)
		
		self.enenmy_on_map=[]
		
	def run(self):
		self.add_enemies(5)
		
		self.screen.exitonclick()
		
	def add_enemies(self, n):
		enemy=Enemy(
			shape="circle",
			health=20,
			damage=10,
			position=(300,300),
			speed=2
		)