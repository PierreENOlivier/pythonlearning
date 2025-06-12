import pygame

NEIGHBOR_OFFSET = [
    (-1, 0), # left
    (-1, -1), # left up
    (0, -1), # up
    (1, -1), # right up
    (1, 0), # right
    (1, 1), # right down
    (0, 1), # down
    (-1, 1) # left down
] # coordinates go up in the negative because axis increases to the right and down

PHYSICS_TILES = {'grass', 'stone'} # List tile types that have physics

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {} # grid for physics
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    """
    Find nearby tiles to the position
    """
    def tiles_around(self, pos):
        tile_loc = (
            int(pos[0] // self.tile_size),
            int(pos[1] // self.tile_size),
        ) # the expanded position has to be converted to the position; integer division

        tiles = []
        for offset in NEIGHBOR_OFFSET:
            check_loc = (
                str(tile_loc[0] + offset[0]) # X
                + ';' + str(tile_loc[1] + offset[1]) # Y
            )
            # Save as string to follow key format of tilemap dictionary

            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])

        return tiles

    """
    Check tiles around character and filter those that have physics attributes
    """
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(
                    tile['pos'][0] * self.tile_size, # X position in pixels
                    tile['pos'][1] * self.tile_size, # Y position in pixels
                    self.tile_size, # width tile on X
                    self.tile_size, # height tile on Y
                ))

        return rects


    def render(self, surf):
        # Look for the location in the dictionary

        # Render offgrid tiles in the background
        for tile in self.offgrid_tiles:
            surf.blit(
                self.game.assets[tile['type']][tile['variant']],
                tile['pos']
            )

        # Render tiles on grid in the foreground
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            # print(f'Tile "{tile}" at location ({loc})')
            surf.blit(
                self.game.assets[tile['type']][tile['variant']],
                (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size)
            )