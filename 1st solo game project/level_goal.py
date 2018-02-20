import pygame
from pygame.sprite import Sprite 

class Level_Goal(Sprite):

	def __init__(self):

		self.image = pygame.image.load('Images/Level_Goal.bmp')
		self.rect = self.image.get_rect()

		self.level1_location = (100, 830)
