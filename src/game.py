from __future__ import division
import pygame
import menu
from racket import Racket
from ball import Ball
from block import Block
from wall import LeftWall, RightWall, BottomWall, TopWall 

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

class Game(object):
    """Main game"""

    def __init__(self, dimension, bg_color = WHITE):
        """constructor for the game object

        dimension -- a dictionary with 'x' and 'y' keys with the dimensions of the game screen
        bg_color -- the color of the board (R, G, B)
        """
        self.bg_color = bg_color
        self.dimension = {'x': dimension[0], 'y': dimension[1]}
        self.paused = False

    def main(self, screen):
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.ball = Ball((300, 200), sprites)
        wall_size = (10,10)
        self.player = Racket((self.dimension['x']/2, self.dimension['y'] - wall_size[1]), self.players)
        self.ball.attach(self.player, 'up')
        self.walls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        hori_wall = (self.dimension['x'], wall_size[1])
        vert_wall = (wall_size[0], self.dimension['y'])

        wall_list = zip([
                            (0,0), 
                            (0,0),
                            (0,self.dimension['y'] - 10), 
                            (self.dimension['x'] - 10,0)],\

                            [hori_wall,
                            vert_wall,
                            hori_wall,
                            vert_wall],\

                            [TopWall,
                            LeftWall,
                            BottomWall,
                            RightWall
                        ])

        for _wall in wall_list:
            wall = _wall[2](_wall[0], _wall[1], self.walls)

        #random block position
        for dimx in range(10):
            for dimy in range(6):
                block = Block((100 + dimx*61,100 + dimy*21),self.blocks)

        sprites.add(self.walls)
        sprites.add(self.players)
        sprites.add(self.blocks)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = True
                        menu.PauseMenu().handle_input(screen, self)
                        dt = clock.tick(120)
            dt = clock.tick(120)
            sprites.update(dt/1000., self)
            screen.fill((200, 200, 200))
            sprites.draw(screen)
            pygame.display.flip()
