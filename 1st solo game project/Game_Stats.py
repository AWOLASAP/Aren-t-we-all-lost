import pygame

from Lvl_1 import Level1
from Lvl_2 import Level2
from lvl_3 import Level3
from lvl_4 import Level4


class GameStats():
	"""Tracks the statistics for Alien Invasion"""

	def __init__(self):
		"""Initialize statistics."""

		#Set game state to start
		self.game_level = 0

		self.start_menu = True
		self.first_start_menu = True
		self.first_level1 = False
		self.first_level2 = True
		self.first_level3 = True
		self.first_level4 = True

		self.levels = []
		
		self.level = Level1()
		self.levels.append(self.level)

		self.level = Level2()
		self.levels.append(self.level)
			
		self.level = Level3()
		self.levels.append(self.level)
		
		self.level = Level4()
		self.levels.append(self.level)
		
		self.current_level = self.levels[self.game_level]


