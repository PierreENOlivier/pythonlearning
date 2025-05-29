from characters import Hero, Enemy
from weapons import bow
from time import sleep

hero = Hero(name="Pierre", health=120)

enemy = Enemy(name="Borg", health=100, weapon=bow)

for i in range(3):
	print(f"{i+1}...")
	sleep(1)

print("FIGHT!!!\n")
sleep(1)

in_combat = True
while in_combat:
		print(f"{hero.name} | HP: {hero.health} | KI: {hero.ki}")
		hero.health_bar.draw()
		print(f"{'_' * 20}")
		print(f"{enemy.name} | HP: {enemy.health}")
		enemy.health_bar.draw()
		
		print()
		
		
		
		action = input("(a)ttack | (c)harge Ki | (k)i attack | (s)hield | (r)un away\n")
		if action == "r":
			print("You ran away!")
			break
		elif action == "c":
			hero.charge_ki()
		elif action == "k":
			hero.attack_ki(enemy)
		elif action == "a":
			hero.attack(enemy)
		print()
		
		enemy.attack(hero)
		
		
		print()
		
		if hero.health <= 0:
			print(f"You died!!")
			in_combat = False
		elif enemy.health <= 0:
			print(f"You survived this fight! {enemy.name} is dead!")
			in_combat = False
		
		