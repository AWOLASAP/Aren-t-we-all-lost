import pygame

class Settings():

	def __init__(self):
		"""Init the game's settings"""

		#Screen settings
		self.screen_width = 1000
		self.screen_height = 700
		self.bg_color = (0, 0, 0)
		self.screen = pygame.display.set_mode(
			(self.screen_width, self.screen_height))

		self.first_start_menu = True