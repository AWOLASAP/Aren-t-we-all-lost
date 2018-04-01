import pygame
from pygame.sprite import Sprite

from MainSettings import Settings
from colors import Colors


color = Colors()
main_settings = Settings()
class blind_affect(Sprite):
	
	def __init__(self):
		self.image = pygame.surface.Surface(
		(main_settings.screen_width, main_settings.screen_height), 
		pygame.SRCALPHA
		)
		self.rect = self.image.get_rect()
		self.image.fill(color.BLACK)
		
		self.sight = pygame.image.load('Images/circle.png')
		self.sight = pygame.transform.scale(self.sight, (250, 250))
		self.sight_rect = self.sight.get_rect()

		
	def update(self, locations=None):
		self.image.fill(color.BLACK)
		if type(locations) != None:
			for location in locations:
				#pygame.draw.circle(self.image, (255, 255, 255, 0), location, 90)
				self.sight_rect.center = location
				self.image.blit(self.sight, self.sight_rect, special_flags=pygame.BLEND_RGBA_SUB)
		main_settings.screen.blit(self.image, (0, 0))
				
