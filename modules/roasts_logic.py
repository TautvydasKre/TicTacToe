import sys
from pythonProject.modules.constants import *
from pythonProject.modules.game_logic import clear_screen
from pythonProject.modules.roasts import roasts

def display_all_roasts():
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

        # Split roast text into lines based on max width
        for word in words:
            test_line = f"{current_line} {word}".strip()
            test_surface = FONT.render(test_line, True, WHITE)
            if test_surface.get_width() <= max_width:
                current_line = test_line
            else:
                if current_line:
                    roast_lines.append(current_line)
                current_line = word
        if current_line:
            roast_lines.append(current_line)

        roast_surfaces.append(roast_lines)

    # Calculate total height of all roasts
    total_roast_height = sum(len(lines) * FONT.get_height() for lines in roast_surfaces) + len(roasts) * roast_spacing
    max_scroll_y = total_roast_height - APP_HEIGHT

    scrolling = True

    # Draw the main menu button at the bottom of the screen
    main_menu_button = pygame.Rect(padding, APP_HEIGHT - 60, max_width, 50)

    while scrolling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'main_menu'
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if main_menu_button.collidepoint(mouseX, mouseY):
                    return 'main_menu'

            # Handle mouse wheel scrolling
            if event.type == pygame.MOUSEWHEEL:
                scroll_y += event.y * 5

        # Scroll up or down based on arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            scroll_y -= 5
        if keys[pygame.K_UP]:
            scroll_y += 5

        # Clamp the scroll position
        scroll_y = max(min(0, scroll_y), -max_scroll_y)

        # Clear the screen and draw content
        screen.fill(BG_COLOR)
        y_offset = scroll_y + padding
        for roast_lines in roast_surfaces:
            for line in roast_lines:
                line_surface = FONT.render(line, True, WHITE)
                screen.blit(line_surface, (padding, y_offset))
                y_offset += FONT.get_height() + 5
            y_offset += roast_spacing

        # Draw the main menu button
        pygame.draw.rect(screen, (0, 128, 255), main_menu_button)
        main_menu_text = FONT.render("Main Menu", True, WHITE)
        text_rect = main_menu_text.get_rect(center=main_menu_button.center)
        screen.blit(main_menu_text, text_rect)

        pygame.display.update()

    return 'main_menu'
