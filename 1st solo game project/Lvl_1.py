import pygame 

from MainSettings import Settings 


class lvl1Assets():

	def __init__(self):
		self.main_settings = Settings()
		self.screen = self.main_settings.screen

		self.small_platform = pygame.image.load('Level_Assets/LevelPlatformSmall.bmp')
		self.medium_platform = pygame.image.load('Level_Assets/LevelPlatformMedium.bmp')
		self.large_platform = pygame.image.load('Level_Assets/LevelPlatformLArge.bmp')

		self.s_platform_rect = self.small_platform.get_rect()
		self.m_platform_rect = self.medium_platform.get_rect()
		self.l_platform_rect = self.large_platform.get_rect()

	def blitsmallplatform(self, location):
		self.screen.blit(self.small_platform, location)

	def blitmediumplatform(self, location):
		self.screen.blit(self.medium_platform, location)

	def blitlargeplatform(self, location):
		self.screen.blit(self.large_platform, location)