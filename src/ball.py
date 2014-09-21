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
        self.attached_to = {'sprite': None, 'side': None, 'relative_position': None, 'move': None}
        self.position = {'x': position[0], 'y': position[1]}

    def attach(self, sprite, side):
        """Attach the ball to an object

        sprite -- the object
        side -- which side ('up', 'down', 'left', 'right')
        """
        self.attached_to['sprite'] = sprite
        self.attached_to['side'] = side
        self.attached_to['relative_position'] = 0
        self.attached_to['move'] = 0.01
        self.speed['x'] = 0
        self.speed['y'] = 0
        if self.attached_to['side'] == 'up':
            self.position['x'] = sprite.rect.center[0] + self.dim[0]
            self.position['y'] = sprite.rect.center[1] - self.dim[1]
            self.rect.x = sprite.rect.center[0] + self.dim[0]
            self.rect.y = sprite.rect.center[1] - self.dim[1]

    def detach(self):
        """Detach the ball from the current object"""
        self.attached_to['sprite'] = None
        self.attached_to['side'] = None
        self.speed['x'] = 0
        self.speed['y'] = 400
    
    def update(self, dt, game):
        if self.attached_to['sprite']:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.detach()
            if self.attached_to['side'] == 'up':
                self.position['x'] = self.attached_to['sprite'].rect.x + self.dim[0] + self.attached_to['sprite'].dim[0]*self.attached_to['relative_position']
                self.position['y'] = self.attached_to['sprite'].rect.y - self.dim[1]
                self.attached_to['relative_position'] += self.attached_to['move']
                if abs(self.attached_to['relative_position']) >= 0.5:
                    self.attached_to['move'] = -self.attached_to['move']
                self.rect.x = self.position['x']
                self.rect.y = self.position['y']
            return

        last = self.rect.copy()

        #this solves the frozen axis bug

        self.position['x'] += self.speed['x']*dt
        self.position['y'] += self.speed['y']*dt
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']

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

