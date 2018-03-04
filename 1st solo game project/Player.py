import pygame
from pygame.sprite import Sprite

from MainSettings import Settings

main_settings = Settings()


class Player(Sprite):

	def __init__(self, x, y):
		"""Initialize the player"""

		super().__init__()

		self.main_settings = Settings()
		self.screen = self.main_settings.screen
		self.screen_rect = self.screen.get_rect()

		#Player images
		self.image = pygame.image.load('Images/Player.bmp')
		self.player = pygame.image.load('Images/Player.bmp')
		self.player_right = pygame.image.load('Images/Player_Right.bmp')
		self.player_left = pygame.image.load('Images/Player_Left.bmp')
		self.player_up = pygame.image.load('Images/Player_Up.bmp')
		self.player_down = pygame.image.load('Images/Player_Down.bmp')
		self.player_crouch_right = pygame.image.load('Images/Player_CrouchR.bmp')
		self.player_crouch_left = pygame.image.load('Images/Player_CrouchL.bmp')

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.change_x = 0
		self.change_y = 0

		self.last_x = self.rect.x
		self.last_y = self.rect.y

		self.level = None

		self.crouching = False

	def go_right(self):
		#User hits right arrow
		if self.rect.right < main_settings.screen_width:
			self.change_x = 3
			self.image = self.player_right

	def go_left(self):
		#User hits left arrow
		if self.rect.left > 0:
			self.change_x = -3
			self.image = self.player_left

	def stop(self):
		#User isn't pressing left or right arrow
		self.change_x = 0
		self.image = self.player
				
	def jump(self):
		"""When the user hits the 'jump' button 
			and the player isn't crouching. """

		#Check to see if player is on a platform by moving a bit down, seeing if player
		#is in a block, then moving back
		self.rect.y += 2
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		self.rect.y -= 2

		#If the player was in a block then the player is on a platform;
		#thus, move the player up
		if (len(block_hit_list) > 0 and not self.crouching) or (self.rect.bottom >= main_settings.screen_height and self.crouching == False):
			self.change_y = -10

	def crouch(self):
		if self.change_x < 0:
			self.image = self.player_crouch_left
		else:
			self.image = self.player_crouch_right

		self.rect = self.image.get_rect()
		self.update_crouch_location()
		self.crouching = True

	def stand(self):
		self.image = self.player
		self.rect = self.image.get_rect()
		self.update_stand_location()
		self.crouching = False

	def calc_grav(self):
		"""Calculate the effect of gravity"""
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35 

		if self.rect.y >= main_settings.screen_height - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = main_settings.screen_height - self.rect.height

	def spawn(self, level):
		#Moves the player to a level spawnpoint
		if level == 0:
			self.rect.center = (100, 625)
		elif level == 1:
			self.rect.center = (100, 600)
		elif level == 2:
			self.rect.center = (900, 600)
		elif level == 3:
			self.rect.center = (50, 100)

	def update_last_location(self):
		self.last_x = self.rect.x
		self.last_y = self.rect.y

	def update_crouch_location(self):
		self.rect.x = self.last_x - 25
		self.rect.y = self.last_y + 50

	def update_stand_location(self):
		self.rect.x = self.last_x + 25
		self.rect.y = self.last_y - 50

	def update(self):
		"""Find a new position for the player 
			and change the image of the player """
		
		if self.crouching:
			if self.change_x < 0:
				self.image = self.player_crouch_left		
			else:
				self.image = self.player_crouch_right

		self.calc_grav()
		
		#Move left/right
		self.rect.x += self.change_x

		#Did this /^\ cause the player to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		for block in block_hit_list:
			#If going right, stop at the left side of the wall
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				#Otherwise, we are moving left so stop at the right side
				self.rect.left = block.rect.right

		#Move up and down
		if (self.change_y + self.rect.top) < 0:
			self.change_y = -1 * self.rect.top

		#See if the player will go off the screen
		if (self.rect.right) > (self.main_settings.screen_width):
			self.rect.right = self.main_settings.screen_width
		elif (self.rect.left) < 0:
			self.rect.left = 0

		self.rect.y += self.change_y
		
		#Did this /^\ cause the player to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
		for block in block_hit_list:
			#Reset position based on the top and bottom of hit object
			if self.change_y < 0:
				self.rect.top = block.rect.bottom
			else:
				self.rect.bottom = block.rect.top

			#Stop our vetical movement
			self.change_y = 0

			if self.change_x == 0 and not self.crouching:
				self.image = self.player

		
		if (self.change_y > 1 and self.change_x == 0) and (not self.crouching):
			self.image = self.player_down
		elif (self.change_y < 0 and self.change_x == 0) and (not self.crouching):
			self.image = self.player_up

		self.update_last_location()