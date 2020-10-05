import pygame, random
from main import display_height, display_width, bar_width, colors

class Bar():

    def __init__(self, position):
        self.height = random.randrange(10, 500, 10)
        self.color = colors["black"]
        self.position = position

        # x location of top left pixel
        self.x_pixel = position * bar_width

        # the drawing of the bar
        self.image = None

    def set_color(self, color):
        self.color = color

    def draw(self):
        x_coord = self.x_pixel
        # need to invert since height starts from the top and goes down
        y_coord = display_height - self.height

        # draw the bar 1 pixel narrower than the allotted space to have borders
        self.image = pygame.draw.rect(pygame.display.get_surface(), self.color, (x_coord + 1, y_coord,
                                                                                      bar_width - 2, self.height))