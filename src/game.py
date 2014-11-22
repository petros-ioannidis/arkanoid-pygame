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

    def __init__(self, screen, dimension, bg_color = WHITE):
        """constructor for the game object

        dimension -- a dictionary with 'x' and 'y' keys with the dimensions of the game screen
        bg_color -- the color of the board (R, G, B)
        """
        self.bg_color = bg_color
        self.dimension = {'x': dimension[0], 'y': dimension[1]}
        self.paused = False
        self.score = 0
        self.screen = screen

    def main(self, stage_name):
        clock = pygame.time.Clock()
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
                            (self.dimension['x'] - wall_size[1],0)],\

                            [hori_wall,
                            vert_wall,
                            vert_wall],\

                            [TopWall,
                            LeftWall,
                            RightWall
                        ])


        #open and parse the stage file
        stage_file = open(stage_name, 'r')
        initial_grid = eval(stage_file.read().rstrip())

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
                        exit = menu.PauseMenu(self).handle_input(self.screen)
                        if exit:
                            return
                        dt = clock.tick(120)
            if not self.blocks.sprites():
                exit = self.win()
                if exit:
                    return
            if self.ball.position['y'] > self.dimension['y']:
                exit = self.win()
                if exit:
                    return
            dt = clock.tick(120)
            self.sprites.update(dt/1000., self)
            self.screen.fill((200, 200, 200))
            self.sprites.draw(self.screen)
            pygame.display.flip()

    def win(self):
        exit = menu.EndGameMenu(self).handle_input(self.screen)
        return exit
