import pygame
from menu import MainMenu

if __name__ == '__main__':
    pygame.init()
    dim = (800, 600)
    screen = pygame.display.set_mode(dim)
    #pygame.display.toggle_fullscreen()
    MainMenu().handle_input(screen)
