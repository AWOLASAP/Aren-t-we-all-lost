import pygame
from pygame.sprite import Sprite

from MainSettings import Settings



class Blind(Sprite):

	def __init__(self):
		self.main_settings = Settings()

		self.image = pygame.image.load('Images/Blind_Small.bmp')
		self.rect = self.image.get_rect()

	def update(self, player):
		self.rect.center = player.rect.center
		self.main_settings.screen.blit(self.image, self.rect)