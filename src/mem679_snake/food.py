# food.py

import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, RED

class Food:
    def __init__(self):
        self.position = [0, 0]
        self.randomize_position()

    def randomize_position(self):
        self.position = [
            random.randrange(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
            random.randrange(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
        ]

    def draw(self, screen):
        pygame.draw.rect(screen, RED,
                         pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))
