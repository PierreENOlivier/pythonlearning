import pygame as pg
import sys

class Grid:
	def __init__(self, screen):
		width,height = screen.get_size()
		
		self.block = pg.Surface([20, 20])
		self.block.fill((0,0,0))

class Game:
	pg.init()
	WIDTH = 1080 # 1080px
	HEIGHT = 1080 # 2400px
	
	def __init__(self):
		self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		
		self.clock = pg.time.Clock()
		
		self.gg = Grid(self.screen)
		
		
	def run(self):
		while True:
			
			self.screen.fill((255, 255, 255))
			
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
					
			pg.display.update()
			
			self.clock.tick(60)
			
def main():
		game = Game()			
		game.run()
		
if __name__ == '__main__':
	main()