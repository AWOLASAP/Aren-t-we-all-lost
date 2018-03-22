import pygame
from pygame.sprite import Sprite

from MainSettings import Settings
from colors import Colors


color = Colors()
main_settings = Settings()
class blind_affect(Sprite):
	
	def __init__(self):
		self.image = pygame.Surface(
		(main_settings.screen_width, main_settings.screen_height)
		)
		self.rect = self.image.get_rect()
		
		self.image.fill(color.BLACK)
		self.sight = pygame.image.load('Images/Sight.bmp')		
		
	def update(self, locations=None):
		self.image.fill(color.NEARBLACK)
		if type(locations) != None:
			for location in locations:
				pygame.draw.circle(main_settings.screen, (255, 255, 255, 0), location, 90)
				print('blinding at: ', location[0], location[1])
				#self.image.blit(self.sight, location, special_flags=pygame.BLEND_RGBA_SUB)
		main_settings.screen.blit(self.image, (0, 0))
				
