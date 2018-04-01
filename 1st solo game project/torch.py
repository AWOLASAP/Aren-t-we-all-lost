import pygame
from pygame.sprite import Sprite

from MainSettings import Settings


class Torch(Sprite):
	
	def __init__(self):
		
		super().__init__()
		
		self.image = pygame.image.load('Images/Torch.png')
		self.rect = self.image.get_rect()
		self.rect.x = -100
		self.rect.y = -100
		
	def spawn(self, level):
		if level == 6:
			self.rect.center = (900, 505)
