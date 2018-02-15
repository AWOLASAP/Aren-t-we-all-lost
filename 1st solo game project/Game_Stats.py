class GameStats():
	"""Tracks the statistics for Alien Invasion"""

	def __init__(self, main_settings):
		"""Initialize statistics."""
		self.main_settings = main_settings

		#Set game stat to intro
		self.game_level = 0