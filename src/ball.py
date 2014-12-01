import pygame
from math import sin,cos
import os

dir = os.path.dirname(__file__)

class Ball(pygame.sprite.Sprite):
    """Ball class"""

    def __init__(self, position, *groups):
        super(Ball, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join(dir, '../sprites/ball.png'))
        self.hit = pygame.mixer.Sound(os.path.join(dir, '../sounds/Hit_Hurt.wav'))
        self.dim = self.image.get_size()
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        #to add variable speed and rotation and angle
        self.top_speed = {'x': 500, 'y': 500}
        self.speed = {'x': 500, 'y': 500}
        self.attached_to = {'sprite': None, 'side': None, 'relative_position': None, 'move': None}
        self.position = {'x': position[0], 'y': position[1]}

    def attach(self, sprite, side):
        """Attach the ball to an object

        sprite -- the Sprite object
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

        temp_position = self.position.copy()

        #compute which block does the ball hit first by rewind the ball movement one step at the time
        #Attention!!! You also have to compute what side it hits first!!
        
        cell = pygame.sprite.spritecollide(self, game.blocks, False)
        _cell = pygame.sprite.spritecollide(self, game.blocks, False)
        while len(_cell) > 1:
            if self.rect.x and self.speed['x']:
                self.rect.x -= (self.speed['x']*dt)/abs(self.speed['x']*dt)
            if self.rect.y and self.speed['y']:
                self.rect.y -= (self.speed['y']*dt)/abs(self.speed['y']*dt)
            cell = _cell
            _cell = pygame.sprite.spritecollide(self, game.blocks, False)

        if _cell:
            cell = _cell

        self.position = temp_position.copy()
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']

        if cell:
            _cell = cell[0].rect
            prev_collision_axis = []
            collision_axis = []

            while len(collision_axis) != 1:
                collision_axis = []
                if last.right <= _cell.left and new.right > _cell.left:
                    collision_axis.append('left')
                if last.left >= _cell.right and new.left < _cell.right:
                    collision_axis.append('right')
                if last.bottom <= _cell.top and new.bottom > _cell.top:
                    collision_axis.append('top')
                if last.top >= _cell.bottom and new.top < _cell.bottom:
                    collision_axis.append('bottom')

                if prev_collision_axis:
                    if len(collision_axis) == 0:
                        collision_axis = [prev_collision_axis[0]]
                prev_collision_axis = collision_axis[:]

                if self.speed['x']:
                    new.x -= (self.speed['x']*dt)/abs(self.speed['x']*dt)
                else:
                    new.x = 0
                if self.speed['y']:
                    new.y -= (self.speed['y']*dt)/abs(self.speed['y']*dt)
                else:
                    new.y = 0

            collision_axis = collision_axis[0]
            if collision_axis == 'left':
                new.right = _cell.left
                self.speed['x'] = -self.speed['x']

            elif collision_axis == 'right':
                new.left = _cell.right
                self.speed['x'] = -self.speed['x']

            elif collision_axis == 'top':
                new.bottom = _cell.top
                self.speed['y'] = -self.speed['y']

            elif collision_axis == 'bottom':
                new.top = _cell.bottom
                self.speed['y'] = -self.speed['y']
            cell[0].kill()
            game.score += 1
            self.hit.play()


#        if cell:
#            _cell = cell[0].rect
#
#            if last.right <= _cell.left and new.right > _cell.left:
#                new.right = _cell.left
#                self.speed['x'] = -self.speed['x']
#            elif last.left >= _cell.right and new.left < _cell.right:
#                new.left = _cell.right
#                self.speed['x'] = -self.speed['x']
#
#            if last.bottom <= _cell.top and new.bottom > _cell.top:
#                new.bottom = _cell.top
#                self.speed['y'] = -self.speed['y']
#            elif last.top >= _cell.bottom and new.top < _cell.bottom:
#                new.top = _cell.bottom
#                self.speed['y'] = -self.speed['y']
#            cell[0].kill()


