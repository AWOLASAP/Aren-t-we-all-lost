import pygame

from MainSettings import Settings

class Player():

	def __init__(self):
		'''Initialize the main_character'''

		self.main_settings = Settings()
		self.screen = self.main_settings.screen

		self.image = pygame.image.load('Images/Player.bmp')
		self.rect = self.image.get_rect()
		self.rect.center = (100, 100)
		self.screen_rect = self.screen.get_rect()

		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		self.change_x = 0
		self.change_y = 0

		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		self.screen.blit(self.image, (self.centerx, self.centery))

	def move_right(self):
		self.change_x += 3

	def move_left(self):
		self.change_x += -3

	def update(self):
		if self.moving_right or self.move_left:
			self.centerx += self.change_x