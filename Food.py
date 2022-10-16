import random
from constants import *

class Food:
    img = APPLE
    
    def __init__(self, snake):
        self.position_randomly(snake)
    
    def position_randomly(self, snake):
        x = random.randint(1, (SCREEN_WIDTH-24)/24)
        y = random.randint(1, (SCREEN_HEIHGT-24)/24)

        self.x = x*24
        self.y = y*24

        while self.x in self.compute_allowed_positions(snake)[0] and self.y in self.compute_allowed_positions(snake)[1]:
            x = random.randint(1, (SCREEN_WIDTH-24)/24)
            y = random.randint(1, (SCREEN_HEIHGT-24)/24)
            self.x = x*24
            self.y = y*24

    def compute_allowed_positions(self, snake):
        x = []
        y = []
        for part in snake:
            x.append(part['x'])
            y.append(part['y'])
        return x,y
    