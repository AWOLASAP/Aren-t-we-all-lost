import pygame
from pygame.sprite import Sprite 

from MainSettings import Settings 


class LevelGoal(Sprite):

	def __init__(self, x, y):

		super().__init__()

		self.image = pygame.image.load('Images/Level_Goal.bmp')
		
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def spawn(self, level):
		if level == 0:
			self.rect.center = (900, 615)
		elif level == 1:
			self.rect.center = (900, 465)
		elif level == 2:
			self.rect.center = (100, 165)
		elif level == 3:
			self.rect.center = (900, 615)