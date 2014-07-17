import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

class Ball(pygame.sprite.Sprite):
    """Ball class"""

    def __init__(self, *groups):
        super(Ball, self).__init__(*groups)
        self.image = pygame.image.load('ball.png')
        self.rect = pygame.rect.Rect((320,280), self.image.get_size())
        self.speed = {'x': 300, 'y': 300}
    
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
        self.rect.x += self.speed['x']*dt
        self.rect.y += self.speed['y']*dt

        new = self.rect
        #print last
        #print new
        #canditates = ['down': 0, 'up': 0, 'left': 0, 'right': 0,
        #print self.rect
        #print "len", len(pygame.sprite.spritecollide(self, game.walls, False))
        #while len(pygame.sprite.spritecollide(self, game.walls, False)) > 1:
            #print "len in", len(pygame.sprite.spritecollide(self, game.walls, False))
            #print self.speed
            #if self.speed['x'] > 0:
                #self.rect.x -= 1
            #else:
                #self.rect.x += 1
#
            #if self.speed['y'] > 0:
                #self.rect.y -= 1
            #else:
                #self.rect.y += 1
#
        #print 'after'
        #print "len", len(pygame.sprite.spritecollide(self, game.walls, False))
        ##print self.rect
        #if len(pygame.sprite.spritecollide(self, game.walls, False)) == 0:
            #if self.speed['x'] > 0:
                #self.rect.x += 1
            #else:
                #self.rect.x -= 1
#
            #if self.speed['y'] > 0:
                #self.rect.y += 1
            #else:
                #self.rect.y -= 1

        #print pygame.sprite.spritecollide(self, game.walls, False)
        print self.speed
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                #print 1
                new.right = cell.left
                #canditates['left'] += 1
                self.speed['x'] = -300
            elif last.left >= cell.right and new.left < cell.right:
                #print 2
                #canditates['right'] += 1
                new.left = cell.right
                self.speed['x'] = 300
            if last.bottom <= cell.top and new.bottom > cell.top:
                #print 3
                new.bottom = cell.top
                self.speed['y'] = -300
                #canditates['down'] += 1
            elif last.top >= cell.bottom and new.top < cell.bottom:
                #print 4
                new.top = cell.bottom
                self.speed['y'] = 300
                #canditates['up'] += 1



class Game(object):
    """Main game"""

    def __init__(self, bg_color = WHITE):
        self.bg_color = bg_color

    def main(self, screen):
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        self.player = Ball(sprites)
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('wall.png')
        block_size = block.get_size()
        hori_block = pygame.transform.scale(block, (640, block_size[1]))
        vert_block = pygame.transform.scale(block, (block_size[0], 480))

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_block
        print block.get_size()
        wall.rect = pygame.rect.Rect((0,0), hori_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_block
        print block.get_size()
        wall.rect = pygame.rect.Rect((0,0), vert_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = hori_block
        print block.get_size()
        wall.rect = pygame.rect.Rect((0,470), hori_block.get_size())

        wall = pygame.sprite.Sprite(self.walls)
        wall.image = vert_block
        print block.get_size()
        wall.rect = pygame.rect.Rect((630,0), vert_block.get_size())
        #for x in range(0,640,10):
        #    for y in range(0,480,10):
        #        if x in (0, 640-10) or y in (0,480-10):
        #            wall = pygame.sprite.Sprite(self.walls)
        #            wall.image = block
        #            print block.get_size()
        #            wall.rect = pygame.rect.Rect((x,y), block.get_size())
        sprites.add(self.walls)
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
