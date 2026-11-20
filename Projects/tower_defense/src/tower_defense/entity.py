from turtle import Turtle
from time import monotonic
from random import uniform

class ConfigEntity:
	ENEMY_SPEED_MULTIPLIER = 1
	PROJECTILE_SPEED_MULTIPLIER = 1.2
	RELOAD_SPEED_MULTIPLIER = 20
	RANGE_TOWER_MULTIPLIER = 1
	GOD_MODE=True
	if GOD_MODE:
		TOWER_HP_MULTIPLIER=10000
	else:
		TOWER_HP_MULTIPLIER=1

class Entity(Turtle):
	def __init__(self, health, position, damage, shape=None):
		if shape is None:
			super().__init__()
		else:
			super().__init__(shape)

		self.health = health
		self.position = position
		self.damage = damage
		
	def take_damage(self, damage):
		self.health -= damage
		
	def is_destroyed(self):
		if self.health <= 0:
			return True
		else:
			return False

	def create_invisible_trace_pen(self):
		self.penup()

		return self
			
class Tower(Entity):
	def __init__(self, health, position, damage, burst, range=100):
		health = health * ConfigEntity.TOWER_HP_MULTIPLIER

		super().__init__(health, position, damage)
		self.create_invisible_trace_pen()
		#### Weapon Stats
		self.burst = burst
		self.range = range * ConfigEntity.RANGE_TOWER_MULTIPLIER
		self.main_weapon = None
		self.secondary_weapon = None
		#### Target
		self.target = None
		self.direction_target = None
		#### Projectiles
		self.last_shot_time = None
		self.reload_time=2 * ConfigEntity.RELOAD_SPEED_MULTIPLIER / 100
		self.reload_timer=0
		self.projectiles=[]

	def aim(self, enemies):
		if self.target and self.target.alive:
			return

		# Acquires target
		self.target = self.find_nearest_target(enemies)

		if self.target:
			self.setheading(self.towards(self.target))
			self.direction_target = self.heading()

	def find_nearest_target(self, enemies):
		nearest = None
		for en in enemies:
			distance = self.distance(en.xcor(), en.ycor())
			if distance < self.range:
				nearest = en
				return nearest
				break

	def load(self, weapon, slot="main"):
		if slot == "main":
			self.main_weapon = weapon
		else:
			self.secondary_weapon = weapon
	
	def shoot(self):
		self.projectiles.append(
			Projectile(
				damage=self.damage * 1.1,
				position=self.position,
				direction=self.direction_target,
				speed=20 * ConfigEntity.PROJECTILE_SPEED_MULTIPLIER
			)
		)

		self.last_shot_time = monotonic()

	def has_reloaded(self):
		if self.last_shot_time is None:
			return True

		elapsed = monotonic() - self.last_shot_time

		return elapsed >= self.reload_time

			
class Enemy(Entity):
	def __init__(self, shape, health, position, damage, speed):
		super().__init__(health, position, damage, shape="triangle")
		self.alive=True
		self.original_shape=shape

		speed_randomizer = uniform(0.5, 1.5)

		self.speed=speed * speed_randomizer * ConfigEntity.ENEMY_SPEED_MULTIPLIER
		self.create_invisible_trace_pen()
		self.goto(position)
		
	def move_towards(self, tower):
		self.setheading(self.towards(tower))
		self.forward(self.speed)
		
class Projectile(Turtle):
	def __init__(self, damage, position, direction, speed):
		super().__init__(shape="circle")

		print("Projectile is crashing")
		self.shapesize(0.5)
		self.penup()

		self.damage = damage
		self.position=position
		self.direction=direction

		self.speed=speed * ConfigEntity.PROJECTILE_SPEED_MULTIPLIER

	def move(self):
		self.setheading(self.direction)
		self.forward(self.speed)

		

			
			
			
			
		