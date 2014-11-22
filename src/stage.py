from ball import Ball
from racket import Racket
from block import Block

class Stage(object):
    """Stage class used for generating the stage that the player will play
    and update the state of the stage
    
    arguments:
    game -- the game object that the stage will be spawned
    initial_grid -- a tuple of tuples that initiates the starting grid
    racket_potition -- starting position of the player racket(default is middle)
    walls -- a list of tuples with the following format 
             (starting coordinates, ending coordinages, Class of wall)

    keyword arguments:
    ball_position -- None if the ball is attached to the Racket else the coords
                     as a tuple
    """
    def __init__(self, game, initial_grid, racket_potition, walls, ball_position = None):
        game.player = Racket(racket_potition, game.players)

        for _block in initial_grid:
            _ = Block(_block[0], _block[1], game.blocks)

        if ball_position:
            game.ball = Ball(ball_position, game.sprites)
        else: 
            game.ball = Ball((0,0), game.sprites)
            game.ball.attach(game.player, 'up')

        for _wall in walls:
            _ = _wall[2](_wall[0], _wall[1], game.walls)
