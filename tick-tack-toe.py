from pythonProject.modules.draw import draw_lines, draw_figures
from pythonProject.modules.game_logic import check_win, check_draw, reset_board
from pythonProject.modules.menu import main_menu
from pythonProject.modules.messages import *
from pythonProject.modules.computer_logic import computer_move
from pythonProject.modules.roasts_logic import display_all_roasts


def display_scores(score_x, score_o):
    # Define the score display area
    score_text_x = FONT.render(f"Score X: {score_x}", True, WHITE)
    score_text_o = FONT.render(f"Score O: {score_o}", True, WHITE)

    # Position the score text
    screen.blit(score_text_x, (10, 10))
    screen.blit(score_text_o, (APP_WIDTH - score_text_o.get_width() - 10, 10))

    # Update the display with the score
    pygame.display.update()


def handle_game_over_choice(choice):
    if choice == 'play_again':
        return True, None
    elif choice == 'main_menu':
        return False, None

def main():
    score_x = 0
    score_o = 0
    GameState.consecutive_draws = 0

    mode = None  # Start with no specific mode

    while True:
        # Show the main menu if no mode is set
        if mode is None:
            mode = main_menu()

        # Prepare the game for a new round
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
                    mouseX, mouseY = event.pos

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
                                if winner == 'X':
                                    score_x += 1
                                else:
                                    score_o += 1
                                choice = game_over_screen(winner, is_computer_win=is_computer_win)

                            elif check_draw(board):
                                game_over = True
                                winner = 'draw'
                                GameState.consecutive_draws += 1
                                choice = game_over_screen(winner)

                            current_player = 3 - current_player

            if mode == 'computer' and current_player == 2 and not game_over:
                row, col = computer_move(board)
                board[row][col] = current_player
                draw_figures(board)

                if check_win(board, current_player):
                    game_over = True
                    winner = 'O'
                    choice = game_over_screen(winner, is_computer_win=True)
                    GameState.consecutive_draws = 0
                elif check_draw(board):
                    game_over = True
                    winner = 'draw'
                    GameState.consecutive_draws += 1
                    choice = game_over_screen(winner)

                current_player = 1

            if mode == 'player':
                display_scores(score_x, score_o)

            pygame.display.update()

        # Handle game over state
        game_over_response = handle_game_over_choice(choice)

        if game_over_response[0]:
            continue

        # If user chooses to view roasts or exit
        if game_over_response[1] == 'view_roasts':
            result = display_all_roasts()

        elif game_over_response[1] is None:
            mode = main_menu()


if __name__ == "__main__":
    main()
