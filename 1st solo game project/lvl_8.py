import pygame 
from pygame.sprite import Sprite

from MainSettings import Settings
from level import Level
from walls_and_floors import *

main_settings = Settings()

class Level8(Level):
	"""Creates all the walls and floors for the level"""

	def __init__(self):
		
		super().__init__()

		#List of the different walls in the form [x, y, width, height, color]
		walls = [
			[0, 300, 500, 25, self.color.BLACK]
		]

		self.lvl_text = "Get me home"
		self.lvl_text_image = self.font.render(self.lvl_text, True, self.color.LIGHTGRAY)
		self.text_location = (500, 50)

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
