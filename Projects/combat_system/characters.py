from weapons import fists
from health_bar import Healthbar

class Character:
	def __init__(self, name: str, health: int) -> None:
		self.name = name
		self.health = health
		self.health_max = health
		
		self.weapon = fists
	
	
	def attack(self, target):
		target.health -= self.weapon.damage
		print(f"{self.name} uses {self.weapon.name} and deals {self.weapon.damage} damage!")
		target.health = max(target.health, 0)
		target.health_bar.update()

class Hero(Character):
	ki = 0
	ki_damage = 50
	
	def __init__(
	self,
	name,
	health
	) -> None:
		super().__init__(name=name, health=health)
		
		self.default_weapon = self.weapon
		self.health_bar = Healthbar(self, color="green")
		
	def charge_ki(self):
		self.ki += 5
		print("You are charging  your energy...!")
		
	def attack_ki(self, target):
		if self.ki < 10:
			print("Attack failed! Not enough Ki!")
		else:
			print(f"You blast your Ki at your enemy dealing {self.ki_damage} damages!!!")
			target.health -= self.ki_damage
			target.health_bar.update()
			
	
	def equip(self, weapon):
		self.weapon=weapon
		print(f"You equipped {self.weapon.name}.")
	
	def drop(self, weapon):
		self.weapon = self.default_weapon
		print(f"You dropped your current weapon and  equipped {self.weapon.name}.")
		
class Enemy(Character):
	def __init__(
	self,
	name,
	health,
	weapon
	) -> None:
		super().__init__(name=name, health=health)
		self.weapon=weapon
		self.health_bar = Healthbar(self, color="red")
