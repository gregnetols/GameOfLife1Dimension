import numpy as np
import pygame, sys
import GOL1d

gameInputs = {'height': 256,
              'width': 513,
              'FPS': 30,
              'black': (0,0,0),
              'red': (255,0,0),
              'grey': (30,30,30),
              'cellSize': 5}


# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# setup window
window = pygame.display.set_mode(((gameInputs['width'] * gameInputs['cellSize']),
                                (gameInputs['height'] * gameInputs['cellSize'])))
pygame.display.set_caption('Conway''s Game of Life in 1D')
window.fill(gameInputs['black'])

# initialize board
board = GOL1d.initialize_board(gameInputs['height'], gameInputs['width'])
generation = 1

# Main Loop
while True:

    # Check if user wants to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if generation < gameInputs['height']:
        # Take game turn
        board = GOL1d.game_of_life_turn(board, generation)

        # draw grid
        for row in range(0, (gameInputs['height'] * gameInputs['cellSize']), gameInputs['cellSize']):
            for col in range(0, (gameInputs['width'] * gameInputs['cellSize']), gameInputs['cellSize']):
                if board[row//gameInputs['cellSize']][col//gameInputs['cellSize']] == 1:
                    pygame.draw.rect(window, gameInputs['red'], [col, row, gameInputs['cellSize'], gameInputs['cellSize']])
                else:
                    pygame.draw.rect(window, gameInputs['black'], [col, row, gameInputs['cellSize'], gameInputs['cellSize']])
                pygame.draw.rect(window, gameInputs['grey'], [col, row, gameInputs['cellSize'], gameInputs['cellSize']], 1)

        generation = generation + 1

    # redraw board
    pygame.display.update()

    # refresh frequency
    clock.tick(gameInputs['FPS'])