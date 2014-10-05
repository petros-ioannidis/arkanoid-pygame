from __future__ import division
import pygame
import menu
from wall import LeftWall, RightWall, BottomWall, TopWall 
from stage import Stage

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
        #sprites = pygame.sprite.Group()
        #self.players = pygame.sprite.Group()
        #self.ball = Ball((300, 200), sprites)
        self.sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        #should the walls go inside the stage class? think about it
        wall_size = (10,10)
        self.walls = pygame.sprite.Group()
        hori_wall = (self.dimension['x'], wall_size[1])
        vert_wall = (wall_size[0], self.dimension['y'])

        wall_list = zip([
                            (0,0), 
                            (0,0),
                            (0,self.dimension['y'] - wall_size[0]), 
                            (self.dimension['x'] - wall_size[1],0)],\

                            [hori_wall,
                            vert_wall,
                            hori_wall,
                            vert_wall],\

                            [TopWall,
                            LeftWall,
                            BottomWall,
                            RightWall
                        ])


        #random block position
        initial_grid = []
        for dimx in range(10):
            for dimy in range(6):
                initial_grid.append((100 + dimx*61, 100 + dimy*21))

        print initial_grid
        self.stage = Stage(self, initial_grid, (self.dimension['x']/2, self.dimension['y'] - wall_size[1]), wall_list)

        self.sprites.add(self.walls)
        self.sprites.add(self.players)
        self.sprites.add(self.blocks)

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
            self.sprites.update(dt/1000., self)
            screen.fill((200, 200, 200))
            self.sprites.draw(screen)
            pygame.display.flip()
