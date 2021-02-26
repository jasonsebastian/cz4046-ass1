from models.state import State

from utils.const import *


class GridEnvironment:
    def __init__(self):
        self.grid = [[State() for _ in range(NUM_COLS)]
                     for _ in range(NUM_ROWS)]
        self.build_grid()
        self.duplicate_grid()

    def build_grid(self):
        self.set_squares(GREEN_SQUARES, GREEN_REWARD)
        self.set_squares(BROWN_SQUARES, BROWN_REWARD)
        self.set_squares(WALLS_SQUARES, WALL_REWARD, is_wall=True)

    def set_squares(self, squares_info, reward, is_wall=False):
        squares = [tuple(map(int, s.strip().split(COL_ROW_DELIM)))
                   for s in squares_info.split(GRID_DELIM)]
        for r, c in squares:
            self.grid[r][c].reward = reward
            self.grid[r][c].is_wall = is_wall

    def duplicate_grid(self):
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if i >= 6 or j >= 6:
                    true_i = i % 6
                    true_j = j % 6
                    self.grid[i][j].reward = self.grid[true_i][true_j].reward
                    self.grid[i][j].is_wall = self.grid[true_i][true_j].is_wall

    def print_grid(self):
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                print('{:>5}  '.format(str(self.grid[i][j])), end='')
            print()
