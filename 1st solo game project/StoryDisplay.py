import pygame.font

from pygame.sprite import Group
from StoryLine import StoryLine

StoryLine = StoryLine()

class StoryDisplay():
	
	def __init__(self, main_settings):
		"""Initialize the storline's display"""
		self.main_settings = main_settings
		self.screen = main_settings.screen
		self.screen_rect = self.screen.get_rect()
		


		#Intro TEXT settings
		self.intro_location1 = (100, 100)
		self.intro_location2 = (100, 150)
		self.intro_location3 = (100, 200)