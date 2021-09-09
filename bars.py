import pygame, random
import board

#todo: look at making bar a subclass of board
class Bar():

    def __init__(self, position):
        self.height = random.randrange(10, 500, 10)
        self.position = position
        self.color = board.colors["black"]

        # x location of top left pixel
        self.x_pixel = position * board.bar_width

        # the drawing of the bar
        self.image = None

    def set_color(self, color):
        self.color = color

    def draw(self):
        x_coord = self.x_pixel
        # need to invert since height starts from the top and goes down
        y_coord = board.display_height - self.height

        # draw the bar 1 pixel narrower than the allotted space to have borders
        self.image = pygame.draw.rect(pygame.display.get_surface(), self.color, (x_coord + 1, y_coord,
                                                                                 board.bar_width - 2, self.height))