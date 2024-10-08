# snake.py

import pygame
from constants import SNAKE_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]  # Initial body segments
        self.direction = pygame.K_RIGHT  # Initial direction
        self.grow = False  # Growth flag

    def move(self):
        head = self.body[0].copy()

        if self.direction == pygame.K_UP:
            head[1] -= SNAKE_SIZE
        elif self.direction == pygame.K_DOWN:
            head[1] += SNAKE_SIZE
        elif self.direction == pygame.K_LEFT:
            head[0] -= SNAKE_SIZE
        elif self.direction == pygame.K_RIGHT:
            head[0] += SNAKE_SIZE

        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, direction):
        opposite_directions = {pygame.K_UP: pygame.K_DOWN, pygame.K_DOWN: pygame.K_UP,
                               pygame.K_LEFT: pygame.K_RIGHT, pygame.K_RIGHT: pygame.K_LEFT}
        if direction != opposite_directions.get(self.direction, None):
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN,
                             pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
