import random
from constants import *

class Snake:
    head = {'img': SNAKE}
    body = [{'img': SNAKE}]
    speed = SNAKE_SPEED
    
    def __init__(self):
        self.position_randomly()
        self.construct_snake()
        self.allign_body()
        self.direction = None
    

    def construct_snake(self):
        self.snake = [self.head] + self.body
    
    def allign_body(self):
        for idx,part  in enumerate(self.snake):
            if idx == 0: continue

            part['x'] = self.snake[idx-1]['x']
            part['y'] = self.snake[idx-1]['y'] + part['img'].get_height()

    def position_randomly(self):
        x = random.randint(1, (SCREEN_WIDTH-24)/24)
        y = random.randint(1, (SCREEN_HEIHGT-24)/24)

        self.head['x'] = x*24
        self.head['y'] = y*24
    

    def move(self):
        for idx in range(len(self.snake)-1, 0, -1):
            self.snake[idx]['x'] = self.snake[idx-1]['x']
            self.snake[idx]['y'] = self.snake[idx-1]['y']
            
        if self.direction == 'right': self.head['x'] += self.speed
        if self.direction == 'left': self.head['x'] -= self.speed
        if self.direction == 'down': self.head['y'] += self.speed
        if self.direction == 'up': self.head['y'] -= self.speed

    def handle_boundries(self):
        if self.head['x'] >= SCREEN_WIDTH: self.head['x'] = 0
        if self.head['x'] <= -24: self.head['x'] = SCREEN_WIDTH
        if self.head['y'] <= -24: self.head['y'] = SCREEN_HEIHGT-24
        if self.head['y'] >= SCREEN_HEIHGT: self.head['y'] = 0

    def self_colide(self):
        for idx,part in enumerate(self.snake):
            if idx == 0: continue

            if self.head['x'] == part['x'] and self.head['y'] == part['y']: return True
        
        return False