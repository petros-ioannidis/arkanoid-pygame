import pygame
from math import sin,cos
import os

dir = os.path.dirname(__file__)

class Ball(pygame.sprite.Sprite):
    """Ball class"""

    def __init__(self, position, *groups):
        """Constructor of the Ball class. 
        Nothing fancy here it is just a regular sprite
        class
        """
        super(Ball, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join(dir, '../sprites/ball.png'))
        self.dim = self.image.get_size()
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        #to add variable speed and rotation and angle
        self.top_speed = {'x': 400, 'y': 400}
        self.speed = {'x': 400, 'y': 400}
        self.attached_to = {'sprite': None, 'side': None}

    def attach(self, sprite, side):
        """Attach the ball to an object

        sprite -- the object
        side -- which side ('up', 'down', 'left', 'right')
        """
        self.attached_to['sprite'] = sprite
        self.attached_to['side'] = side
        self.speed['x'] = 0
        self.speed['y'] = 0
        if self.attached_to['side'] == 'up':
            self.rect.x = sprite.rect.x + self.dim[0]
            self.rect.y = sprite.rect.y - self.dim[1]
    
    def update(self, dt, game):
        if self.attached_to['sprite']:
            if self.attached_to['side'] == 'up':
                self.rect.x = self.attached_to['sprite'].rect.x + self.dim[0]
                self.rect.y = self.attached_to['sprite'].rect.y - self.dim[1]
            return

        last = self.rect.copy()
        self.rect.x += self.speed['x']*dt 
        self.rect.y += self.speed['y']*dt 

        new = self.rect
        for wall in pygame.sprite.spritecollide(self, game.walls, False):
            wall.calculate_speed(self)

        for racket in pygame.sprite.spritecollide(self, game.players, False):
            racket.calculate_speed(self)

        cell = pygame.sprite.spritecollide(self, game.blocks, True)
        if cell:
            cell = cell[0].rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.speed['x'] = -self.speed['x']
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.speed['x'] = -self.speed['x']

            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
                self.speed['y'] = -self.speed['y']
            elif last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.speed['y'] = -self.speed['y']

