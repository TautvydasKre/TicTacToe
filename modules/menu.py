import sys
from pythonProject.modules.constants import *
from pythonProject.modules.game_logic import clear_screen
from pythonProject.modules.roasts_logic import display_all_roasts
from pythonProject.models.GameState import GameState

def main_menu():
    clear_screen()
    button_width = APP_WIDTH // 2
    button_height = APP_HEIGHT // 8
    spacing = APP_HEIGHT // 16

    # Define button rectangles
    button1 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3, button_width, button_height)
    button2 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3 + button_height + spacing, button_width, button_height)
    button3 = pygame.Rect(APP_WIDTH // 4, APP_HEIGHT // 3 + 2 * (button_height + spacing), button_width, button_height)

    # Draw buttons
    pygame.draw.rect(screen, WHITE, button1)
    pygame.draw.rect(screen, WHITE, button2)
    pygame.draw.rect(screen, WHITE, button3)

    # Render button texts
    vs_player_text = FONT.render('VS Player', True, BLACK)
    vs_computer_text = FONT.render('VS Computer', True, BLACK)
    exit_text = FONT.render('Exit', True, BLACK)

    # Center the text on buttons
    screen.blit(vs_player_text, (button1.x + button1.width // 2 - vs_player_text.get_width() // 2,
                                   button1.y + button1.height // 2 - vs_player_text.get_height() // 2))
    screen.blit(vs_computer_text, (button2.x + button2.width // 2 - vs_computer_text.get_width() // 2,
                                     button2.y + button2.height // 2 - vs_computer_text.get_height() // 2))
    screen.blit(exit_text, (button3.x + button3.width // 2 - exit_text.get_width() // 2,
                             button3.y + button3.height // 2 - exit_text.get_height() // 2))

    # Check for secret button visibility
    secret_button = None
    if GameState.consecutive_draws >= 5:
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
                    return 'player'
                if button2.collidepoint(event.pos):
                    return 'computer'
                if button3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                # Check secret button click
                if GameState.consecutive_draws >= 5 and secret_button and secret_button.collidepoint(event.pos):
                    clear_screen()
                    result = display_all_roasts()
                    if result == 'main_menu':
                        return 'main_menu'

        pygame.display.update()
