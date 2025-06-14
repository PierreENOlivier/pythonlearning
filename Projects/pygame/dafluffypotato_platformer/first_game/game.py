import pygame
import sys

from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        # Initialize the engine
        pygame.init()

        WINDOW_WIDTH = 640
        WINDOW_HEIGHT = 480

        # Create a window
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.canvas = pygame.Surface([round(dim / 2) for dim in self.screen.get_size()])


        # Control the frame rate
        self.clock = pygame.time.Clock()

        # Load assets

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        for tile_type in ['decor', 'grass', 'large_decor', 'stone']:
            self.assets[tile_type] = load_images(f'tiles/{tile_type}')

        print(self.assets)

        self.player = PhysicsEntity(
            self,
            'player',
            (50, 50),
            (8, 15)
        )

        self.tilemap = Tilemap(self, tile_size=16)

    def run(self):
        while True:

            # Setup the scene
            self.canvas.fill((14, 219, 248))  # RGB

            # Render tiles
            self.tilemap.render(self.canvas)

            # Render player
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.canvas)

            print(f'tile around: {self.tilemap.tiles_around(self.player.pos)}')


            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Keyboard Control
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.movement[0] = True
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.movement[1] = True

                    if event.key in [pygame.K_SPACE]:
                        self.player.velocity[1] = -3

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.movement[0] = False
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.movement[1] = False

            # Print on screen
            self.screen.blit(
                pygame.transform.scale(self.canvas, self.screen.get_size()),
                (0,0)
            )
            pygame.display.update()
            self.clock.tick(60)

Game().run()


