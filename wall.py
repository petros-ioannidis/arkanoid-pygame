from __future__ import division, print_function
import pygame

class Wall(pygame.sprite.Sprite):
    """Basic wall class"""

    def __init__(self, left_top, dimensions, *groups):
        """Constructor for class wall

        left_top -- the left top point of the rectancle
        dimensions -- width, height of the rectancle
        """
        super(Wall, self).__init__(*groups)
        self.left_top = left_top
        self.dimensions = dimensions
        self.image = pygame.image.load('wall.png')
        self.image = pygame.transform.scale(self.image, self.dimensions)
                                            
                                           
        self.rect = pygame.rect.Rect(self.left_top, self.dimensions)
