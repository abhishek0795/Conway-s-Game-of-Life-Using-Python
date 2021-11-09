""" Game Window class of the program """

import pygame  # importing the pygame module.
import copy   # importing shallow and deep copy operations module.
from cell_class import *  # importing the required classes to run this game window class.

vector = pygame.math.Vector2  # Two-Dimensional vector.

class Game_window:
    """ Creating Game window class from where the actual game will be play. """
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

    def update(self): # Updating the events whenever new events called.
        """ Update function to update the rectangle position on different grid cells. """
        # self.rectangle.topleft = self.position
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self): # Drawing the image onto the game window.
        """ Draw function to draw the rectangle image on grid cells with the help of pygame.Surface() """
        # self.image.fill((102, 102, 102))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.position.x, self.position.y)) # Draw the rectangle image of the game window.

    def reset_grid(self): # Reset the grid when reset function is called.
        """ Reset grid function to reset the grid when a user click on reset button. """
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
    
    def evaluate(self): # Identifying the neighbours and check the conditions of live state of the grid cells.
        """ Evalute function for Implementing conway's game of life rules. """
        new_grid = copy.copy(self.grid) # Storing the shallow copy of the grid cells.
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
