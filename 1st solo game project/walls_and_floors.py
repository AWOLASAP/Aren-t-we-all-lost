import pygame
from pygame.sprite import Sprite

from MainSettings import Settings 


class Wall(Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height, color):

        # Call the parent's constructor
        super().__init__()

        # Make a 'color' wall, of the size specified in the parameters
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class floor(Sprite):

    def __init__(self, x, y, width, height, color):
        """Constructor for the floor that the player can stand on and jump off."""
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x