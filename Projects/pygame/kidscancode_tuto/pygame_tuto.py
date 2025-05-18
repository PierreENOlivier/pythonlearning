# My first pygame game

import pygame
import random

WIDTH = 800 # 1080
HEIGHT = 720 # 2400
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (120, 0, 0)
BLUE = (3, 4, 94)
GREEN = (38, 70, 83)

# Prepare sprites
## Player sprite

class Player(pygame.sprite.Sprite):
	cursor = [20, 15]
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		# Image location or what to display
		self.image = pygame.Surface((50, 50)) # size
		self.image.fill(RED)
		
		# Rectangle enclosing the image to keep track of size or position 
		self.rect = self.image.get_rect() # Find current location
		self.rect.center = (WIDTH / 2, HEIGHT/ 2) # Set location to center
		
		# Each method controls a type of update
	def update(self):
		
		self.rect.x += self.cursor[0] # when update, move 5 px on x axis (so right)
		self.rect.y += self.cursor[1]
		
		# Prevent the object from leaving the screen
		if self.rect.left < 0 or self.rect.right > WIDTH:
			
			self.cursor[0] = -1 * self.cursor[0]
			self.cursor[1] = random.randrange(3, 5)
			
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			factor = random.randrange(1, 3)
			self.cursor[1] = -1 * factor * self.cursor[1]
			self.cursor[0] = -1 * self.cursor[0]
		 
		
# Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.list_modes()

pygame.display.set_caption("Tuto Game")
clock = pygame.time.Clock()

# Prepare sprites groups
all_sprites = pygame.sprite.Group()

# Initiate player
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
	# Maintain speed loop (wait if too quick)
	clock.tick(FPS)
	
	# Process input
	## Process all latest recorded events
	for event in pygame.event.get():
		### Check Event Close Game
		if event.type == pygame.QUIT:
			running = False
	
	
	# Update
	all_sprites.update()
	
	
	# Draw (layers on top of each other)
	screen.fill(BLUE)
	all_sprites.draw(screen)
	
	# After drawing everything: display the result
	pygame.display.flip() # Double Buffering 

# Close the game
pygame.quit()