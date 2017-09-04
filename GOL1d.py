import numpy as np


# creates a game of life board and sets the midpoint cell in the first row to 1
# inputs:
#   height - height of the board
#   width - width of the board
# returns:
#   board - a initial game of life board
def initialize_board(height, width):
    midpoint = width//2
    board = np.zeros((height, width))
    board[0,midpoint] = 1
    return board


# performs one turn of game of life using the XOR logic
# inputs:
#   board - a game of life board
#   generation - the current generation of the game
# returns:
#   board - an updated game of life board
def game_of_life_turn(board, generation):
    for x in range(1, len(board[0,:])-1):
        if board[generation-1, x-1] != board[generation-1, x+1]:
            board[generation, x] = 1
    return board


