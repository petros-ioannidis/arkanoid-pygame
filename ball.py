import pygame

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
        self.speed = {'x': 300, 'y': 300}
    
    def update(self, dt, game):
        last = self.rect.copy()
        self.rect.x += self.speed['x']*dt
        self.rect.y += self.speed['y']*dt

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.speed['x'] = -300
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.speed['x'] = 300

            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
                self.speed['y'] = -300
            elif last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.speed['y'] = 300

        for cell in pygame.sprite.spritecollide(self, game.players, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.speed['x'] = -300
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.speed['x'] = 300

            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
                self.speed['y'] = -300
            elif last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.speed['y'] = 300

        for cell in pygame.sprite.spritecollide(self, game.blocks, True):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.speed['x'] = -300
            elif last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.speed['x'] = 300

            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
                self.speed['y'] = -300
            elif last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.speed['y'] = 300

