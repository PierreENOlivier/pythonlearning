# My first pygame game

import pygame
import random

WIDTH = 320
HEIGHT = 480
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (120, 0, 0)
BLUE = (3, 4, 94)
GREEN = (38, 70, 83)

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tuto Game")
clock = pygame.time.Clock()

# Prepare sprites

all_sprites = pygame.sprite.Group()
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