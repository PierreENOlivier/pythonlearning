import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False,
                           'down': False,
                           'left': False,
                            'right': False} # Keep track of previous collision

    def rect(self):
        return pygame.Rect(self.pos[0],
                           self.pos[1],
                           self.size[0], # width
                           self.size[1]) # height

    def update(self, tilemap, movement=(0, 0)):
        # Reset collision memory each frame
        self.collisions = {'up': False,
                           'down': False,
                           'left': False,
                           'right': False}  # Keep track of previous collision

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # Collision on X and Y is split to more easily detect collision
        self.pos[0] += frame_movement[0]
        # Apply collision physics
        entity_rect = self.rect() # Create a rectangle around current object

        # Check surrounding tiles for collision
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Check direction of collision
                if frame_movement[0] > 0: # If > 0 on X, then moving right and right edge  collided with left of obstacle
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0: # If < 0 on X, then moving left and left edge collided with right of obstacle
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        # Apply collision physics
        entity_rect = self.rect()  # Create a rectangle around current object

        # Check surrounding tiles for collision
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Check direction of collision
                if frame_movement[1] > 0:  # If > 0 on Y, then moving down and bottom edge  collided with top of obstacle
                    entity_rect.bottom = rect.top
                    self.collisions['bottom'] = True
                if frame_movement[1] < 0:  # If < 0 on Y, then moving up and top edge collided with bottom of obstacle
                    entity_rect.top = rect.bottom
                    self.collisions['top'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        print(f'Position player: {frame_movement} at velocity {self.velocity}')

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)