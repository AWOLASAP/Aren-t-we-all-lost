import pygame


class Level(object):
	"""Super class for levels"""

	#Each room has a list of walls and floors
	wall_list = None
	floor_list = None

	def __init__(self):
		"""Constructor, create our lists"""
		self.wall_list = pygame.sprite.Group()
		self.floor_list = pygame.sprite.Group()