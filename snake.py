from collections import deque, namedtuple
from random import randint

import pyxel

Point = namedtuple("point", ["x", "y"])

########## Global Constants ##########

#### Main Screen Game Colors ####
BACKGROUND_COLOR = 0
BODY_COLOR = 7
HEAD_COLOR = 3
FOOD_COLOR = 8
SB_TEXT = 1
SB_BACKGROUND = 8

#### Game Over Colors ####
GAMEOVER_TEXT = ["GAME OVER", "PLAY AGAIN?", "PRESS Y OR N"]
GAMEOVER_TEXT_COLOR = 0
GAMEOVER_COLOR = 7

#### Dimensions of Game Window ####
WIDTH = 40
HEIGHT = 50

SB_HEIGHT = pyxel.FONT_HEIGHT

#### Define Nav Directions ####
UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
INITIAL = Point(5, 5)       ###The starting point of the game

#### Classes ####

class Snake: 
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption = "Pre-Sliter.io", fps = 0)
        self.start
        pyxel.run(self.update, self.draw)
    
    def start(self):
        self.snake = deque()
        self.direction = RIGHT
        self.score = 0
        self.death = False
        self.spawn_food()
         





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

    def spawn_food(self):
        snake_pixels = set(self.snake)
        self.food = self.snake[0]
        while self.food in snake_pixels:
            x = randint(0, WIDTH - 1)            ### The '-1' is needed because the max width value would appear off screen
            y = randint(0, HEIGHT - 1)

    def eat(self):


    def grow_snake(self):
        head = self.snake[0]
        new_head = Point(head.x + self.direction.x, head.y + self.direction.y)
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()