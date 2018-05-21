import pygame
pygame.init()
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
from level_goal import LevelGoal
from colors import Colors
from torch import Torch
from blind_affect import blind_affect


main_settings = Settings()
GameStats = GameStats()
StoryLine = StoryLine()
StoryDisplay = StoryDisplay(main_settings)
GameLogo = GameLogo()
PlayButton = PlayButton()
Credits = Credits()
player = Player(100, 100)
levelgoal = LevelGoal(900, 615)
color = Colors()
torch = Torch()
blind_affect = blind_affect()

clock = pygame.time.Clock()

norm_font = pygame.font.SysFont(None, 64)
large_font = pygame.font.SysFont(None, 128)

sprite_list = pygame.sprite.Group()
sprite_list.add(levelgoal)
sprite_list.add(player)


def update_game():

	GameStats.current_level = GameStats.levels[GameStats.game_level]
	player.level = GameStats.current_level

	main_settings.screen.fill(main_settings.bg_color)

	check_events()

	if GameStats.start_menu:
		if not pygame.mixer.Channel(1).get_busy():
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("Music/Intro_Song.wav"))
		show_start_menu()
		
		
	elif GameStats.game_level == 0:
		play_level_one()
		pygame.mixer.Channel(1).stop()
		
	elif GameStats.game_level == 1:
		play_level_two()

	elif GameStats.game_level == 2:
		play_level_three()

	elif GameStats.game_level == 3:
		play_level_four()
	
	elif GameStats.game_level == 4:
		play_level_five()
	
	elif GameStats.game_level == 5:
		play_level_six()

	elif GameStats.game_level == 6:
		play_level_seven()


	#Set the game to run at 60fps
	clock.tick(100)
	
	
def get_fps():
	fps = int(clock.get_fps())
	return fps

def check_KEYDOWN_events(event):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_s:
		advance_level()
	elif event.key == pygame.K_b:
		degrade_level()
	elif event.key == pygame.K_RIGHT:
		player.go_right()
	elif event.key == pygame.K_LEFT:
		player.go_left() 
	elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
		if player.crouching:
			player.stand()
		else:
			player.jump()
	elif event.key == pygame.K_z:
		player.pick_up_item(torch)
	elif event.key == pygame.K_DOWN:
		player.crouch()
	elif event.key == pygame.K_f:
		open_fullscreen()
	elif event.key == pygame.K_c:
		close_fullscreen()
	elif event.key == pygame.K_m:
		make_screen_movable()
	elif event.key == pygame.K_n:
		make_screen_not_movable()
	elif event.key == pygame.K_h:
		pygame.display.iconify()

def check_KEYUP_events(event):
	if event.key == pygame.K_LEFT and player.change_x < 0:
		player.stop()
	elif event.key == pygame.K_RIGHT and player.change_x > 0:
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

	if play_button_clicked and GameStats.start_menu:
		play_intro_to_char()
		GameStats.start_menu = False

def open_fullscreen():
	pygame.display.set_mode(
			(main_settings.screen_width, main_settings.screen_height), 
			pygame.NOFRAME | pygame.DOUBLEBUF | pygame.FULLSCREEN
			)
	pygame.display.update()
		
def close_fullscreen():
	pygame.display.set_mode(
			(main_settings.screen_width, main_settings.screen_height), 
			pygame.NOFRAME | pygame.DOUBLEBUF
			)
	pygame.display.update()

def make_screen_movable():
	pygame.display.set_mode(
			(main_settings.screen_width, main_settings.screen_height), 
			pygame.DOUBLEBUF
			)
	pygame.display.update()

def make_screen_not_movable():
	pygame.display.set_mode(
			(main_settings.screen_width, main_settings.screen_height), 
			pygame.NOFRAME | pygame.DOUBLEBUF
			)
	pygame.display.update()

def play_head_hit():
	pygame.mixer.Channel(7).play(pygame.mixer.Sound("Sounds/Head_Bump.wav"))

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
			main_settings.screen.blit(surf2, (text_location_x + uniform(-1, 1), text_location_y + uniform(-1, 1)))
		else:
			main_settings.screen.blit(surf2, (text_location_x, text_location_y))

		pygame.display.flip()
		clock.tick(100)

		check_events()

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

		check_events()

def print_by_letter(text_str, text_location, font_type):
	'''Print a str letter by letter on the screen'''
	text = ''
	font = font_type
	new_surf = pygame.surface.Surface((main_settings.screen_width, main_settings.screen_height))
	for i in range(len(text_str)):
		new_surf.fill(main_settings.bg_color)
		text += text_str[i]
		text_surface = font.render(text, True, color.WHITE)
		text_rect = text_surface.get_rect()
		text_rect.center = text_location
		new_surf.blit(text_surface, text_location)
		main_settings.screen.blit(new_surf, (0, 0))
		pygame.display.update()
		pygame.time.wait(20)
		check_events()

def set_bg_color(color):

	main_settings.bg_color = color

def fill_main_screen():
	
	main_settings.screen.fill(main_settings.bg_color)

def check_goal():
	hit_goal = pygame.sprite.collide_rect(player, levelgoal)
	if hit_goal:
		advance_level()

def spawn_sprites():
	player.spawn(GameStats.game_level)
	levelgoal.spawn(GameStats.game_level)

def advance_level():
	if GameStats.game_level < (len(GameStats.levels) - 1):
		GameStats.game_level += 1
		if GameStats.start_menu:
			GameStats.start_menu = False
			GameStats.game_level = 0
		GameStats.current_level = GameStats.levels[GameStats.game_level]
		spawn_sprites()
		if GameStats.game_level == 0:
			GameStats.first_level1 = True
		elif GameStats.game_level == 1:
			GameStats.first_level2 = True
		elif GameStats.game_level == 2:
			GameStats.first_level3 = True
		pygame.display.flip()

def degrade_level():
	GameStats.game_level -= 1
	if GameStats.game_level == -1:
		set_bg_color(color.BLACK)
		GameStats.first_start_menu = True
		GameStats.start_menu = True

	if GameStats.game_level < 0:
		GameStats.game_level = 0

	if GameStats.game_level == 0:
		GameStats.first_level1 = True
	elif GameStats.game_level == 1:
		GameStats.first_level2 = True
	elif GameStats.game_level == 2:
		GameStats.first_level3 = True
	
	GameStats.current_level = GameStats.levels[GameStats.game_level]
	spawn_sprites()
	pygame.display.flip

def update_level():
	check_events()
	check_goal()
	player.update()
	torch.update(player)
	GameStats.current_level.wall_list.draw(main_settings.screen)

	sprite_list.draw(main_settings.screen)

	if GameStats.game_level == 5:
		blind_affect.update(player)

	if GameStats.game_level == 6:
		main_settings.screen.blit(torch.image, torch.rect)
		blind_affect.update(player, torch)
		player.pick_up_item(torch)

	#Try to blit the level's text to the screen
	try:
		main_settings.screen.blit(GameStats.current_level.lvl_text_image, GameStats.current_level.text_location)
	#Allow if there is no text
	except TypeError:
		pass
		
	pygame.display.flip()

def show_start_menu():
	set_bg_color(color.BLACK)
	if GameStats.first_start_menu:
		fade_image(GameLogo.image, 0, 3, -33, 90, False)
		fade_image(PlayButton.image, 0, 3, 387, 317, False,)
		GameStats.first_start_menu = False
	Credits.blitme()
	GameLogo.blitme()
	PlayButton.blitme()
	while GameStats.start_menu:
		check_events()

def play_intro_to_char():
	set_bg_color(color.BLACK)
	fill_main_screen()
	GameStats.game_level = 0
	spawn_sprites()
	print_by_letter(StoryLine.intro_to_charTEXT1, StoryDisplay.intro_location1, norm_font)
	sleep(1.5)
	print_by_letter(StoryLine.intro_to_charTEXT2, StoryDisplay.intro_location2, norm_font)
	sleep(1.5)
	main_settings.screen.fill(main_settings.bg_color)
	fade_text(StoryLine.intro_to_charTEXT3, 0, 2, 325, 300, large_font, False)
	sleep(0.5)
	fade_text(StoryLine.intro_to_charTEXT3, 1, 2, 325, 300, large_font, True)
	GameStats.first_level1 = True

def play_level_one():
	set_bg_color(color.FADEDGRAY)
	fill_main_screen()
	update_level()

def play_level_two():
	set_bg_color(color.FADEDGRAY)
	fill_main_screen()
	update_level()

def play_level_three():
	set_bg_color(color.GLOOMYGRAY)
	fill_main_screen()
	update_level()

def play_level_four():
	set_bg_color(color.DARKGRAY)
	fill_main_screen()
	update_level()

def play_level_five():
	set_bg_color(color.DARKGRAY)
	fill_main_screen()
	update_level()

def play_level_six():
	set_bg_color(color.BLACK)
	fill_main_screen()
	update_level()

def play_level_seven():
	if GameStats.first_level7:
		torch.spawn(GameStats.game_level)
		GameStats.first_level7 == False
	set_bg_color(color.BLACK)
	fill_main_screen()
	update_level()
