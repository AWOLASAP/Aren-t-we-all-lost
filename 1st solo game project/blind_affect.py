import pygame
from pygame.sprite import Sprite
from MainSettings import Settings


main_settings = Settings()
class blind_affect(Sprite):
	
	def __init__(self):
		self.image = pygame.Surface(
		(main_settings.screen_width, main_settings.screen_height)
		)
		
