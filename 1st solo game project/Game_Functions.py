import pygame
import sys 
import time
from time import sleep
from random import *
from pygame.locals import *
from pygame.sprite import Sprite

from MainSettings import Settings
from StoryDisplay import StoryDisplay
from Game_Stats import GameStats 
from StoryLine import StoryLine
from Start_Menu import GameLogo
from Play_Button import PlayButton
from Credits import Credits
from Player import Player
from walls_and_floors import *
from Lvl_1 import Level1

main_settings = Settings()
GameStats = GameStats(main_settings)
StoryLine = StoryLine()
StoryDisplay = StoryDisplay(main_settings)
GameLogo = GameLogo()
PlayButton = PlayButton()
Credits = Credits()
player = Player(100, 100)
clock = pygame.time.Clock()

norm_font = pygame.font.SysFont(None, 64)
large_font = pygame.font.SysFont(None, 128)

sprite_list = pygame.sprite.Group()
sprite_list.add(player)

levels = []
level = Level1()
levels.append(level)
current_level = levels[GameStats.game_level] 
player.level = current_level


def update_game():
    main_settings.screen.fill(main_settings.bg_color)

    if GameStats.game_level == 0:
        show_start_menu()
    elif GameStats.game_level == 1:
        play_level_one()

    clock.tick(60)

    pygame.display.flip()

def check_KEYDOWN_events(event):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_s:
        GameStats.game_level += 1
    elif event.key == pygame.K_b:
        GameStats.game_level -= 1
    elif event.key == pygame.K_RIGHT:
        player.go_right()
    elif event.key == pygame.K_LEFT:
        player.go_left() 
    elif event.key == pygame.K_UP:
        player.jump()

def check_KEYUP_events(event):
    if event.key == pygame.K_LEFT and player.change_x < 0:
        player.stop()
    if event.key == pygame.K_RIGHT and player.change_x > 0:
        player.stop()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y)
        elif event.type == pygame.KEYUP:
            check_KEYUP_events(event)

def check_play_button(mouse_x, mouse_y):
    play_button_clicked = PlayButton.rect.collidepoint(mouse_x, mouse_y)

    if play_button_clicked and GameStats.game_level == 0:
        play_intro_to_char()

def fade_text(text_str, fade_in_or_out, fade_time, text_location_x, text_location_y, font_type, blurr):
        '''Show a str fade in/out'''

        FADE_IN_EASING = lambda x: x  # Linear
        FADE_OUT_EASING = lambda x: x  # Linear

        ST_FADEIN = 0
        ST_FADEOUT = 1
        clock = pygame.time.Clock()

        font = font_type
        rendered_text = font.render(text_str, True, (200, 200, 200))
        text_rect = rendered_text.get_rect()
        text_rect.center = (text_location_x, text_location_y)

        state = fade_in_or_out

        last_state_change = time.time()
        state_time = time.time() - last_state_change

        while 1:
            ## Update the state
            state_time = time.time() - last_state_change

            if state == ST_FADEIN:
                alpha = FADE_IN_EASING(1.0 * state_time / fade_time)
                rt = rendered_text
            elif state == ST_FADEOUT:
                alpha = 1.0 - FADE_OUT_EASING(1.0 * state_time / fade_time)
                rt = rendered_text
            else:
                raise ValueError()

            if state_time > fade_time:
            	break

            surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
            surf2.set_alpha(255 * alpha)

            surf2.fill(main_settings.bg_color)
            surf2.blit(rt, (0, 0))

            if blurr:
                main_settings.screen.blit(surf2, (text_location_x + uniform(-0.5, 0.5), text_location_y + uniform(-0.5, 0.5)))
            else:
                main_settings.screen.blit(surf2, (text_location_x, text_location_y))



            pygame.display.flip()
            clock.tick(100)

def fade_image(image, fade_in_or_out, fade_time, x, y, blurr):
    '''Show an image fade in/out'''

    FADE_IN_EASING = lambda x: x  # Linear
    FADE_OUT_EASING = lambda x: x  # Linear

    ST_FADEIN = 0
    ST_FADEOUT = 1
    clock = pygame.time.Clock()

    image_rect = image.get_rect()
    image_rect.center = (0, 0)

    state = fade_in_or_out

    last_state_change = time.time()
    state_time = time.time() - last_state_change

    while 1:
        ## Update the state
        state_time = time.time() - last_state_change

        if state == ST_FADEIN:
            alpha = FADE_IN_EASING(1.0 * state_time / fade_time)
            
        elif state == ST_FADEOUT:
            alpha = 1.0 - FADE_OUT_EASING(1.0 * state_time / fade_time)
            
        else:
            raise ValueError()

        if state_time > fade_time:
            break

        surf2 = pygame.surface.Surface((image_rect.width, image_rect.height))
        surf2.set_alpha(255 * alpha)

        surf2.fill(main_settings.bg_color)
        surf2.blit(image, (0, 0))

        if blurr:
            main_settings.screen.blit(surf2, (x + uniform(-0.5, 0.5), y + uniform(-0.5, 0.5)))
        else:
            main_settings.screen.blit(surf2, (x, y))



        pygame.display.flip()
        clock.tick(100)

def print_by_letter(text_str, text_location, font_type, extra_image_yn, extra_image):
    '''Print a str letter by letter on the screen'''
    text = ''
    new_surf = pygame.surface.Surface((main_settings.screen_width, main_settings.screen_height))
    font = font_type
    for i in range(len(text_str)):
        new_surf.fill(main_settings.bg_color)
        text += text_str[i]
        text_surface = font.render(text, True, (200, 200, 200))
        text_rect = text_surface.get_rect()
        text_rect.center = text_location
        new_surf.blit(text_surface, text_location)
        main_settings.screen.blit(new_surf, (0, 0))
        pygame.display.update()
        pygame.time.wait(50)

def spawn_player(x, y):
    Player.rect.x = x
    Player.rect.y = y

def show_start_menu():
    if main_settings.first_start_menu:
        fade_image(GameLogo.image, 0, 3, -33, 90, False)
        fade_image(PlayButton.image, 0, 3, 387, 317, False,)
        main_settings.first_start_menu = False

    Credits.blitme()
    GameLogo.blitme()
    PlayButton.blitme()
    while GameStats.game_level == 0:
        check_events()

def play_intro_to_char():
    GameStats.game_level = 1

    print_by_letter(StoryLine.intro_to_charTEXT1, StoryDisplay.intro_location1, norm_font, False, False)
    sleep(1.5)
    print_by_letter(StoryLine.intro_to_charTEXT2, StoryDisplay.intro_location2, norm_font, False, False)
    sleep(1.5)
    main_settings.screen.fill(main_settings.bg_color)
    fade_text(StoryLine.intro_to_charTEXT3, 0, 3, 325, 300, large_font, False)
    sleep(0.5)
    fade_text(StoryLine.intro_to_charTEXT3, 1, 3, 325, 300, large_font, True)

def play_level_one():
    check_events()
    player.move()
    current_level.wall_list.draw(main_settings.screen)
    sprite_list.draw(main_settings.screen)
    
