import pygame

from graphic.colors import BLACK
from graphic.graphical_element import GraphicalElement

BRICK_WIDTH = 30
BRICK_HEIGHT = 15
BRICK_MAX_HEALTH = 1


class Brick(GraphicalElement):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height)
        self.height = BRICK_HEIGHT
        self.width = BRICK_WIDTH
        self.health = BRICK_MAX_HEALTH
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def is_broken(self):
        return self.health == 0

    def is_not_broken(self):
        return not self.is_broken()

    def hit(self):
        self.health = max(0, self.health - 1)
