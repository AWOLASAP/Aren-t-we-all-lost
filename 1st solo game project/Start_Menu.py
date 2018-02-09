import pygame

from MainSettings import Settings


class GameLogo():

	def __init__(self):
		self.main_settings = Settings()
		self.screen = self.main_settings.screen
		
		self.image = pygame.image.load('Images/Game_Logo.bmp')
		
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.center = (500, 200)

	def blitme(self):
		self.screen.blit(self.image, self.rect)