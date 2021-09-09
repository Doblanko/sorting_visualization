import time
import board

def bubble_sort(game_board):
    bars = game_board.bars
    length = len(bars)
    swap_count = 0

    # Traverse through all array elements
    for i in range(length):
        swap_count = 0
        # Last i elements are already in order
        for j in range(0, length - i - 1):
            bars[j].set_color(board.colors["green"])
            bars[j+1].set_color(board.colors["green"])
            game_board.redraw()
            time.sleep(board.sleep_time)

            if bars[j].height > bars[j+1].height:
                game_board.animate_swap(bars[j], bars[j + 1], bars[j+1].height, bars[j].height)
                swap_count += 1
            else:
                time.sleep(board.sleep_time)

                bars[j].set_color(board.colors["black"])
                bars[j + 1].set_color(board.colors["black"])
                game_board.redraw()
        if swap_count == 0:
            break


