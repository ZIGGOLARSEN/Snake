import pygame

SCREEN_WIDTH = 720
SCREEN_HEIHGT = 720

SNAKE_SPEED = 24
GAME_SPEED = 0.1

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIHGT))

ICON = pygame.image.load(r'.\images\anaconda.png')
SNAKE = pygame.image.load(r'.\images\green-square-svgrepo-com.svg')
APPLE = pygame.image.load(r'.\images\apple.png')
GAME_OVER = pygame.image.load(r'.\images\game-over.png')