""" Wriring the game logic seperately to check the game working. """

import copy   # importing shallow and deep copy operations module.

class Grid:
    """ Grid class to implement all the logics of the game. """
    def __init__(self,grid):
        """ Initializing the variables. """
        self.life_grid=copy.copy(grid) # Storing the shallow copy of the grid cells.
    
    def is_alive(self,x,y): 
        """ Checking the neighbour condition alive or not. """
        return self.life_grid[x][y]==1
    
    def get_neighbours(self,x,y):
        """ Getting the neighbour details and return the total number of neighbours. """
        neighbours_count=0 # num
        for row in [x-1,x,x+1]:
            for column in [y-1,y,y+1]:
                if row<0 or column<0 or row>=len(self.life_grid) or column>=len(self.life_grid):
                    pass
                elif row==x and column==y:
                    pass
                elif self.is_alive(row,column):
                    neighbours_count+=1
        return neighbours_count

    def kill_cell(self,x,y):
        """ Intializing the x,y coordinate of dead cells condition to 0. """
        self.life_grid[x][y]=0
    
    def birth_cell(self,x,y):
        """ Intializing the x,y coordinate of birth cells condition to 1. """
        self.life_grid[x][y]=1

    def size(self):
        """ Return the total length of the grid. """
        return len(self.life_grid)

    def grid_as_array(self):
        """ Return the grid in the form array. """
        return self.life_grid

    def apply_rules(self):
        """ Apply rules function for Implementing conway's game of life rules. """
        current_grid=Grid(self.life_grid)
        for x in range(0,current_grid.size()):
            for y in range(0,current_grid.size()):
                if not current_grid.is_alive(x,y) and current_grid.get_neighbours(x,y) == 3:
                    self.birth_cell(x,y)
                elif current_grid.is_alive(x,y) and current_grid.get_neighbours(x,y) < 2:
                    self.kill_cell(x,y)
                elif current_grid.is_alive(x,y) and current_grid.get_neighbours(x,y) > 3:
                    self.kill_cell(x,y)
                else:
                    pass
        