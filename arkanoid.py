import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

class Racket(pygame.sprite.Sprite):
    """Racket class"""

    def __init__(self, *groups):
        """Constructor of the Racket class. 
        Nothing fancy here it is just a regular sprite
        class
        """
        super(Racket, self).__init__(*groups)
        #This will not be a wall but it is easy to use for now
        self.image = pygame.image.load('wall.png')
        #need to change the way the positions are calculated
        #it should be more generic
        self.image = pygame.transform.scale(self.image,(80,20))
        self.rect = pygame.rect.Rect((40,440), self.image.get_size())

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

class Game(object):
    """Main game"""

    def __init__(self, bg_color = WHITE):
        self.bg_color = bg_color

    def main(self, screen):
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.ball = Ball(sprites)
        self.player = Racket(self.players)
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('wall.png')
        block_size = block.get_size()
        hori_block = pygame.transform.scale(block, (640, block_size[1]))
        vert_block = pygame.transform.scale(block, (block_size[0], 480))

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_block
        wall.rect = pygame.rect.Rect((0,0), hori_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_block
        wall.rect = pygame.rect.Rect((0,0), vert_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_block
        wall.rect = pygame.rect.Rect((0,470), hori_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_block
        wall.rect = pygame.rect.Rect((630,0), vert_block.get_size())

        sprites.add(self.walls)
        sprites.add(self.players)
        while True:
            dt = clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            sprites.update(dt/1000., self)
            screen.fill((200, 200, 200))
            sprites.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)
