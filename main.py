import pygame, threading
import board, bars

display_width = 1000
display_height = 500
bar_width = 10
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "grey": (200, 200, 200),
    "blue": (0, 0, 255),
}
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))


if __name__ == '__main__':
    sorting_algorithm = 'quicksort'
    pygame.init()
    pygame.display.set_caption('Sorting Visualization')
    gameDisplay.fill(colors["grey"])

    game_board = board.Board()

    crashed = False

    while not crashed:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    solution_algorithm = 'dijkstra'

                if event.key == pygame.K_a:
                    solution_algorithm = 'a_star'

                #if event.key == pygame.K_SPACE:

                    #x = threading.Thread(target=a_star.a_star_solver, args=()
                    #x.start()

            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)