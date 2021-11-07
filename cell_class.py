""" Cell class of the program """

import pygame  # importing the pygame module.

""" Creating cell class which helps to create the rectangle image on cell and also check the neighbour cells are alive or not and take decisions. """

class Cell:
    def __init__(self, surface, grid_x, grid_y): #Intializing the variables.
        self.alive = False      # Intializing the live neighbours boolean value to false.         
        self.surface = surface  # Intializing the surface variable.
        self.grid_x = grid_x    # Intializing the grid position of x-direction.
        self.grid_y = grid_y    # Initializing the grid position of y-direction.
        self.image = pygame.Surface((20, 20))  # Size of the each grid cells.
        self.reactangle = self.image.get_rect() # Calling the rectangle image and storing in the rectangle variable.
        self.neighbours = [] # Intializing the list of neighbours.
        self.alive_neighbours = 0 # Intializing the live neighbours count.

    def update(self): # Update the grid cells.
        self.reactangle.topleft = (self.grid_x * 20, self.grid_y * 20) # It will start updating the grid cells from the topleft corner of the game window.
    
    """ Draw function helps to draw the rectangle image and filling the colour if cell is alive. """

    def draw(self): # Draw the cell image
        try:
            if self.alive: 
                self.image.fill((0,0,0)) # Filling the black colour image in reactangle shape if neigbours is alive.
            else:
                # self.image.fill((0, 0, 0)) 
                pygame.draw.rect(self.image, (255, 255, 255), (1, 1, 18, 18)) # Filling the cell colour and setting border width.
            self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20)) # Draw the rectangle image on the grid cells.
        except(Exception):
            print("Exception: ", Exception)

    """ Get neighbours function helps to identify the neighbours of each grid cells. """

    def get_neighbours(self, grid): # Get the neighbours details
        neighbour_list = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, -1], [0, 1],[1, 0], [-1, 0]] # Checking neighbours in all the eight directions.
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x  # Updating the neighbours list of first position in grid x-direction.
            neighbour[1] += self.grid_y  # Updating the neighbours list of first position in grid y-direction.
        for neighbour in neighbour_list: 
            try:
                if neighbour[0] < 0:
                    neighbour[0] += 30
                if neighbour[1] < 0:
                    neighbour[1] += 30
                if neighbour[1] > 29:
                    neighbour[1] -= 30
                if neighbour[0] > 29:
                    neighbour[0] -= 30
            except(Exception):
                print("Exception: ",Exception)
        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except:
                print(neighbour)

    """ Live neighbours function checks whether the neighbours of grid cells are alive or not. """

    def live_neighbours(self): # Increamenting the count variable whenever live neighbour gets encountered.
        count = 0
        for neighbour in self.neighbours:
            try:
                if neighbour.alive:
                    count += 1
            except(Exception):
                print("Exception: ",Exception)

        self.alive_neighbours = count

