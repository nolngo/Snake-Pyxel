from collections import deque, namedtuple
from random import randint

import pyxel

Point = namedtuple("point", ["x", "y"])

########## Global Constants ##########

#### Main Screen Game Colors ####
BACKGROUND_COLOR = 0
BODY_COLOR = 7
HEAD_COLOR = 3
APPLE_COLOR = 8

#### Game Over Colors ####
GAMEOVER_TEXT = ["GAME OVER", "PLAY AGAIN?", "PRESS Y OR N"]
GAMEOVER_TEXT_COLOR = 0
GAMEOVER_COLOR = 7

#### Dimensions of Game Window ####
WIDTH = 40
HEIGHT = 50

#### Define Nav Directions ####
UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
INITIAL = Point(5, 5)       ###The starting point of the game

#### Classes ####

class Snake: 
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption = "Not Sliter.io", fps = 0)
    
    def initial(self):
        self.direction = RIGHT
        self.score = 0





def update(self):
    pass

def controls(self):
    if pyxel.btn(pyxel.KEY_UP):
        if self.direction is not DOWN:      ### In Snake, you cannot flip 180 degrees onto your own body, which is why we need the "is not" statement
            self.direction = UP
    elif pyxel.btn(pyxel.KEY_DOWN):
        if self.direction is not UP:
            self.direction = DOWN
    elif pyxel.btn(pyxel.KEY_LEFT):
        if self.direction is not RIGHT:
            self.direction = LEFT
    elif pyxel.btn(pyxel.KEY_RIGHT):
        if self.direction is not LEFT:
            self.direction = RIGHT

