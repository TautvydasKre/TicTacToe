import pygame
import sys
import random
from roasts import roasts

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

consecutive_draws = 0


def draw_lines():
    """
    This function: draws horizontal and vertical lines to draw a TicTacToe board
    :return: None
    """
    # Horizontal lines
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (OFFSET_X, OFFSET_Y + row * SQUARE_SIZE),
                         (OFFSET_X + GAME_WIDTH, OFFSET_Y + row * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y),
                         (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y + GAME_HEIGHT), LINE_WIDTH)


def draw_figures(board):
    """
    This function: Draws the figures (X and O) on the Tic-Tac-Toe board based on the current state of the board.
    :param board: A 2D list representing the Tic-Tac-Toe board where each cell contains
                  either 1 (for X), 2 (for O), or None (for an empty cell).
    :return: None
    """
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
    """
    This function: checks if the specified player has won the game.

    :param board: a 2D list representing the Tic-Tac-Toe board where each cell contains
                  either 1 (for player X), 2 (for player O), or None (for an empty cell).
    :param player: An integer representing the player to check for a win. 1 for player X, 2 for player O.
    :return: True if the specified player has won the game, otherwise False.
    """
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
    """
    This function: checks if the game is a draw, meaning all cells are filled and no player has won.
    :param board: a 2D list representing the Tic-Tac-Toe board where each cell contains
                  either 1 (for player X), 2 (for player O), or None (for an empty cell).
    :return: True if the game is a draw (i.e., all cells are filled and there is no winner),
             otherwise False.
    """
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


def reset_board():
    """
    This function: resets the Tic-Tac-Toe board to its initial empty state.
    :return: a 2D list representing the Tic-Tac-Toe board with all cells set to None,
             indicating that no moves have been made yet.
    """
    return [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def display_message(message, font, color, max_width, padding=20):
    """
    This function: displays a message on the screen, handling text wrapping if necessary.
    :param message: The text message to be displayed.
    :param font: The font object used to render the text.
    :param color: The color of the text.
    :param max_width: The maximum width of the text area, used to wrap text if it's too wide.
    :param padding: The padding around the text area, default is 20 pixels.
    :return: None
    """
    words = message.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() <= max_width - 2 * padding:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    text_height = font.get_height() * len(lines)
    text_surface = pygame.Surface((max_width, text_height + 2 * padding), pygame.SRCALPHA)
    text_surface.fill(BG_COLOR)

    y_offset = padding
    for line in lines:
        line_surface = font.render(line, True, color)
        line_x = (max_width - line_surface.get_width()) // 2
        text_surface.blit(line_surface, (line_x, y_offset))
        y_offset += font.get_height()

    text_x = (APP_WIDTH - max_width) // 2
    text_y = (APP_HEIGHT - (text_height + 2 * padding)) // 2

    screen.blit(text_surface, (text_x, text_y))
    pygame.display.update()


def clear_screen():
    """
    This function: clears the screen by filling it with the background color.
    :return: None
    """
    screen.fill(BG_COLOR)
    pygame.display.update()


def display_all_roasts():
    """
    This function: displays all roasts in a scrollable view on the screen. The user can scroll through the roasts using the mouse wheel or arrow keys.
    Also provides a 'Back to Menu' button at the bottom of the screen for navigation.
    :return: None
    """
    clear_screen()

    scroll_y = 0
    roast_spacing = 40
    padding = 20
    max_width = APP_WIDTH - 2 * padding

    roast_surfaces = []
    for i, roast in enumerate(roasts):
        roast_text = f"{i + 1}. {roast}"
        roast_lines = []
        words = roast_text.split(' ')
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            test_surface = FONT.render(test_line, True, WHITE)
            if test_surface.get_width() <= max_width:
                current_line = test_line
            else:
                roast_lines.append(current_line)
                current_line = word
        if current_line:
            roast_lines.append(current_line)

        roast_surfaces.append(roast_lines)

    total_roast_height = sum(len(lines) * FONT.get_height() for lines in roast_surfaces) + len(roasts) * roast_spacing
    max_scroll_y = total_roast_height - APP_HEIGHT

    scrolling = True

    button_width = APP_WIDTH // 2
    button_height = APP_HEIGHT // 8
    back_button = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT - button_height - padding, button_width, button_height)

    while scrolling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                scroll_y += event.y * -30
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    scroll_y -= 30
                if event.key == pygame.K_UP:
                    scroll_y += 30
                if event.key == pygame.K_ESCAPE:
                    scrolling = False
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    scrolling = False
                    return

        scroll_y = max(min(0, scroll_y), -max_scroll_y)

        screen.fill(BG_COLOR)
        y_offset = scroll_y + padding
        for roast_lines in roast_surfaces:
            for line in roast_lines:
                line_surface = FONT.render(line, True, WHITE)
                screen.blit(line_surface, (padding, y_offset))
                y_offset += FONT.get_height() + 5
            y_offset += roast_spacing

        pygame.draw.rect(screen, WHITE, back_button)
        back_text = FONT.render('Back to Menu', True, BLACK)
        screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2,
                                back_button.y + back_button.height // 2 - back_text.get_height() // 2))

        pygame.display.update()


def main_menu():
    """
    This function: displays the main menu screen with options to start a game against another player, against the computer, or to exit the game.
    If the player has achieved 20 consecutive draws, a 'Secret' button is also displayed.
    Handles user input to navigate to the selected game mode or exit the game.
    If the 'Secret' button is pressed, it opens the screen to display all roasts.
    :return: str - Returns 'player' if the user selects 'VS Player', 'computer' if the user selects 'VS Computer', or exits the game if the 'Exit' button is clicked.
    """
    clear_screen()

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

    if consecutive_draws >= 20:
        secret_button = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3 + 3 * (button_height + spacing), button_width,
                                    button_height)
        pygame.draw.rect(screen, WHITE, secret_button)
        secret_text = FONT.render('Secret', True, BLACK)
        screen.blit(secret_text, (secret_button.x + secret_button.width // 2 - secret_text.get_width() // 2,
                                  secret_button.y + secret_button.height // 2 - secret_text.get_height() // 2))

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
                # Check secret button click
                if consecutive_draws >= 20 and secret_button.collidepoint(event.pos):
                    clear_screen()
                    display_all_roasts()


def display_secret_unlocked():
    """
    This function: displays a message indicating that the secret has been unlocked.
    The message is "Secret Unlocked In Main Menu" with alternating colors for each letter (RED and BLUE).
    The message is centered on the screen.
    :return: None
    """
    message = "Secret Unlocked In Main Menu"
    color_pattern = [RED, BLUE]
    max_width = APP_WIDTH - 40
    padding = 20

    letter_surfaces = []
    for i, letter in enumerate(message):
        letter_surface = FONT.render(letter, True, color_pattern[i % 2])
        letter_surfaces.append(letter_surface)

    total_width = sum([surf.get_width() for surf in letter_surfaces])

    x_offset = (APP_WIDTH - total_width) // 2
    y_offset = (APP_HEIGHT - FONT.get_height()) // 2

    for letter_surface in letter_surfaces:
        screen.blit(letter_surface, (x_offset, y_offset))
        x_offset += letter_surface.get_width()

    pygame.display.update()


def game_over_screen(winner, is_computer_win=False):
    """
    This function: displays the game over screen with the result of the game.
    The screen shows a message based on the game's outcome:
    - If the game is a draw, it either displays "It's a draw!" or "Secret Unlocked In Main Menu" if 20 consecutive draws have been reached.
    - If the game is won, it shows which player won or a roast message if the computer won.
    The screen also includes buttons for 'Play Again' and 'Main Menu'.
    :param winner: A string indicating the result of the game. It can be 'draw', 'X', or 'O'.
    :param is_computer_win: A boolean indicating whether the computer won the game. Default is False.
    :return: A string indicating the user's choice after the game over screen. Can be 'play_again' or 'main_menu'.
    """
    clear_screen()

    if winner == 'draw':
        if consecutive_draws >= 20:
            display_secret_unlocked()
        else:
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
    """
    This function: implements the Minimax algorithm to evaluate the best move for the current player.
    The function recursively simulates all possible moves to determine the optimal move based on the current board state.
    :param board: A 2D list representing the current state of the Tic-Tac-Toe board.
                  Each element is None for an empty cell, 1 for Player X, or 2 for Player O.
    :param depth: The current depth in the game tree. Depth increases with each recursive call.
    :param is_maximizing: A boolean indicating whether the current player is maximizing (True for Player O, False for Player X).
    :return: An integer score representing the outcome of the board state:
             - 10 if Player O (the maximizing player) wins
             - -10 if Player X (the minimizing player) wins
             - 0 if the game is a draw
    """
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
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] is None:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    """
    This function: determines the best move for the computer player (Player O) by evaluating all possible moves
    and selecting the move with the highest score using the Minimax algorithm.
    :param board: A 2D list representing the current state of the Tic-Tac-Toe board.
                  Each element is None for an empty cell, 1 for Player X, or 2 for Player O.
     :return: A tuple (row, col) representing the best move for Player O.
             If there are multiple moves with the same score, the function returns the first one encountered.
    """
    best_move = None
    best_score = -float('inf')
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def computer_move(board):
    """
    This function: calculates the best move for the computer player (Player O) using the `find_best_move` function.
    This move is determined based on the current state of the Tic-Tac-Toe board, aiming to maximize the
    computer's chances of winning.
    :param board: A 2D list representing the current state of the Tic-Tac-Toe board.
                  Each element is None for an empty cell, 1 for Player X, or 2 for Player O.
    :return: A tuple (row, col) representing the best move for Player O as determined by the `find_best_move` function.
    """
    return find_best_move(board)


def main():
    """
    The main game loop for the Tic-Tac-Toe game. Handles the game flow, including:
    - Displaying the main menu and handling user input to start a game or exit.
    - Managing the game state and player turns.
    - Handling game events, including player moves and computer moves if playing against the computer.
    - Checking for win conditions or draws and displaying the appropriate game over screens.
    - Allowing the player to either play again or return to the main menu after a game ends.

    This function:
    - Initializes the game mode and board state.
    - Calls helper functions to draw the board and figures.
    - Manages player turns and updates the board based on user or computer moves.
    - Checks win or draw conditions and updates the game state accordingly.
    - Handles the transition between different game states and menus.
    :return: None
    """
    mode = None
    global consecutive_draws

    while True:
        if mode is None:
            mode = main_menu()

        board = reset_board()
        clear_screen()
        draw_lines()
        pygame.display.update()

        game_over = False
        current_player = 1
        winner = None

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    if OFFSET_X <= mouseX <= OFFSET_X + GAME_WIDTH and OFFSET_Y <= mouseY <= OFFSET_Y + GAME_HEIGHT:
                        clicked_row = (mouseY - OFFSET_Y) // SQUARE_SIZE
                        clicked_col = (mouseX - OFFSET_X) // SQUARE_SIZE

                        if board[clicked_row][clicked_col] is None:
                            board[clicked_row][clicked_col] = current_player
                            draw_figures(board)

                            if check_win(board, current_player):
                                game_over = True
                                winner = 'X' if current_player == 1 else 'O'
                                is_computer_win = (mode == 'computer' and winner == 'O')
                                choice = game_over_screen(winner, is_computer_win=is_computer_win)
                                consecutive_draws = 0

                            elif check_draw(board):
                                game_over = True
                                winner = 'draw'
                                consecutive_draws += 1
                                choice = game_over_screen(winner)

                            current_player = current_player % 2 + 1

            if mode == 'computer' and current_player == 2 and not game_over:
                row, col = computer_move(board)
                board[row][col] = current_player
                draw_figures(board)

                if check_win(board, current_player):
                    game_over = True
                    winner = 'O'
                    choice = game_over_screen(winner, is_computer_win=True)
                    consecutive_draws = 0

                elif check_draw(board):
                    game_over = True
                    winner = 'draw'
                    consecutive_draws += 1
                    choice = game_over_screen(winner)

                current_player = current_player % 2 + 1

            pygame.display.update()

        if choice == 'play_again':
            board = reset_board()
            game_over = False
            current_player = 1
            winner = None
            clear_screen()
            draw_lines()
            pygame.display.update()
            pygame.event.clear()
            pygame.time.wait(100)

        elif choice == 'main_menu':
            mode = None
            clear_screen()
            pygame.display.update()
            pygame.time.wait(100)


if __name__ == "__main__":
    main()
