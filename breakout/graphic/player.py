import pygame

from graphic.colors import BLACK
from graphic.graphical_element import GraphicalElement

MINIMAL_WIDTH = 70
MAXIMAL_WIDTH = 2 * MINIMAL_WIDTH
GROWTH = 10
HEIGHT = 15


class Player(GraphicalElement):
    def __init__(self, screen_width, screen_height, position=0):
        super().__init__(screen_width, screen_height)
        self.height = HEIGHT
        self.__create_bar(MINIMAL_WIDTH, position)

    def move(self, position):
        if position < (self.width // 2):
            self.rect.x = 0
        elif position > self.screen_width - (self.width // 2):
            self.rect.x = self.screen_width - self.width
        else:
            self.rect.x = position - (self.width // 2)

    def grow(self):
        self.__create_bar(min(MAXIMAL_WIDTH, self.width + GROWTH), self.rect.x)

    def diminish(self):
        self.__create_bar(max(MINIMAL_WIDTH, self.width - GROWTH), self.rect.x)

    def __create_bar(self, width, previous_x):
        self.width = width
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = previous_x
        self.rect.y = self.screen_height - self.height - 10
