import pygame 
from pygame.sprite import Sprite

from MainSettings import Settings
from level import Level
from walls_and_floors import *

main_settings = Settings()

class Level4(Level):
	"""Creates all the walls and floors for level1"""

	def __init__(self):
		
		super().__init__()

		#List of the different walls in the form [x, y, width, height, color]
		walls = [
			[0, 675, 1000, 25, self.color.GRAY],
			[0, 150, 200, 25, self.color.GRAY],
			[150, 275, 200, 25, self.color.GRAY],
			[300, 400, 200, 25, self.color.GRAY],
			[450, 525, 200, 25, self.color.GRAY]
		]

		self.lvl_text = "We need to hurry"
		self.lvl_text_image = self.font.render(self.lvl_text, True, (200, 200, 200))
		self.text_location = (600, 50)

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
