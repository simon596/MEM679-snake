# snake_game.py

import pygame
import sys
from constants import *
from snake import Snake
from food import Food

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()
        self.score = 0

        self.font = pygame.font.SysFont('Arial', 25)
        self.game_over = False

    def check_food_collision(self):
        if self.snake.body[0] == self.food.position:
            self.snake.grow_snake()
            self.score += 1
            self.place_food()

    def place_food(self):
        while True:
            self.food.randomize_position()
            if self.food.position not in self.snake.body:
                break

    def check_wall_collision(self):
        head = self.snake.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            self.game_over = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not self.game_over:
                    self.snake.change_direction(event.key)
                else:
                    if event.key == pygame.K_r:
                        self.__init__()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def update(self):
        if not self.game_over:
            self.snake.move()
            self.check_food_collision()
            self.check_wall_collision()
            if self.snake.check_collision():
                self.game_over = True

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, [0, 0])

    def show_game_over(self):
        game_over_text = self.font.render('Game Over!', True, RED)
        retry_text = self.font.render('Press R to Retry or Q to Quit', True, RED)
        self.screen.blit(game_over_text, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3])
        self.screen.blit(retry_text, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2])

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        if self.game_over:
            self.show_game_over()
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(SNAKE_SPEED)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()
