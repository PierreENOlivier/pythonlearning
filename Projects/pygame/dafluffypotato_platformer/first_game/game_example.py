import pygame
import sys

from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        # Initialize the engine
        pygame.init()

        WINDOW_WIDTH = 640
        WINDOW_HEIGHT = 480

        # Create a window
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Control the frame rate
        self.clock = pygame.time.Clock()

        # Load assets
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))  # if the background is black
        self.img_pos = [160, 260]
        self.movement = [False, False]


        # Set the physics
        self.collision_area = pygame.Rect(50, 50, 300, 50)

        self.player = PhysicsEntity(
            self,
            'player',
            (50, 50),
            (8, 15)
        )

    def run(self):
        while True:

            # Setup the scene
            self.screen.fill((14, 219, 248)) # RGB

            # Place on surface
            img_r = pygame.Rect(
                *self.img_pos,
                *self.img.get_size()
            )

            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (88, 88, 88), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_w]:
                    # if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                    # if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_UP, pygame.K_w]:
                    # if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                    # if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            # Print on screen
            pygame.display.update()
            self.clock.tick(60)

Game().run()


