import pygame
from game import Game

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 


class Menu(object):
    """The basic menu class of the game
    This class is used as a parent for the various classes that represent the
    menus in the game.
    
    args:

        options -- a tuple of possible options in the menu
        font_size -- integer representing the size of the font
        font_space -- integer representing the space between the entries
        font -- the type of font to be used

    attrs:
       
        options -- the list of possible options in the menu
        font_size -- integer representing the size of the font
        font_space -- integer representing the space between the entries
        font -- the type of font to be used
        height -- the height of the menu
        active -- a bool indicating if the menu is currently active
    """
    def __init__(self, options, font_size, font_space, font=None):
        self.options = options
        self.font = pygame.font.Font(font, font_size)
        self.font_size = font_size
        self.font_space = font_space
        self.height = (font_size + font_space) * len(options)
        self.active = False

    def display(self, screen):
        pass

class MainMenu(Menu):
    """Main menu of the game
    This menu is displayed at the starting screen of the game
    """

    def __init__(self, font_size=36, font_space=4):
        options = ('Start game',
                   'Scores',
                   'Options',
                   'Credits',
                   'Exit')
        font_space = font_space
        font_size = font_size
        super(MainMenu, self).__init__(options, font_size, font_space)

    def display(self, screen):
        """Display the menu
        This function is responsible for updating the menu selection and
        reading the user input. Furthermore, it creates the game object
        and performs the necessary actions.

        screen -- the display that the menu will be displayed
        """
        clock = pygame.time.Clock()
        y = screen.get_height()//2 - self.height//2 

        option_obj = dict()
        #a dictionary with the objects of the menu options
        #{number} => (text object, rect object)
        for num, entry in enumerate(self.options):
            text = self.font.render(entry, 1, WHITE)
            text_rect = text.get_rect(centerx=screen.get_width()//2, centery=y + self.font_size + self.font_space)
            option_obj[num] = text, text_rect
            y += self.font_size + self.font_space

        for text, rect in option_obj.itervalues():
            screen.blit(text, rect)
        pygame.display.flip()
        
        while True:
            dt = clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.active:
                            option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, WHITE), option_obj[highlight_entry][1]
                            highlight_entry = (highlight_entry + 1) % len(self.options)
                        else:
                            self.active = True
                            highlight_entry = 0
                        option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, RED), option_obj[highlight_entry][1]
                        screen.fill(BLACK)
                        for text, rect in option_obj.itervalues():
                            screen.blit(text, rect)
                        pygame.display.flip()

                    if event.key == pygame.K_UP:
                        if self.active:
                            option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, WHITE), option_obj[highlight_entry][1]
                            highlight_entry = (highlight_entry - 1) % len(self.options)
                        else:
                            self.active = True
                            highlight_entry = len(self.options) - 1
                        option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, RED), option_obj[highlight_entry][1]
                        screen.fill(BLACK)
                        for text, rect in option_obj.itervalues():
                            screen.blit(text, rect)
                        pygame.display.flip()

                    elif event.key == pygame.K_ESCAPE:
                        option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, WHITE), option_obj[highlight_entry][1]
                        self.active = False
                        screen.fill(BLACK)
                        for text, rect in option_obj.itervalues():
                            screen.blit(text, rect)
                        pygame.display.flip()

                    elif event.key == pygame.K_RETURN:
                        if self.active:
                            if self.options[highlight_entry] == "Start game":
                                Game((screen.get_width(), screen.get_height())).main(screen)

                                option_obj[highlight_entry] = self.font.render( self.options[highlight_entry], 1, WHITE), option_obj[highlight_entry][1]
                                self.active = False
                                screen.fill(BLACK)
                                for text, rect in option_obj.itervalues():
                                    screen.blit(text, rect)
                            elif self.options[highlight_entry] == "Exit":
                                return
                        pygame.display.flip()


