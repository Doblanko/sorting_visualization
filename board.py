import pygame, time
import bars

display_width = 600
display_height = 500
bar_width = 30
sleep_time = 0.15
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "grey": (200, 200, 200),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "red": (255, 0, 0),
}

class Board():
    '''Creates the board that will be filled with bars of random height'''

    def __init__(self, gameDisplay, clock):
        self.number_of_bars = int(display_width / bar_width)
        self.bars = []
        self.generate_bars()
        self.gameDisplay = gameDisplay
        self.clock = clock

    def generate_bars(self):
        """Generate bars and initially draw them"""
        for i in range(self.number_of_bars):
            new_bar = bars.Bar(i)
            new_bar.draw()
            self.bars.append(new_bar)

    def redraw(self):
        # redraw all the bars
        self.gameDisplay.fill(colors["white"])
        for i in range(self.number_of_bars):
            self.bars[i].draw()

        pygame.display.update()


    def animate_swap(self, bar_1, bar_2, short_bar, tall_bar):
        """Animate bars swapping position"""
        swapping = True
        bar_1_starting_position = bar_1.x_pixel
        bar_2_starting_position = bar_2.x_pixel

        while swapping:
            # clear the display
            self.gameDisplay.fill(colors["white"])

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
            self.clock.tick(30)

            # check if the bars are done moving
            if bar_1.x_pixel == bar_2_starting_position:
                self.redraw()

                swapping = False
                time.sleep(sleep_time)

                # reset the positions and swap the heights instead of moving the position of the bars
                # TODO: See if you should reset the position then recalc the x_pixel instead (see bar class)
                bar_1.x_pixel = bar_1_starting_position
                bar_2.x_pixel = bar_2_starting_position
                bar_1.height = short_bar
                bar_2.height = tall_bar
                bar_1.set_color(colors["black"])
                bar_2.set_color(colors["black"])

                self.redraw()


