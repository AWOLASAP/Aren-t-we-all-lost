import pygame
from pygame.sprite import Sprite

from MainSettings import Settings

main_settings = Settings()

class Player(Sprite):

	def __init__(self, x, y):
		"""Initialize the player"""

		#Call the parents constuctor
		super().__init__()

		self.main_settings = Settings()
		self.screen = self.main_settings.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('Images/Player.bmp')
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.change_x = 0
		self.change_y = 0

		self.level = None

	def go_right(self):
		#User hits right arrow
		self.change_x = 3
		self.image = pygame.image.load('Images/Player_Right.bmp')

	def go_left(self):
		#User hits left arrow
		self.change_x = -3
		self.image = pygame.image.load('Images/Player_Left.bmp')

	def stop(self):
		#User isn't pressing left or right arrow
		self.change_x = 0
		self.image = pygame.image.load('Images/Player.bmp')
				
	def jump(self):
		"""When the user hits the 'jump' button."""

		#Check to see if player is on a platform by moving a bit down, seeing if player
		#is in a block, then moving back
		self.rect.y += 2
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		self.rect.y -= 2

		#If the player was in a block then the player is on a platform;
		#thus, move the player up
		if len(block_hit_list) > 0 or self.rect.bottom >= main_settings.screen_height:
			self.change_y = -10

	def calc_grav(self):
		"""Calculate the effect of gravity"""
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35 

		if self.rect.y >= main_settings.screen_height - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = main_settings.screen_height - self.rect.height

	def move(self):
		"""Find a new position for the player. """
		
		self.calc_grav()
	
		
		#Move left/right
		self.rect.x += self.change_x

		#Did this |^| cause the player to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		for block in block_hit_list:
			#If going right, stop at the left side of the wall
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				#Otherwise, we are moving left so stop at the right side
				self.rect.left = block.rect.right

		#Move up and down
		self.rect.y += self.change_y
		
		#Did this |^| cause the player to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		for block in block_hit_list:
			#Reset position based on the top and bottom of hit object
			if self.change_y < 0:
				self.rect.top = block.rect.bottom
			else:
				self.rect.bottom = block.rect.top

			#Stop our vetical movement
			self.change_y = 0
			if self.change_x == 0:
				self.image = pygame.image.load('Images/Player.bmp')
			
		if self.change_y > 1 and self.change_x == 0:
			self.image = pygame.image.load('Images/Player_Down.bmp')
		elif self.change_y < 0 and self.change_x == 0:
			self.image = pygame.image.load('Images/Player_Up.bmp')
