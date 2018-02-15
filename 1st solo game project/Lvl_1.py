import pygame 
from pygame.sprite import Sprite

from MainSettings import Settings 
from level import Level
from walls_and_floors import *

main_settings = Settings()

class Level1(Level):
	"""Creates all the walls and floors for level1"""

	def __init__(self):
		super().__init__()

		#List of the different walls in the form [x, y, width, height, color]
		walls = [[0, 0, main_settings.screen_width, 50, (255, 255, 0)],
		 [0, 650, main_settings.screen_width, 50, (0, 255, 255)],
		 [0, 0, 50, main_settings.screen_height, (255, 0, 255)],
		 [main_settings.screen_width - 50, 0, 50, main_settings.screen_height, (255, 0, 255)]]

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
