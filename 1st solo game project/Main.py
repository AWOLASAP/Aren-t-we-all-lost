import pygame 
pygame.init()

import sys

import Game_Functions as gf


def run_game():
	#Intit pygame, settings, and screen object
	pygame.display.set_caption("Aren't We All Lost?")

	while True:
		gf.update_game()
		gf.check_events()

run_game()

#don't worry about this
#https://superiorgamingtech.com/the-ultimate-gaming-pc-build-for-1800-dollars
