import pygame 
from pygame.sprite import Sprite

from MainSettings import Settings
from level import Level
from walls_and_floors import *

main_settings = Settings()

class Level5(Level):
	"""Creates all the walls and floors for the level"""

	def __init__(self):
		
		super().__init__()

		#List of the different walls in the form [x, y, width, height, color]
		walls = [
			[0, 675, 1000, 25, self.color.GLOOMYGRAY],
			[400, 0, 200, 625, self.color.GLOOMYGRAY],
			[0, 0, 400, 400, self.color.GLOOMYGRAY], 
			[600, 0, 400, 400, self.color.GLOOMYGRAY]
		]

		self.lvl_text = "I'll fit under that"
		self.lvl_text_image = self.font.render(self.lvl_text, True, self.color.LIGHTGRAY)
		self.text_location = (100, 50)
		
		self.has_blinding = True
		
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
