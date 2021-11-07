""" Button class of the program """

import pygame # importing the pygame module.

vector = pygame.math.Vector2

""" Creating button class with required settings when events happen after clicking on buttons. """

class Button:
    def __init__(self, surface, x, y, width, height, state='', id='', function=0, colour=(255, 255, 255), hover_colour=(255, 255, 255), border=True, border_width=2, border_colour=(0, 0, 0), text='', font_name='arial', text_size=20, text_colour=(0, 0, 0), bold_text=False): # Initializing the variables.
        self.type = 'button' 
        self.x = x
        self.y = y
        self.position = vector(x, y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.reactangle = self.image.get_rect()
        self.reactangle.topleft = self.position
        self.state = state
        self.id = id
        self.function = function
        self.colour = colour
        self.hover_colour = hover_colour
        self.border = border
        self.border_width = border_width
        self.border_colour = border_colour
        self.text = text
        self.font_name = font_name
        self.text_size = text_size
        self.text_colour = text_colour
        self.bold_text = bold_text
        self.hovered = False
        self.showing = True

    def update(self, position, game_state=''): # Updating the events based on the mouse cursor position and the game state.
        try:
            if self.mouse_hovering(position):
                self.hovered = True
            else:
                self.hovered = False
        except(Exception):
            print("Exception occurs in handling mouse event: ", Exception)
        try:
            if self.state == '' or game_state == '':
                self.showing = True
            else:
                if self.state == game_state:
                    self.showing = True
                else:
                    self.showing = False
        except(Exception):
            print("Exception: ", Exception)

    def draw(self): # Draw the image based on the changes occurs in the game window.
        try:
            if self.showing:
                if self.border:
                    self.image.fill(self.border_colour)
                    if self.hovered:
                        pygame.draw.rect(self.image, self.hover_colour, (self.border_width, self.border_width, self.width - (self.border_width * 2), self.height - (self.border_width * 2)))
                    else:
                        pygame.draw.rect(self.image, self.colour, (self.border_width, self.border_width, self.width - (self.border_width * 2), self.height - (self.border_width * 2)))

                else:
                    self.image.fill(self.colour)

                if len(self.text) > 0:
                    self.show_text()
                self.surface.blit(self.image, self.position) # Draw the rectangle image of the buttons icon.
        except(Exception):
            print("Exception: ", Exception)

    def click(self): # Click function helps to identify whether the mouse is hovered or not in the grid cells.
        try:
            if self.function != 0 and self.hovered:
                self.function()
        except(Exception):
            print("Exception: ", Exception)

    def show_text(self): # Show text function will set the text on the text button.
        font = pygame.font.SysFont(self.font_name, self.text_size, bold=self.bold_text)
        text = font.render(self.text, False, self.text_colour)
        size = text.get_size()
        x, y = self.width // 2 - (size[0] // 2), self.height // 2 - (size[1] // 2)
        position = vector(x, y)
        self.image.blit(text, position)   # Draw the rectangle image on the grid cells.

    def mouse_hovering(self, position): # Mouse hovering function to check the hovering events based on the cursor position.
        try:
            if self.showing:
                if position[0] > self.position[0] and position[0] < self.position[0] + self.width:
                    if position[1] > self.position[1] and position[1] < self.position[1] + self.height:
                        return True
                    else:
                        return False
            else:
                return False
        except(Exception):
            print("Exception: ", Exception)