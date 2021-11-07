""" game window class of the program """

import pygame  # importing the pygame module.
import copy   # importing shallow and deep copy operations module.

""" Importing the required classes to run this game window class """

from cell_class import *

vector = pygame.math.Vector2  # Two-Dimensional vector.

""" Creating Game window class from where the actual game will be play. """

class Game_window:
    def __init__(self, screen, x, y): # Initializing the variables.
        self.screen = screen  # Initializing the game window screen.
        self.position = vector(x, y)  # Intializing the vector passed through the init function.
        self.width, self.height = 600, 600 # Setting width and height of the game window.
        self.image = pygame.Surface((self.width, self.height))  # Helps to draw one image onto another of game surface window.
        self.rectangle = self.image.get_rect() # Drawing the rectangle image onto game window screen.
        self.rows = 30 # Number of grid rows to be drawn on the game window.
        self.cols = 30 # Number of grid colums to be drawn on the game window.
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)] # Storing grid values by calculating x and y coordinate values based on given range of rows and columns and passing to the cell class.
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)

    """ Update function to update the rectangle position on different grid cells. """

    def update(self):
        self.rectangle.topleft = self.position
        for row in self.grid:
            for cell in row:
                cell.update()
    
    """ Draw function to draw the rectangle image on grid cells with the help of pygame.Surface() """

    def draw(self):
        self.image.fill((102, 102, 102))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.position.x, self.position.y)) # Draw the rectangle image of the game window.

    """ Reset grid function to reset the grid when a user click on reset button. """

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]
                     for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)

    """ Evalute function for Implementing conway's game of life rules. """
    
    def evaluate(self):
        new_grid = copy.copy(self.grid)
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()

        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                try:
                    if cell.alive:
                        if cell.alive_neighbours == 2 and cell.alive_neighbours == 3:
                            new_grid[yidx][xidx].alive = True
                        if cell.alive_neighbours < 2:
                            new_grid[yidx][xidx].alive = False
                        if cell.alive_neighbours > 3:
                            new_grid[yidx][xidx].alive = False
                    else:
                        if cell.alive_neighbours == 3:
                            new_grid[yidx][xidx].alive = True
                except(Exception):
                    print("Exception: ", Exception)

        self.grid = new_grid
