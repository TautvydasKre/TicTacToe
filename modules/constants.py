import pygame

pygame.init()

# Dimensions and constants
APP_WIDTH, APP_HEIGHT = 750, 750
GAME_WIDTH, GAME_HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_COLS = 3
BOARD_ROWS = 3
SQUARE_SIZE = GAME_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
RED = (206, 45, 79)
BLUE = (24, 49, 242)
BG_COLOR = (186, 160, 179)
LINE_COLOR = (31, 10, 17)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont('monospace', 50)

# Set up the display
screen = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Offset to center the game board within the app window
OFFSET_X = (APP_WIDTH - GAME_WIDTH) // 2
OFFSET_Y = (APP_HEIGHT - GAME_HEIGHT) // 2

