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

class LeftWall(Wall):
    def __init__(self, left_top, dimensions, *groups):
        """Constructor for horizontal wall

        left_top -- the left top point of the rectancle
        dimensions -- width, height of the rectancle
        """
        super(LeftWall, self).__init__(left_top, dimensions, *groups)

    def calculate_speed(self, collided_object):
        """Change the speed of the object that collides
        with the wall

        collided_object -- the object
        """
        collided_object.speed['x'] = abs(collided_object.speed['x'])

class RightWall(Wall):
    def __init__(self, left_top, dimensions, *groups):
        """Constructor for horizontal wall

        left_top -- the left top point of the rectancle
        dimensions -- width, height of the rectancle
        """
        super(RightWall, self).__init__(left_top, dimensions, *groups)

    def calculate_speed(self, collided_object):
        """Change the speed of the object that collides
        with the wall

        collided_object -- the object
        """
        collided_object.speed['x'] = -abs(collided_object.speed['x'])

class TopWall(Wall):
    def __init__(self, left_top, dimensions, *groups):
        """Constructor for vertical wall

        left_top -- the left top point of the rectancle
        dimensions -- width, height of the rectancle
        """
        super(TopWall, self).__init__(left_top, dimensions, *groups)

    def calculate_speed(self, collided_object):
        """Change the speed of the object that collides
        with the wall

        collided_object -- the object
        """
        collided_object.speed['y'] = abs(collided_object.speed['y'])

class BottomWall(Wall):
    def __init__(self, left_top, dimensions, *groups):
        """Constructor for vertical wall

        left_top -- the left top point of the rectancle
        dimensions -- width, height of the rectancle
        """
        super(BottomWall, self).__init__(left_top, dimensions, *groups)

    def calculate_speed(self, collided_object):
        """Change the speed of the object that collides
        with the wall

        collided_object -- the object
        """
        collided_object.speed['y'] = -abs(collided_object.speed['y'])
