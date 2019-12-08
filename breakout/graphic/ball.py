import math

import pygame

from graphic.colors import RED
from graphic.graphical_element import GraphicalElement

BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_INITIAL_DIRECTION = 180
BALL_SPEED = 5


class Ball(GraphicalElement):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height)
        self.direction = BALL_INITIAL_DIRECTION
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.speed = BALL_SPEED
        self.x = x
        self.y = y
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def bounce(self, diff):
        self.direction = ((180 - self.direction) % 360) - diff

    def move(self):
        direction_radians = math.radians(self.direction)

        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        if self.x > self.screen_width - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screen_width - self.width - 1

    def is_out_of_screen(self):
        return self.y > self.screen_height
