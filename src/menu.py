import pygame
import game

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
        option_obj -- a dictionary with the objects of the options
        color -- the highlighted color
    """
    def __init__(self, options, font_size, font_space, color, highlight_color, bg_color, font=None):
        self.options = options
        self.font = pygame.font.Font(font, font_size)
        self.font_size = font_size
        self.font_space = font_space
        self.height = (font_size + font_space) * len(options)
        self.active = False
        self.option_obj = dict()
        self.color = color
        self.highlight_color = highlight_color
        self.bg_color = bg_color

    def highlight(self, number_of_option):
        """Highlight the specified option on the menu

        number_of_option -- the number of the option to be highlighted
        """
        if self.active:
            self.highlight_entry = number_of_option
        else:
            self.active = True
            self.highlight_entry = number_of_option

    def display(self, screen):
        """Display the menu
        This function is responsible for updating the menu selection and
        reading the user input. Furthermore, it creates the game object
        and performs the necessary actions.

        screen -- the display that the menu will be displayed
        """
        y = screen.get_height()//2 - self.height//2 

        #a dictionary with the objects of the menu options
        #{number} => (text object, rect object)
        for num, entry in enumerate(self.options):
            if self.active and self.highlight_entry == num:
                text = self.font.render(entry, 1, self.highlight_color)
            else:
                text = self.font.render(entry, 1, self.color)
            text_rect = text.get_rect(centerx=screen.get_width()//2, centery=y + self.font_size + self.font_space)
            self.option_obj[num] = text, text_rect
            y += self.font_size + self.font_space

        screen.fill(self.bg_color)
        for text, rect in self.option_obj.itervalues():
            screen.blit(text, rect)
        pygame.display.flip()

class MainMenu(Menu):
    """Main menu of the game
    This menu is displayed at the starting screen of the game
    """

    def __init__(self):
        options = ('Start game',
                   'Scores',
                   'Options',
                   'Credits',
                   'Exit')
        font_size = 36
        font_space = 4
        super(MainMenu, self).__init__(options, font_size, font_space, WHITE, RED, BLACK)

    def handle_input(self, screen):
        """Handle the user input
        This function is responsible for updating the menu selection and
        reading the user input. Furthermore, it creates the game object
        and performs the necessary actions.

        screen -- the display that the menu will be displayed
        """
        clock = pygame.time.Clock()
        self.display(screen)
        
        while True:
            dt = clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.active:
                            self.highlight((self.highlight_entry + 1) % len(self.options))
                        else:
                            self.active = True
                            self.highlight(0)
                        self.display(screen)

                    if event.key == pygame.K_UP:
                        if self.active:
                            self.highlight((self.highlight_entry - 1) % len(self.options))
                        else:
                            self.active = True
                            self.highlight(len(self.options) - 1)
                        self.display(screen)

                    elif event.key == pygame.K_ESCAPE:
                        self.active = False
                        self.display(screen)

                    elif event.key == pygame.K_RETURN:
                        if self.active:
                            if self.options[self.highlight_entry] == "Start game":
                                game.Game((screen.get_width(), screen.get_height())).main(screen)
                                self.active = False
                                self.display(screen)
                            elif self.options[self.highlight_entry] == "Exit":
                                return


class PauseMenu(Menu):
    """Pause menu of the game
    This menu is displayed when the user pauses the game
    """
    def __init__(self):
        options = ('Return to game',
                   'Options',
                   'Exit to main menu')
        font_size = 36
        font_space = 4
        super(PauseMenu, self).__init__(options, font_size, font_space, BLACK, BLUE, WHITE)

    def handle_input(self, screen, game_instance):
        """Handle the user input
        This function is responsible for updating the menu selection and
        reading the user input. Furthermore, it creates the game object
        and performs the necessary actions.

        screen -- the display that the menu will be displayed
        """
        clock = pygame.time.Clock()
        self.display(screen)
        
        while True:
            dt = clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.active:
                            self.highlight((self.highlight_entry + 1) % len(self.options))
                        else:
                            self.active = True
                            self.highlight(0)
                        self.display(screen)

                    if event.key == pygame.K_UP:
                        if self.active:
                            self.highlight((self.highlight_entry - 1) % len(self.options))
                        else:
                            self.active = True
                            self.highlight(len(self.options) - 1)
                        self.display(screen)

                    elif event.key == pygame.K_ESCAPE:
                        self.active = False
                        self.display(screen)
                        game_instance.paused = False
                        return

                    elif event.key == pygame.K_RETURN:
                        if self.active:
                            if self.options[self.highlight_entry] == "Return to game":
                                game_instance.paused = False
                                return
