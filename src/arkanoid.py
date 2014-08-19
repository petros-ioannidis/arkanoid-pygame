import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    dim = (800, 600)
    #dim = (640, 480)
    screen = pygame.display.set_mode(dim)
    Game(dim).main(screen)
