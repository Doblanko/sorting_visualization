import pygame, threading, time
import board, bubble_sort, merge_sort



if __name__ == '__main__':
    clock = pygame.time.Clock()
    sorting_algorithm = 'bubble_sort'
    pygame.init()
    gameDisplay = pygame.display.set_mode((board.display_width, board.display_height))
    pygame.display.set_caption('Sorting Visualization')
    gameDisplay.fill(board.colors["white"])

    game_board = board.Board(gameDisplay, clock)

    crashed = False

    while not crashed:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    sorting_algorithm = 'bubble_sort'

                if event.key == pygame.K_m:
                    sorting_algorithm = 'merge_sort'

                if event.key == pygame.K_SPACE:
                    if sorting_algorithm == 'bubble_sort':
                        x = threading.Thread(target=bubble_sort.bubble_sort, args=(game_board,))
                    elif sorting_algorithm == "merge_sort":
                        x = threading.Thread(target=merge_sort.merge_sort, args=(game_board.bars, game_board))
                    x.start()

            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)