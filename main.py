import pygame
import sys
from game_window_class import *
from button_class import *

""" Pygame display settings. """

WIDTH, HEIGHT = 800, 800  # Setting width and height of the pygame window
BACKGROUND = (199, 199, 199)  # Setting pygame window background colour
FPS = 60  # Setting speed of the game play
pygame.display.set_caption("Conway's  Game  of  Life")  # Setting caption of the game 

#<------------------------SETTING FUNCTIONS--------------------->

def get_events():
    try:
        global running
        for event in pygame.event.get(): # fetching all the events occurs previously one by one from (pygame.event.get()) method.
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_on_grid(mouse_position):
                    click_cell(mouse_position)
                else:
                    for button in buttons:
                        button.click()
    except(Exception) :
        print("Exception occurs in handling mouse event: ", Exception)

def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)


def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#<------------------------RUNNING FUNCTIONS--------------------->

def running_get_events():
    try:
        global running
        for event in pygame.event.get():  # fetching all the events occurs previously one by one from (pygame.event.get()) method.
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

def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)
    try:
        if frame_count % (FPS // 10) == 0:
            game_window.evaluate()
    except ValueError as e:
        print("Number is not divisible by FPS: ", e)


def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#<------------------------PAUSED FUNCTIONS--------------------->

def paused_get_events():
    try:
        global running
        for event in pygame.event.get(): # fetching all the events occurs previously one by one from (pygame.event.get()) method.
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

def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)


def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

""" Calculating the mouse position. """

def mouse_on_grid(position): # Calculating the mouse position on the grid cells
    try:
        if position[0] > 100 and position[0] < WIDTH - 100:
            if position[1] > 100 and position[1] < HEIGHT - 20:
                return True
        return False
    except(Exception):
        print("Exception: ", Exception)

""" Calculating the clicking events on grid of cells position. """

def click_cell(position): # Check the mouse clicking event on the grid cells and take decision to make it alive the cells or not.
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

""" Calculating and creating the different buttons with respect to position from the size of the window. """

def make_buttons(): # Creating buttons on the pygame window 
    buttons = []
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='RUN', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='setting')) # Appending 'RUN' button details in the button list.
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='PAUSE', colour=(18, 104, 135), hover_colour=(51, 168, 212), bold_text=True, function=pause_game, state='running')) # Appending 'PAUSE' button details in the button list.
    buttons.append(Button(window, WIDTH // 4 - 50, 50, 100, 30, text='RESET', colour=(117, 14, 14), hover_colour=(217, 54, 54), bold_text=True, function=reset_grid, state='paused')) # Appending 'RESET' button details in the button list.
    buttons.append(Button(window, WIDTH // 1.25 - 50, 50, 100, 30, text='RESUME', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='paused')) # Appending 'RESUME' button details in the button list.

    return buttons

""" Different state of the game that is running, stop and reset. """

def run_game():
    global state
    state = 'running'


def pause_game():
    global state
    state = 'paused'


def reset_grid():
    global state
    state = 'setting'
    game_window.reset_grid()

""" Intializing the game and set the display setting, clock, buttons, state and frame count. """

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Display setting of the pygame window.
clock = pygame.time.Clock() # Create an object to help track time.
game_window = Game_window(window, 100, 180) # Rectangle size window drwan from where the actual game will be played.
buttons = make_buttons() 
state = 'setting'
frame_count = 0

running = True
while running:
    frame_count += 1
    mouse_position = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update() # Always update the pygame display window whenever new things added to the game.
    clock.tick(FPS) # Controlling speed of the game play.

""" Quit the game at the end and get exit. """

pygame.quit() 
sys.exit()