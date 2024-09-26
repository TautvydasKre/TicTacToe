from pythonProject.modules.constants import *

# Dimensions and constants
LINE_WIDTH = 10
SQUARE_SIZE = 200
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
OFFSET_X = 75
OFFSET_Y = 75
LINE_COLOR = (31, 10, 17)


def draw_lines():

    # Horizontal lines
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (OFFSET_X, OFFSET_Y + row * SQUARE_SIZE),
                         (OFFSET_X + GAME_WIDTH, OFFSET_Y + row * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y),
                         (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y + GAME_HEIGHT), LINE_WIDTH)


def draw_figures(board):

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            center_x = OFFSET_X + col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = OFFSET_Y + row * SQUARE_SIZE + SQUARE_SIZE // 2

            if board[row][col] == 1:  # Player 1 (X)
                pygame.draw.line(screen, BLUE,
                                 (center_x - CIRCLE_RADIUS, center_y - CIRCLE_RADIUS),
                                 (center_x + CIRCLE_RADIUS, center_y + CIRCLE_RADIUS),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, BLUE,
                                 (center_x - CIRCLE_RADIUS, center_y + CIRCLE_RADIUS),
                                 (center_x + CIRCLE_RADIUS, center_y - CIRCLE_RADIUS),
                                 CROSS_WIDTH)
            elif board[row][col] == 2:  # Player 2 (O)
                pygame.draw.circle(screen, RED,
                                   (center_x, center_y),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
