import pygame
from math import sin,cos

class Ball(pygame.sprite.Sprite):
    """Ball class"""

    def __init__(self, *groups):
        """Constructor of the Ball class. 
        Nothing fancy here it is just a regular sprite
        class
        """
        super(Ball, self).__init__(*groups)
        self.image = pygame.image.load('ball.png')
        self.rect = pygame.rect.Rect((320,280), self.image.get_size())
        #to add variable speed and rotation and angle
        self.top_speed = {'x': 400, 'y': 400}
        self.speed = {'x': 400, 'y': 400}
    
    def update(self, dt, game):
        last = self.rect.copy()
        self.rect.x += self.speed['x']*dt
        self.rect.y += self.speed['y']*dt

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
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

        for racket in pygame.sprite.spritecollide(self, game.players, False):
            angle = racket.calculate_rotation(self)
            cell = racket.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.speed['x'] = sin(angle)*self.top_speed['x']
                self.speed['y'] = -abs(cos(angle)*self.top_speed['y'])
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.speed['x'] = sin(angle)*self.top_speed['x']
                self.speed['y'] = -abs(cos(angle)*self.top_speed['y'])

            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
                self.speed['x'] = sin(angle)*self.top_speed['x']
                self.speed['y'] = -abs(cos(angle)*self.top_speed['y'])
            elif last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.speed['x'] = sin(angle)*self.top_speed['x']
                self.speed['y'] = -abs(cos(angle)*self.top_speed['y'])

        for cell in pygame.sprite.spritecollide(self, game.blocks, True):
            cell = cell.rect
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
