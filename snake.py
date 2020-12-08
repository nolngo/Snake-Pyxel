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
GAMEOVER_TEXT = ["GAME OVER", "PLAY AGAIN?", "Q TO QUIT | R TO RETRY"]
GAMEOVER_TEXT_COLOR = 0
GAMEOVER_COLOR = 7
GAMEOVER_HEIGHT = 5

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

########## Classes ##########

class Snake: 
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption = "Pre-Sliter.io", fps = 15)              #### FPS determines the pace of the game, how often the program UPDATES!!!
        self.reset
        pyxel.run(self.update, self.render)
    
    def reset(self):                                   ### This will reinitiate the game back to starting position
        self.direction = RIGHT
        self.snake = deque()
        self.snake.append(INITIAL)
        self.death = False
        self.score = 0
        self.spawn_food()


    def update(self):
        if not self.death:
            self.controls()
            self.grow_snake()
            self.eat()
            self.is_dead()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if pyxel.btnp(pyxel.KEY_R):
            self.reset()



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
            x = randint(0, WIDTH - 1)               ### The '-1' is needed because the max width value would appear off screen
            y = randint(SB_HEIGHT + 1, HEIGHT - 1)
            self.food = Point(x, y)

    def eat(self):
        if self.snake[0] == self.food:              ### This line checks if the position of the head of the snake equals the food.
            self.score += 1                         ### If the position of the head and the food matches, the snake will eat it and gain a point.
            self.snake.append(self.popped_point)    ### The snake gets longer through this append to deque process. Making it easier to mess up.
            self.spawn_food()                       ### When the food is eaten, a new one will spawn.

    def grow_snake(self):
        old_head = self.snake[0]                                                                ### Identifies snake[0] as the head
        new_head = Point(old_head.x + self.direction.x, old_head.y + self.direction.y)              
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()

    def is_dead(self):
        head = self.snake[0]
        if head.x < 0 or head.y <= SB_HEIGHT or head.x > WIDTH or head.y >= HEIGHT:
            self.game_over()
        if len(self.snake) != len(set(self.snake)):
            self.game_over()
    
    def game_over(self):
        self.death = True

        pyxel.stop()

########## Rendering ###########

    def render(self):
        if not self.death:
            pyxel.cls(col=BACKGROUND_COLOR)
            self.render_snake()
            self.render_score()
            pyxel.pset(self.food.x, self.food.y, col=FOOD_COLOR)
        else:
            self.render_game_over()

    def render_snake(self):
        for i, point in enumerate(self.snake):
            if i == 0:
                color = HEAD_COLOR
            else:
                color = BODY_COLOR
            pyxel.pset(point.x, point.y, col=color)

    def render_score(self):
        score = "{:03}".format(self.score)                              ### Makes the Score a 3 digit number with 000 as the starting score.
        pyxel.rect(0, 0, WIDTH, SB_HEIGHT, SB_BACKGROUND)               ### 0 margin 0 padding
        pyxel.text(1, 1, score, SB_TEXT)                                ### 1 margin 1 padding bc text is within the scoreboard.
        

    def render_game_over(self):
        pyxel.cls(col=GAMEOVER_COLOR)
        display_text = GAMEOVER_TEXT[:]
        for i, text in enumerate(display_text):
            y_offset = (pyxel.FONT_HEIGHT + 2) * i
            text_x = self.center_text(text, WIDTH)
            pyxel.text(text_x, GAMEOVER_HEIGHT + y_offset, text, GAMEOVER_TEXT_COLOR)

    @staticmethod
    def center_text(text, page_width, char_width=pyxel.FONT_WIDTH):
        text_width = len(text) * char_width
        return (page_width - text_width) // 2

Snake()