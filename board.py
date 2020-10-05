import pygame
import bars
from main import clock, gameDisplay, display_height, display_width, bar_width, colors

class Board():
    '''Creates the board that will be filled with bars of random height'''

    def __init__(self):
        self.number_of_bars = int(display_width / bar_width)
        self.bars = []
        self.generate_bars()

    def generate_bars(self):
        """Generate bars and initially draw them"""
        for i in range(self.number_of_bars):
            new_bar = bars.Bar(i)
            new_bar.draw()
            self.bars.append(bars.Bar(i))

        self.animate_swap(self.bars[1], self.bars[50])

    def animate_swap(self, bar_1, bar_2):
        """Animate bars swapping position"""
        swapping = True
        bar_1_starting_position = bar_1.x_pixel
        bar_2_starting_position = bar_2.x_pixel

        while swapping:
            # clear the display
            gameDisplay.fill(colors["white"])

            # redraw all the bars not being moved
            for i in range(self.number_of_bars):
                if i != (bar_1.position or bar_2.position):
                    self.bars[i].draw()

            # highlight the bars about to be swapped
            bar_1.set_color(colors["blue"])
            bar_2.set_color(colors["blue"])

            # move the bars 1 pixel each time
            bar_1.x_pixel += 5
            bar_2.x_pixel -= 5

            self.bars[bar_1.position].draw()
            self.bars[bar_2.position].draw()

            # update the board to display all the changes
            pygame.display.update()
            clock.tick(120)

            # check if the bars are done moving
            if bar_1.x_pixel == bar_2_starting_position:
                swapping = False


