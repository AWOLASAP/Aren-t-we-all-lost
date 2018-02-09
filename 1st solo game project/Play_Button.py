import pygame

from MainSettings import Settings


class PlayButton():

	def __init__(self):
		self.main_settings = Settings()
		self.screen = self.main_settings.screen

		self.image = pygame.image.load('Images/Play_Button.bmp')

		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.center = (500, 400)

	def blitme(self):
		self.screen.blit(self.image, self.rect)
