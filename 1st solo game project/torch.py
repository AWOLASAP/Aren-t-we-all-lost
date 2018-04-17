import pygame
from pygame.sprite import Sprite

from MainSettings import Settings


class Torch(Sprite):
	
	def __init__(self):
		
		super().__init__()
		
		self.image = pygame.image.load('Images/Torch.png')
		self.rect = self.image.get_rect()
		self.rect.x = -100
		self.rect.y = -100
		self.in_hand = False
		
	def spawn(self, level):
		if level == 6:
			self.rect.center = (900, 505)
			
	def pick_up(self, player):
		self.in_hand = True
		self.go_to_player_hand(player)
		
	def go_to_player_hand(self, player):
		self.rect.x = player.rect.x + 30
		self.rect.y = player.rect.y + 20
	
	def update(self, player):
		if self.in_hand:
			self.go_to_player_hand(player)
