import pygame, time
import board

sleep_time = 1

def merge_sort(bars, game_board):
    if len(bars) > 1:
        # show section being looked at
        color(game_board, bars, board.colors["green"])
        time.sleep(sleep_time)

        middle = int(len(bars)/2)
        left_half = bars[:middle]
        right_half = bars[middle:]

        # color halves
        color(game_board, left_half, board.colors["blue"])
        color(game_board, right_half, board.colors["red"])
        time.sleep(sleep_time)
        # uncolor
        color(game_board, left_half, board.colors["black"])
        color(game_board, right_half, board.colors["black"])
        time.sleep(sleep_time)

        merge_sort(left_half, game_board)
        merge_sort(right_half, game_board)

        i = 0
        j = 0

        # need to store the heights in a temporary variable. bars, left_half, and right_half only reference bar
        # objects (they don't store them). If you change bars during the sorting, you will change the actual objects
        # and subsequently change left_half and right_half since they reference the same objects

        temp_height = []
        while i < len(left_half) and j < len(right_half):
            if left_half[i].height <= right_half[j].height:
                temp_height.append(left_half[i].height)
                i = i + 1
            else:
                temp_height.append(right_half[j].height)
                j = j + 1

        # next two while statements account for one half being larger than the other
        while i < len(left_half):
            temp_height.append(left_half[i].height)
            i = i + 1

        while j < len(right_half):
            temp_height.append(right_half[j].height)
            j = j + 1

        # change the bar objects after comparison complete
        k = 0
        for bar in bars:
            bar.height = temp_height[k]
            k = k + 1

        # redraw bars
        game_board.redraw()
        time.sleep(sleep_time)

def color(game_board, bars, color):
    for bar in bars:
        bar.set_color(color)

    game_board.redraw()


# only temporarily changes the color of a bar
# todo: make a separate redraw and recolor function. Recolor just draws over the old bar. Redraw draws the whole
#  section again after merging.
def draw_color():
    for i in range(temp_bars.number_of_bars):
        temp_bars[i].draw()

