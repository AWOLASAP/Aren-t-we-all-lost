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
		
		self.sight = pygame.image.load('Images/circle_01.png')
		self.player_sight = pygame.transform.scale(self.sight, (300, 300))
		self.player_sight_rect = self.player_sight.get_rect()

		self.torch_sight = pygame.transform.scale(self.sight, (750, 750))
		self.torch_sight_rect = self.torch_sight.get_rect()
		
	def update(self, player, torch=None):
		self.image.fill(color.BLACK)
		
		if not torch == None and not torch.in_hand:
			self.player_sight_rect.center = player.rect.center
			self.image.blit(self.player_sight, self.player_sight_rect, special_flags=pygame.BLEND_RGBA_SUB)
		elif torch == None:
			self.player_sight_rect.center = player.rect.center
			self.image.blit(self.player_sight, self.player_sight_rect, special_flags=pygame.BLEND_RGBA_SUB)
			
		try:
			self.torch_sight_rect.center = torch.rect.center
			self.image.blit(self.torch_sight, self.torch_sight_rect, special_flags=pygame.BLEND_RGBA_SUB)
		except AttributeError:
			pass
			
		main_settings.screen.blit(self.image, (0, 0))
				
