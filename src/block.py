import pygame
import os

dir = os.path.dirname(__file__)

class Block(pygame.sprite.Sprite):
    """Base class for blocks"""
    def __init__(self, position, size, *groups):
        """Constructor for a single block

        position -- a tuple with the position of the block
        groups -- the groups that the block belongs
        """
        super(Block, self).__init__(*groups)
        #this is to be changed to custom blocks
        self.image = pygame.image.load(os.path.join(dir, '../sprites/wall.png'))
        self.image = pygame.transform.scale(self.image, size)
        self.rect = pygame.rect.Rect(position, self.image.get_size()) 

