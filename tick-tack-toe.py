import pygame
import sys
import random
from roasts import roasts

pygame.init()

# Dimensions and constants
APP_WIDTH, APP_HEIGHT = 750, 750  # App size
GAME_WIDTH, GAME_HEIGHT = 600, 600  # Game board size
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
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


def reset_board():
    return [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def display_message(message, font, color, max_width, padding=20):
    # Split message into words for word wrapping
    words = message.split(' ')
    lines = []
    current_line = ""

    # Break the message into lines that fit within the max width
    for word in words:
        test_line = f"{current_line} {word}".strip()
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() <= max_width - 2 * padding:  # Adjust for padding
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    # Calculate the total height of the text block
    text_height = font.get_height() * len(lines)
    text_surface = pygame.Surface((max_width, text_height + 2 * padding), pygame.SRCALPHA)
    text_surface.fill(BG_COLOR)

    # Render each line of text with padding
    y_offset = padding
    for line in lines:
        line_surface = font.render(line, True, color)
        line_x = (max_width - line_surface.get_width()) // 2  # Center the line horizontally
        text_surface.blit(line_surface, (line_x, y_offset))
        y_offset += font.get_height()

    # Calculate the centered position for the text surface
    text_x = (APP_WIDTH - max_width) // 2
    text_y = (APP_HEIGHT - (text_height + 2 * padding)) // 2

    # Blit the text surface to the screen
    screen.blit(text_surface, (text_x, text_y))
    pygame.display.update()


def clear_screen():
    screen.fill(BG_COLOR)
    pygame.display.update()


def main_menu():
    clear_screen()  # Clear screen before drawing the main menu

    button_width = APP_WIDTH // 2
    button_height = APP_HEIGHT // 8
    spacing = APP_HEIGHT // 16

    button1 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3, button_width, button_height)
    button2 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3 + button_height + spacing, button_width, button_height)
    button3 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3 + 2 * (button_height + spacing), button_width, button_height)

    pygame.draw.rect(screen, WHITE, button1)
    pygame.draw.rect(screen, WHITE, button2)
    pygame.draw.rect(screen, WHITE, button3)

    vs_player_text = FONT.render('VS Player', True, BLACK)
    vs_computer_text = FONT.render('VS Computer', True, BLACK)
    exit_text = FONT.render('Exit', True, BLACK)

    screen.blit(vs_player_text, (button1.x + button1.width // 2 - vs_player_text.get_width() // 2,
                                 button1.y + button1.height // 2 - vs_player_text.get_height() // 2))
    screen.blit(vs_computer_text, (button2.x + button2.width // 2 - vs_computer_text.get_width() // 2,
                                   button2.y + button2.height // 2 - vs_computer_text.get_height() // 2))
    screen.blit(exit_text, (button3.x + button3.width // 2 - exit_text.get_width() // 2,
                            button3.y + button3.height // 2 - exit_text.get_height() // 2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    clear_screen()
                    return 'player'
                if button2.collidepoint(event.pos):
                    clear_screen()
                    return 'computer'
                if button3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def game_over_screen(winner, is_computer_win=False):
    clear_screen()  # Clear screen before drawing the game over screen

    if winner == 'draw':
        display_message("It's a draw!", FONT, WHITE, APP_WIDTH - 40)
    elif is_computer_win:
        roast_message = random.choice(roasts)
        display_message(roast_message, FONT, WHITE, APP_WIDTH - 40)
    else:
        display_message(f"Player {winner} wins!", FONT, WHITE, APP_WIDTH - 40)

    button_width = APP_WIDTH // 2
    button_height = APP_HEIGHT // 8
    spacing = APP_HEIGHT // 16

    button1 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 2 + APP_HEIGHT // 8, button_width, button_height)
    button2 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 2 + button_height + 3 * spacing, button_width, button_height)
    pygame.draw.rect(screen, WHITE, button1)
    pygame.draw.rect(screen, WHITE, button2)

    play_again_text = FONT.render('Play Again', True, BLACK)
    main_menu_text = FONT.render('Main Menu', True, BLACK)

    screen.blit(play_again_text, (button1.x + button1.width // 2 - play_again_text.get_width() // 2,
                                  button1.y + button1.height // 2 - play_again_text.get_height() // 2))
    screen.blit(main_menu_text, (button2.x + button2.width // 2 - main_menu_text.get_width() // 2,
                                 button2.y + button2.height // 2 - main_menu_text.get_height() // 2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    return 'play_again'
                if button2.collidepoint(event.pos):
                    return 'main_menu'


def minimax(board, depth, is_maximizing):
    if check_win(board, 1):
        return -10
    if check_win(board, 2):
        return 10
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] is None:
                    board[row][col] = 2  # Assume computer (O) is making the move
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] is None:
                    board[row][col] = 1  # Assume player (X) is making the move
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                board[row][col] = 2  # Assume computer (O) is making the move
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def computer_move(board):
    return find_best_move(board)


def main():
    mode = None  # Initialize mode variable to keep track of the game mode

    while True:
        if mode is None:
            mode = main_menu()  # Main menu for selecting player vs player or vs computer

        board = reset_board()  # Reset the board for a new game
        clear_screen()  # Clear the screen before drawing the game board
        draw_lines()  # Redraw the grid lines
        pygame.display.update()  # Update the display

        game_over = False
        current_player = 1  # Player 1 starts as X
        winner = None  # Initialize winner

        # The game loop (runs until 'game_over' becomes True)
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y

                    # Adjust mouse position to account for offset
                    if OFFSET_X <= mouseX <= OFFSET_X + GAME_WIDTH and OFFSET_Y <= mouseY <= OFFSET_Y + GAME_HEIGHT:
                        clicked_row = (mouseY - OFFSET_Y) // SQUARE_SIZE
                        clicked_col = (mouseX - OFFSET_X) // SQUARE_SIZE

                        # Ensure the click is within the square boundaries
                        if board[clicked_row][clicked_col] is None:
                            board[clicked_row][clicked_col] = current_player  # Mark the square
                            draw_figures(board)  # Draw X or O on the board

                            if check_win(board, current_player):
                                game_over = True
                                winner = 'X' if current_player == 1 else 'O'
                                is_computer_win = (mode == 'computer' and winner == 'O')
                                choice = game_over_screen(winner, is_computer_win=is_computer_win)

                            elif check_draw(board):
                                game_over = True
                                winner = 'draw'  # Set winner as 'draw'
                                choice = game_over_screen(winner)

                            current_player = current_player % 2 + 1  # Switch players

            if mode == 'computer' and current_player == 2 and not game_over:
                row, col = computer_move(board)  # Get computer's move
                board[row][col] = current_player  # Mark computer's move
                draw_figures(board)

                if check_win(board, current_player):
                    game_over = True
                    winner = 'O'  # Computer is always 'O'
                    choice = game_over_screen(winner, is_computer_win=True)

                elif check_draw(board):
                    game_over = True
                    winner = 'draw'
                    choice = game_over_screen(winner)

                current_player = current_player % 2 + 1  # Switch back to player

            pygame.display.update()

        # Game Over: Handle "Play Again" or "Main Menu"
        if choice == 'play_again':
            # Reset game state: board, current player, etc.
            board = reset_board()  # Reset the board for the new game
            game_over = False  # Set game_over to False for the new game
            current_player = 1  # Player 1 starts again as X
            winner = None  # Reset the winner

            clear_screen()  # Clear the screen before starting a new game
            draw_lines()  # Redraw the grid lines
            pygame.display.update()  # Update the display

            # Clear any previous events
            pygame.event.clear()

            # Wait for the next event loop to process correctly
            pygame.time.wait(100)  # Small delay to ensure screen update

        elif choice == 'main_menu':
            mode = None  # Reset mode to None to show the main menu again
            clear_screen()  # Clear the screen before going back to the main menu
            pygame.display.update()  # Ensure display is updated
            # Optionally, you can add a small delay to ensure the screen update
            pygame.time.wait(100)


if __name__ == "__main__":
    main()
