from .entity import *
from turtle import Screen
from random import randint
from math import hypot

class Game:
	def __init__(self):
		self.screen = Screen()
		self.screen.setup(width=1000, height=800)
		self.screen.tracer(0)
		
		self.tower = Tower(
			health=100, 
			position=(0,0),
			damage=10,
			burst=2,
			range=200
		)

		self.tower.shapesize(4)
		
		self.enemy_on_map=[]
		
	def run(self):
		self.enemy_on_map.extend(self.add_enemies(10))

		self.update()

		print(self.enemy_on_map)

		self.game_loop()
		
		self.screen.exitonclick()

	def game_loop(self):
		self.update()
		self.screen.update()


		self.screen.ontimer(self.game_loop, 100)
		
	def add_enemies(self, n):
		enemies = []
		for i in range(n):
			x_post, y_post = self.get_outside_radius_coordinates(
				inner_radius=250,
				outer_radius=400
			)

			enemy=Enemy(
				shape="circle",
				health=20,
				damage=10,
				position=(x_post,y_post),
				speed=2
			)

			enemy.color("red")
			enemies.append(enemy)
		return enemies
	def update(self):
		self.update_enemies()
		self.update_tower()
		self.update_projectiles()

	def update_enemies(self):
		for en in self.enemy_on_map:
			en.move_towards(self.tower)

	def update_tower(self):
		self.tower.aim(self.enemy_on_map)
		if self.tower.target and self.tower.target.alive:
			if self.tower.has_reloaded():
				self.tower.shoot()
				print(f"Shoot: {id(self.tower.target)}")

	def update_projectiles(self):
		for missile in self.tower.projectiles:
			missile.move()

	def get_outside_radius_coordinates(self, inner_radius, outer_radius):
		while True:
			x = randint(-outer_radius, outer_radius)
			y = randint(-outer_radius, outer_radius)

			if hypot(
					x - self.tower.xcor(),
					y - self.tower.ycor()
			) > inner_radius:
				break


		return (x, y)


