import pygame

from colors import Colors

class Level(object):
	"""Super class for levels"""

	#Each room has a list of walls and floors
	wall_list = None
	floor_list = None

	lvl_text = ''
	lvl_text_image = None
	text_location = (0, 0)
	font = pygame.font.SysFont(None, 64)

	color = Colors()
	
	
	def __init__(self):
		"""Constructor, create our lists"""
		self.wall_list = pygame.sprite.Group()
		self.floor_list = pygame.sprite.Group()