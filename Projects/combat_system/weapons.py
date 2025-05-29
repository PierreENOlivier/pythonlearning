class Weapon:
	def __init__(
		self,
		name: str,
		weapon_type: str,
		damage: int,
		value: int
	) -> None:
		self.name = name
		self.weapon_type = weapon_type
		self.damage = damage
		self.value = value
		
axe = Weapon(
	name="Valorian axe",
	weapon_type="axe",
	damage=10,
	value=5
)

bow = Weapon(
	name="Short bow",
	weapon_type="bow",
	damage=7,
	value=3
)

wand = Weapon(
	name="Magic wand",
	weapon_type="wand",
	damage=20,
	value=10
)

fists = Weapon(
	name="Fists",
	weapon_type="blunt",
	damage=5,
	value=0
)