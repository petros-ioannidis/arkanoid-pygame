from __future__ import division
from math import cos, sin, pi
import pygame
import os

dir = os.path.dirname(__file__)

class Racket(pygame.sprite.Sprite):
    """Racket class"""

    def __init__(self, position, *groups):
        """Constructor of the Racket class. 
        Nothing fancy here it is just a regular sprite
        class
        """
        super(Racket, self).__init__(*groups)
        #This will not be a wall but it is easy to use for now
        self.image = pygame.image.load(os.path.join(dir, '../sprites/wall.png'))
        #need to change the way the positions are calculated
        #it should be more generic
        self.image = pygame.transform.scale(self.image,(80,20))
        self.position = (int(position[0]), position[1] - self.image.get_size()[1]- 10)
        self.rect = pygame.rect.Rect(self.position, self.image.get_size())
        self.dim = (80, 20)
        self.rotation = dict()
        self.max_angle = pi + pi/2
        #how many pieces has the racket(accuracy for angles)

    def calculate_speed(self, collided_object):
        """Returns the angle that an object will have after colliding
        with the racket

        collided_object -- the object colliding with the racket
        """
        relative_dist = self.rect.center[0] - collided_object.rect.center[0]
        norm_relative_dist = relative_dist/self.rect.center[0]
        angle = -norm_relative_dist*self.max_angle
        collided_object.speed['x'] = sin(angle)*collided_object.top_speed['x']
        collided_object.speed['y'] = -abs(cos(angle)*collided_object.top_speed['y'])

    def update(self, dt, game):
        """The basic movement of the racket"""
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300*dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300*dt

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right


