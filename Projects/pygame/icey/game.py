import pygame as pg
import sys
from scripts.tilemap import Grid

class Game:
	pg.init()
	WIDTH = 640 # 1080 # 1080px
	HEIGHT = 480 # 1080 # 2400px
	
	def __init__(self):
		pg.display.set_caption("Ninja Game")
		self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		
		self.clock = pg.time.Clock()
		
		self.gg = Grid(
			self,
			size_grid = (10, 10),
			tile_size = 16)

		self.assets = {
			'water': pg.image.load('data/images/water/waters.png').convert()
		}



		
	def run(self):
		while True:
			
			self.screen.fill((255, 100, 255))
			self.screen.blit(self.assets['water'])
			
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
					
			pg.display.update()
			
			self.clock.tick(60)
			
game = Game()
game.run()
		
