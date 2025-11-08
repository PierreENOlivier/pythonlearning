"""
Generate a grid to place tiles on
"""
class Grid:
    def __init__(self, game, size_grid=(5, 5), tile_size=16):
        self.game = game
        self.size_grid = size_grid
        self.tile_size = tile_size
        self.grid = {}

        # add walls on outer
        ## Horizontal
        for x in range(self.size_grid[0]):
            self.grid[str(x) + ';0'] = {'type': 'wall', 'pos':(x, 0)}
            self.grid[str(x) + f';{self.size_grid[1]}'] = {'type': 'wall', 'pos': (x, 0)}

        ## Vertical
        for y in range(self.size_grid[1]):
            self.grid['0;' + str(y)] = {'type': 'wall', 'pos':(0, y)}
            self.grid[f';{self.size_grid[0]}' + str(y)] = {'type': 'wall', 'pos': (y, 0)}

        # place floor
        for xx in range(1, self.size_grid[0] - 1):
            for yy in range(1, self.size_grid[1] - 1):
                self.grid[str(xx) + ';' + str(yy)] = {'type': 'floor', 'pos': (xx, yy)}


    def center_on_screen(self, screen):
        pass
        # translocate the coordinates based on dimension of the screen

    def trace_path(self, game):
        pass
    # take game settings and difficulty
    # place an exist and go back

    def render(self):
        pass

