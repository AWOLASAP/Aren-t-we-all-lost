import pygame
pygame.init()

import sys

import Game_Functions as gf

def run_game():
	#Intit pygame, settings, and screen object
	pygame.display.set_caption("Aren't We All Lost?")

	while True:
		gf.update_game()

run_game()