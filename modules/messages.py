import random
import sys
from pythonProject.modules.constants import *
from pythonProject.modules.game_logic import clear_screen
from pythonProject.modules.roasts import roasts
from pythonProject.models.GameState import GameState


def display_message(message, font, color, max_width, padding=20):

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

def display_secret_unlocked():

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

    clear_screen()

    if winner == 'draw':
        if GameState.consecutive_draws >= 5:
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
