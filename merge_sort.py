import pygame
import bars
from main import clock, gameDisplay, display_height, display_width, bar_width, colors

def merge_sort(board):
    if len(board) > 1:
        middle = len(board)/2
        left_half = board[middle:]
        right_half = board[:middle]

        merge_sort(left_half)
        merge_sort(right_half)


        ### start of visualization code
        for i in range(left_half):
            left_half[i].set_color(color("green"))
        for i in range(right_half):
            right_half[i].set_color(color("blue"))

        # update board
        # todo: make a generic function to update board
        gameDisplay.fill(colors["white"])
        # redraw all the bars not being moved
        for i in range(self.number_of_bars):
            self.bars[i].draw()
        #### end of visualization code

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            ### start of visualization code
            left_half[i].set_color(colors("red"))
            right_half[j].set_color(colors("red"))
            ### end of visualization code
            
            if left_half[i] <= right_half[j]:
                board[k] = left_half[i]
                i = i + 1
            else:
                board[k] = right_half[j]
                j = j + 1
            k = k + 1

        # next two while statements account for one half being larger than the other
        while i < len(left_half):
            board[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            board[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)
