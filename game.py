import pygame
from racket import Racket
from ball import Ball
from block import Block

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

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
        self.blocks = pygame.sprite.Group()
        wall = pygame.image.load('wall.png')
        wall_size = wall.get_size()
        hori_wall = pygame.transform.scale(wall, (640, wall_size[1]))
        vert_wall = pygame.transform.scale(wall, (wall_size[0], 480))

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_wall
        wall.rect = pygame.rect.Rect((0,0), hori_wall.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_wall
        wall.rect = pygame.rect.Rect((0,0), vert_wall.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_wall
        wall.rect = pygame.rect.Rect((0,470), hori_wall.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_wall
        wall.rect = pygame.rect.Rect((630,0), vert_wall.get_size())

        block = Block((100,100),self.blocks)

        sprites.add(self.walls)
        sprites.add(self.players)
        sprites.add(self.blocks)
        while True:
            dt = clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            sprites.update(dt/1000., self)
            screen.fill((200, 200, 200))
            sprites.draw(screen)
            pygame.display.flip()
