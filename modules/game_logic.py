
from pythonProject.modules.constants import *

def check_win(board, player):

    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):
    global consecutive_draws
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


def reset_board():

    return [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def clear_screen():

    screen.fill(BG_COLOR)
    pygame.display.update()