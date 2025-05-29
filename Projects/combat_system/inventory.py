import math

class Inventory:
	def __init__(
		self,
		size: int = 20,
		width: int = 5
		
	) -> None:
		self.size = size
		self.width = width
		
		self.space = [
		[slots for slots in range(self.size)],
		[None for x in range(self.size)]
		]
		
		first_empty_slot = 0
		
	def update(self):
		pass
		#empty_slots = [i for i, v in enumerate(space[1][]) if v == None]
		
#		self.first_empty_slot = min(empty_slots)
	
	def add(self, object):
		pass
		
	def print(self):
		print(self.space)
