from constants import *
import pygame
import sys
import tkinter as tk
from tkinter import messagebox

def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

def draw_button(screen, surface, rect, color, text, font_size=50, color_text=BLACK):
    try:
        if not (isinstance(screen, pygame.Surface) and isinstance(surface, pygame.Surface)):
            raise TypeError("Invalid screen or button surface provided.")

        if not (isinstance(rect, pygame.Rect) and isinstance(color, tuple)):
            raise TypeError("Invalid button rectangle or color provided.")
        surface.fill(color)
        screen.blit(surface, rect)
        font = pygame.font.Font('pixel_font.ttf', font_size)
        text_surface = font.render(text, True, color_text)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
    except Exception as e:
        showError(f"Error in with drawing the button: {e}")

def showError(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()

def show_start_screen(screen, font):
    background_image = pygame.image.load('background_image_1.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True
    show_image = False
    while running:
        screen.blit(background_image, (0, 0))

        start_button_surface = pygame.Surface((250, 70))
        start_button_rect = start_button_surface.get_rect(center=(400, 225))
        exit_button_surface = pygame.Surface((200, 70))
        exit_button_rect = exit_button_surface.get_rect(center=(400, 325))
        keyshorts_button_surface = pygame.Surface((450, 70))
        keyshorts_button_rect = keyshorts_button_surface.get_rect(center=(400, 425))

        start_button_color = (134,243,32,255)
        exit_button_color = (236,17,48,255)
        keyshorts_button_color = (254,137,47,255)

        font = pygame.font.Font('pixel_font.ttf', 75)
        main_text = font.render("Game of Life", True, BLACK)
        main_text_rect = main_text.get_rect(center=(400, 100))
        screen.blit(main_text, main_text_rect)

        draw_button(screen, start_button_surface, start_button_rect, start_button_color, "Start", color_text=BLACK)
        draw_button(screen, keyshorts_button_surface, keyshorts_button_rect, keyshorts_button_color, "Key Commands", font_size=40, color_text=BLACK)
        draw_button(screen, exit_button_surface, exit_button_rect, exit_button_color, "Exit", color_text=BLACK)

        key_shorts_table = pygame.image.load('key_commands.png')
        key_shorts_table = pygame.transform.scale(key_shorts_table, (WINDOW_WIDTH, WINDOW_HEIGHT))
        key_shorts_table_rect = key_shorts_table.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return 'start'
                if exit_button_rect.collidepoint(event.pos):
                    return 'exit'
                if keyshorts_button_rect.collidepoint(event.pos) and not show_image:
                    show_image = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = True
                    show_image = False
                
        if show_image:
            screen.blit(key_shorts_table, key_shorts_table_rect)

        pygame.display.update()

def show_middle_screen(screen, font):
    background_image = pygame.image.load('background_image_1.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True
    in_start_screen = False
    while running:
        screen.blit(background_image, (0, 0))

        normal_rules_button_surface = pygame.Surface((535, 70))
        normal_rules_button_rect = normal_rules_button_surface.get_rect(center=(400, 225))
        custom_rules_button_surface = pygame.Surface((525, 70))
        custom_rules_button_rect = custom_rules_button_surface.get_rect(center=(400, 325))
        back_button_surface = pygame.Surface((225, 70))
        back_button_rect = back_button_surface.get_rect(center=(400, 425))

        normal_rules_button_color = (134,243,32,255)
        custom_rules_button_color = (254,137,47,255)
        back_button_color = (236,17,48,255)

        draw_button(screen, normal_rules_button_surface, normal_rules_button_rect, normal_rules_button_color, "Normal Rules", color_text=BLACK)
        draw_button(screen, custom_rules_button_surface, custom_rules_button_rect, custom_rules_button_color, "Custom Rules", color_text=BLACK)
        draw_button(screen, back_button_surface, back_button_rect, back_button_color, "Back", color_text=BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if normal_rules_button_rect.collidepoint(event.pos):
                    return 'normal_rules'
                if custom_rules_button_rect.collidepoint(event.pos):
                    return 'custom_rules'
                if back_button_rect.collidepoint(event.pos) and not in_start_screen:
                    return 'back'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'back'

        pygame.display.update()

def input_box(screen, font):

    def is_valid_rule(rule):
        return all(char.isdigit() and char != '9' for char in rule) and len(set(rule)) == len(rule)
    
    background_image = pygame.image.load('background_image_1.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True

    survival_text = ''
    birth_text = ''

    back_button_color = (236,17,48,255)
    survival_color = (254,137,47,255)
    birth_color = (254,137,47,255)
    submit_color = (134,243,32,255)

    active_box = None

    while running:
        screen.blit(background_image, (0, 0))

        survival_text_surface = pygame.Surface((475, 60))
        survival_text_rect = survival_text_surface.get_rect(center=(400, 75))
        survival_box_surface = pygame.Surface((INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT))
        survival_box_rect = survival_box_surface.get_rect(center=(400, 150))
        birth_text_surface = pygame.Surface((350, 60))
        birth_text_rect = birth_text_surface.get_rect(center=(400, 250))
        birth_box_surface = pygame.Surface((INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT))
        birth_box_rect = birth_box_surface.get_rect(center=(400, 325))
        submit_surface = pygame.Surface((300, 70))
        submit_rect = submit_surface.get_rect(center=(400, 425))
        back_button_surface = pygame.Surface((225, 70))
        back_button_rect = back_button_surface.get_rect(center=(400, 525))

        draw_button(screen, survival_text_surface, survival_text_rect, survival_color, 'Survival Rules', font_size=40, color_text=BLACK)
        draw_button(screen, survival_box_surface, survival_box_rect, survival_color, survival_text, color_text=BLACK)
        draw_button(screen, birth_text_surface, birth_text_rect, birth_color, 'Birth Rules', font_size=40, color_text=BLACK)
        draw_button(screen, birth_box_surface, birth_box_rect, birth_color, birth_text, color_text=BLACK)
        draw_button(screen, back_button_surface, back_button_rect, back_button_color, "Back", color_text=BLACK)
        draw_button(screen, submit_surface, submit_rect, submit_color, 'Submit', color_text=BLACK)

        pygame.draw.rect(screen, BLACK, survival_box_rect, 8)
        pygame.draw.rect(screen, BLACK, birth_box_rect, 8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if survival_box_rect.collidepoint(event.pos):
                    active_box = 'survival'
                elif birth_box_rect.collidepoint(event.pos):
                    active_box = 'birth'
                elif submit_rect.collidepoint(event.pos):
                    valid_survival = is_valid_rule(survival_text)
                    valid_birth = is_valid_rule(birth_text)
                    if valid_survival and valid_birth:
                        survival_list = [int(char) for char in survival_text if char.isdigit()]
                        birth_list = [int(char) for char in birth_text if char.isdigit()]
                        return ('custom_game', survival_list, birth_list)
                    else:
                        showError("Invalid rules. Please enter a valid set of digits (0-8).")
                elif back_button_rect.collidepoint(event.pos):
                    return ("back", [2, 3], [3])
                else:
                    active_box = None
            elif event.type == pygame.KEYDOWN:
                if active_box == 'survival':
                    if event.key == pygame.K_BACKSPACE:
                        survival_text = survival_text[:-1]
                    elif event.unicode.isdigit() and len(survival_text) < 8:
                        survival_text += event.unicode
                    elif event.unicode.isdigit() and len(survival_text) >= 8:
                        pass
                    elif event.key == pygame.K_ESCAPE:
                        return ("back", [2, 3], [3])
                elif active_box == 'birth':
                    if event.key == pygame.K_BACKSPACE:
                        birth_text = birth_text[:-1]
                    elif event.unicode.isdigit() and len(birth_text) < 8:
                        birth_text += event.unicode
                    elif event.unicode.isdigit() and len(birth_text) >= 8:
                        pass
                    elif event.key == pygame.K_ESCAPE:
                        return ("back", [2, 3], [3])
                elif event.key == pygame.K_ESCAPE:
                    return ("back", [2, 3], [3])


        pygame.display.flip()

    pygame.quit()