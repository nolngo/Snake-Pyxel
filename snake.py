from collections import deque, namedtuple
from random import randint

import pyxel

Point = namedtuple("point", ["x", "y"])

#### Global Constants ####
BACKGROUND_COLOR = 0
BODY_COLOR = 7
HEAD_COLOR = 3
APPLE_COLOR = 8
GAMEOVER_COLOR = 7

GAMEOVER_TEXT = ["GAME OVER", "PLAY AGAIN?", "PRESS Y OR N"]
GAMEOVER_TEXT_COLOR = 0

WIDTH = 40
HEIGHT = 50





#### Classes ####

class Snake: 
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption = "Not Sliter.io", fps = 0)
    
    def start(self):
        self.direction = RIGHT
