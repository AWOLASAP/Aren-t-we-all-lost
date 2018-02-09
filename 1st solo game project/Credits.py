import pygame

from MainSettings import Settings


class Credits():

	def __init__(self):
		self.main_settings = Settings()
		self.screen = self.main_settings.screen

		self.font = pygame.font.SysFont(None, 18)
		self.credits = "MUSIC: https://www.bensound.com"

		self.rendered_font = self.font.render(self.credits, True, (255, 255, 255))
		self.rf_rect = self.rendered_font.get_rect()
		self.rf_rect.center = (110, 690)

	def blitme(self):
		self.screen.blit(self.rendered_font, self.rf_rect)