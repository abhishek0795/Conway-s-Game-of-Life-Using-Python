""" Game Project: Conway's Game of Life Using Python """

""" Main class of the program """

import pygame # importing the pygame module.
from game_window_class import *  # importing the required classes to run this main class.
from button_class import * # importing the required classes to run this main class.

""" Pygame display settings. """

WIDTH, HEIGHT = 800, 800  # Setting width and height of the pygame window.
BACKGROUND = (199, 199, 199)  # Setting pygame window background colour.
FPS = 60  # Setting speed of the game play.
pygame.display.set_caption("Conway's  Game  of  Life")  # Setting caption of the game .

#<------------------------SETTING FUNCTIONS--------------------->

def get_events(): # Initial state of the game which will set all the necessary events to play the game.
    try:
        global running # Intializing the global variable
        for event in pygame.event.get(): # Fetching all the events occurs previously one by one from (pygame.event.get()) method.
            if event.type == pygame.QUIT: # When the cancel button get clicked the running state of the fame window get closed.
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Identifying the cursor position of the mouse.
                mouse_position = pygame.mouse.get_pos() # Storing the cursor position of the mouse.
                if mouse_on_grid(mouse_position): # Passing the mouse position value to check whether button is clicked or not.
                    click_cell(mouse_position)  # Calling click cell function and passing mouse position value to get the number of click happened in the different cells.
                else:
                    for button in buttons:
                        button.click()
    except(Exception) :
        print("Exception occurs in handling mouse event: ", Exception)

def update(): # Updating the events whenever new events called.
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)


def draw(): # Drawing the image onto the game window.
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#<------------------------RUNNING FUNCTIONS--------------------->

def running_get_events():  # Running state of the game when events get called.
    try:
        global running # Intializing the global variable
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_on_grid(mouse_position):
                    click_cell(mouse_position)
                else:
                    for button in buttons:
                        button.click()
    except(Exception):
        print("Exception occurs in handling mouse event: ", Exception)

def running_update():  # Updating the running events whenever new events called.
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)
    try:
        if frame_count % (FPS // 10) == 0:
            game_window.apply_rules()
    except ValueError as e:
        print("Number is not divisible by FPS: ", e)


def running_draw():  # Drawing the image onto the game window in running state.
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#<------------------------PAUSED FUNCTIONS--------------------->

def paused_get_events():  # Paused state of the game when events get called.
    try:
        global running # Intializing the global variable
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_on_grid(mouse_position):
                    click_cell(mouse_position)
                else:
                    for button in buttons:
                        button.click()
    except(Exception):
        print("Exception occurs in handling mouse event: ", Exception)

def paused_update():   # Updating the paused events whenever new events called.
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)


def paused_draw():  # Drawing the image onto the game window in paused state.
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

def mouse_on_grid(position): # Calculating the mouse position on the grid cells.
    """ Calculating the mouse position. """
    try:
        if position[0] > 100 and position[0] < WIDTH - 100:
            if position[1] > 100 and position[1] < HEIGHT - 20:
                return True
        return False
    except(Exception):
        print("Exception: ", Exception)

def click_cell(position): # Check the mouse clicking event on the grid cells and take decision to make it alive the cells or not. 
    """ Calculating the clicking events on grid of cells position. """
    grid_position = [position[0] - 100, position[1] - 180] # Calculating the click position in grid cells between x,y directions.
    grid_position[0] = grid_position[0] // 20 # Calculating the position of the cell in x-direction divided by the cell size of the game window.
    grid_position[1] = grid_position[1] // 20  # Calculating the position of the cell in y-direction divided by the cell size of the game window.
    try:
        if game_window.grid[grid_position[1]][grid_position[0]].alive: # Checking the alive state of grid position in x and y direction and make it true if it is in alive state
            game_window.grid[grid_position[1]][grid_position[0]].alive = False
        else:
            game_window.grid[grid_position[1]][grid_position[0]].alive = True # Checking the alive state of grid position in x and y direction and make it true if it is in dead state
    except(Exception):
        print("Exception: ", Exception)

def make_buttons(): # Creating buttons on the pygame window 
    """ Calculating and creating the different buttons with respect to position from the size of the window. """
    buttons = []
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='RUN', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='setting')) # Appending 'RUN' button details in the button list.
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='PAUSE', colour=(18, 104, 135), hover_colour=(51, 168, 212), bold_text=True, function=pause_game, state='running')) # Appending 'PAUSE' button details in the button list.
    buttons.append(Button(window, WIDTH // 4 - 50, 50, 100, 30, text='RESET', colour=(117, 14, 14), hover_colour=(217, 54, 54), bold_text=True, function=reset_grid, state='paused')) # Appending 'RESET' button details in the button list.
    buttons.append(Button(window, WIDTH // 1.25 - 50, 50, 100, 30, text='RESUME', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='paused')) # Appending 'RESUME' button details in the button list.

    return buttons

def run_game(): # Create run game function and changed the state to running mode.
    global state  # Intializing the global variable
    state = 'running'


def pause_game(): # Create pause game function and changed the state to paused mode.
    global state # Intializing the global variable
    state = 'paused'


def reset_grid(): # Create reset game function and changed the state to original mode.
    global state # Intializing the global variable
    state = 'setting'
    game_window.reset_grid()

pygame.init() # Starting the game.
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Display setting of the pygame window.
clock = pygame.time.Clock() # Create an object to help track time.
game_window = Game_window(window, 100, 180) # Rectangle size window drwan from where the actual game will be played.
buttons = make_buttons()  # Calling the button function.
state = 'setting' # Setting the state to initial setting mode. 
frame_count = 0 # The frame rate or refresh rate is the number of pictures that the program draws per second is initialized to 0.

running = True # Assigned boolean value to the running variable.
while running: # Checking the condition if the game is running state then it will perform several tasks.
    frame_count += 1 # Increamenting the frame count whenever new image get drawn onto the window.
    mouse_position = pygame.mouse.get_pos() # Get the mouse position value.
    if state == 'setting': # Checking the state and calling all the function one by one that belongs to setting state.
        get_events()
        update()
        draw()
    if state == 'running':  # Checking the state and calling all the function one by one that belongs to running state.
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':  # Checking the state and calling all the function one by one that belongs to paused state.
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update() # Always update the pygame display window whenever new things added to the game.
    clock.tick(FPS) # Controlling speed of the game play.

pygame.quit() # Quit the game
