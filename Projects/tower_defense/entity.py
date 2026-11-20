from turtle import Turtle

class Entity:
	def __init__(self, health, position, damage):
		self.health = health
		self.position = position
		self.damage = damage
		
	def take_dame(self, damage):
		self.health -= damage
		
	def is_destroyed(self):
		if self.health <= 0:
			return True
		else:
			return False
			
class Tower(Entity):
	def __init__(self, health, position, damage, burst):
		super().__init__(health, position, damage)
		self.burst = burst
		self.main_weapon = None
		self.secondary_weapon = None
		
		self.tower=Turtle()
	
	def load(self, weapon, slot="main"):
		if slot == "main":
			self.main_weapon = weapon
		else:
			self.secondary_weapon = weapon
	
	def shoot(self):
			pass
			
class Enemy(Entity):
	def __init__(self, shape, health, position, damage, speed):
		super().__init__(health, position, damage)
		self.original_shape=shape
		self.speed=speed
		self.enemy=Turtle(shape)
		self.enemy.goto(position)
		
	def move_towards(self, tower):
		pass
		
class Projectile:
	def __init__(self, damage, position, direction):
		self.damage = damage
		self.position=position
		self.direction=direction
		
	def travel(self):
		pass
		

			
			
			
			
		