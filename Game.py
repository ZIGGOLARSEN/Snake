from constants import *
from Snake import Snake
from Food import Food
import time

pygame.init()


class Game:
    screen = SCREEN
    score = 0
    snake, food, font = None, None, None
    running, key_pressed, over = False, False, False

    def __init__(self):
        self.setup()

    def setup(self):
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption('Snake')
        pygame.display.set_icon(ICON)
        self.score = 0
        self.snake = Snake()
        self.food = Food(self.snake.snake)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.render()


    def eat(self):
        if self.snake.head['x'] == self.food.x and self.snake.head['y'] == self.food.y:

            self.snake.snake.append({'img': SNAKE, 'x': self.snake.snake[-1]['x'], 'y': self.snake.snake[-1]['y']})

            self.food = Food(self.snake.snake)

            self.score += 1


    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.key_pressed = True

            if event.key == pygame.K_RIGHT and self.snake.direction != 'left':
                self.snake.direction = 'right'

            if event.key == pygame.K_LEFT and self.snake.direction != 'right':
                self.snake.direction = 'left'

            if event.key == pygame.K_DOWN and self.snake.direction != 'up':
                self.snake.direction = 'down'

            if event.key == pygame.K_UP and self.snake.direction != 'down':
                self.snake.direction = 'up'

            if event.key == pygame.K_ESCAPE:
                self.running = False

            if event.key == pygame.K_r:
                self.setup()

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def handle_events(self, event):
        self.handle_key_events(event)
        self.handle_quit_event(event)


    def display_score(self):
        score = self.font.render(f'score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score, (0, 0))


    def game_over(self):
        if self.snake.self_colide():
            self.screen.blit(GAME_OVER, ((SCREEN_WIDTH-GAME_OVER.get_width())/2, (SCREEN_HEIHGT-GAME_OVER.get_height())/2))
            self.over = True
            pygame.display.update()


    def update_screen(self):
        self.screen.fill((0, 0, 0))

        for part in self.snake.snake:
            self.screen.blit(part['img'], (part['x'], part['y']))

        self.screen.blit(self.food.img, (self.food.x, self.food.y))

        self.display_score()

        pygame.display.update()


    def render(self):
        self.running = True
        self.key_pressed, self.over = False, False

        while self.running:
            for event in pygame.event.get():
                self.handle_events(event)

            if self.key_pressed:
                self.snake.move()

            time.sleep(GAME_SPEED)

            self.eat()
            self.snake.handle_boundries()
            self.game_over()

            if not self.over:
                self.update_screen()

Game()
