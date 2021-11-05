import pygame
import sys
from game_window_class import *
from button_class import *

""" Pygame display settings. """

WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 60

#<------------------------SETTING FUNCTIONS--------------------->


def get_events():
    global running
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
    global running
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


def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)
    if frame_count % (FPS // 10) == 0:
        game_window.evaluate()


def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()


#<------------------------PAUSED FUNCTIONS--------------------->


def paused_get_events():
    global running
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


def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_position, game_state=state)


def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

""" Calculating the mouse position """

def mouse_on_grid(position):
    if position[0] > 100 and position[0] < WIDTH - 100:
        if position[1] > 100 and position[1] < HEIGHT - 20:
            return True
    return False

""" Calculating the clicking events on grid of cells position """

def click_cell(position):
    grid_position = [position[0] - 100, position[1] - 180]
    grid_position[0] = grid_position[0] // 20
    grid_position[1] = grid_position[1] // 20
    if game_window.grid[grid_position[1]][grid_position[0]].alive:
        game_window.grid[grid_position[1]][grid_position[0]].alive = False
    else:
        game_window.grid[grid_position[1]][grid_position[0]].alive = True

""" Calculating and creating the different buttons with respect to position from the size of the window """

def make_buttons():
    buttons = []
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='RUN', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='setting'))
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='PAUSE', colour=(18, 104, 135), hover_colour=(51, 168, 212), bold_text=True, function=pause_game, state='running'))
    buttons.append(Button(window, WIDTH // 4 - 50, 50, 100, 30, text='RESET', colour=(117, 14, 14), hover_colour=(217, 54, 54), bold_text=True, function=reset_grid, state='paused'))
    buttons.append(Button(window, WIDTH // 1.25 - 50, 50, 100, 30, text='RESUME', colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True, function=run_game, state='paused'))

    return buttons

""" Different state of the game that is running, stop and reset """

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

""" Intializing the game and set the display setting, clock, buttons, state and frame count """

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
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
    pygame.display.update()
    clock.tick(FPS)

""" Quit the game at the end and get exit """

pygame.quit()
sys.exit()