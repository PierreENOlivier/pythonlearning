

in_combat = True
while in_combat:
		hero.attack(enemy)
		enemy.attack(hero)
		
		print(f"{hero.name} | HP: {hero.health}")
		print(f"{enemy.name} | HP: {enemy.health}")
		
		print()
		
		action = input("(a)ttack | (s)hield | (r)un away\n")
		if action == "r":
			in_combat = False
			
		print()
		
		