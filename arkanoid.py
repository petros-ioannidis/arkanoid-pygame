import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

class ball(pygame.sprite.Sprite):
    """Player class"""

    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('ball.png')
        self.rect = pygame.rect.Rect((320,280), self.image.get_size())
    
    def update(self, dt, game):
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300*dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300*dt
        if key[pygame.K_UP]:
            self.rect.y -= 300*dt
        if key[pygame.K_DOWN]:
            self.rect.y += 300*dt

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom


class Game(object):
    """Main game"""

    def __init__(self, bg_color = WHITE):
        self.bg_color = bg_color

    def main(self, screen):
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('wall.png')
        for x in range(0,640,10):
            for y in range(0,480,10):
                if x in (0, 640-10) or y in (0,480-10):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x,y), block.get_size())
        sprites.add(self.walls)
        while True:
            dt = clock.tick(30)
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
