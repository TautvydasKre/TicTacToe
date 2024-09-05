import pygame

pygame.init()

# Demensions and constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_COLS = 3
BOARD_ROWS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
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
FONT = pygame.font.SysFont('monospace',40)

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

