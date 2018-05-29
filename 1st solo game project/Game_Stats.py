import pygame

from Lvl_1 import Level1
from Lvl_2 import Level2
from lvl_3 import Level3
from lvl_4 import Level4
from lvl_5 import Level5
from lvl_6 import Level6
from lvl_7 import Level7
from lvl_8 import Level8



class GameStats():
	"""Tracks the statistics for Alien Invasion"""

	def __init__(self):
		"""Initialize statistics."""

		#Set game state to start
		self.game_level = 0

		self.start_menu = True
		self.first_start_menu = True
		self.first_level1 = True
		self.first_level2 = True
		self.first_level3 = True
		self.first_level4 = True
		self.first_level5 = True
		self.first_level6 = True
		self.first_level7 = True
		self.first_level8 = True
		self.first_level9 = True
		self.first_level10 = True
		

		self.levels = []

		self.level = Level1()
		self.levels.append(self.level)

		self.level = Level2()
		self.levels.append(self.level)
			
		self.level = Level3()
		self.levels.append(self.level)
		
		self.level = Level4()
		self.levels.append(self.level)

		self.level = Level5()
		self.levels.append(self.level)
		
		self.level = Level6()
		self.levels.append(self.level)

		self.level = Level7()
		self.levels.append(self.level)

		self.level = Level8()
		self.levels.append(self.level)
		
		self.current_level = self.levels[self.game_level]