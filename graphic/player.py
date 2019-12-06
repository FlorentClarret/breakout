import pygame

from graphic.colors import BLACK
from graphic.graphical_element import GraphicalElement

MINIMAL_WIDTH = 70
MAXIMAL_WIDTH = 2 * MINIMAL_WIDTH
HEIGHT = 15


class Player(GraphicalElement):
    def __init__(self):
        super().__init__()
        self.height = HEIGHT
        self.__create_bar(MINIMAL_WIDTH, pygame.mouse.get_pos()[0])

    def move(self):
        mouse_x = pygame.mouse.get_pos()[0]

        if mouse_x < (self.width // 2):
            self.rect.x = 0
        elif mouse_x > self.screen_width - (self.width // 2):
            self.rect.x = self.screen_width - self.width
        else:
            self.rect.x = mouse_x - (self.width // 2)

    def grow(self):
        self.__create_bar(min(MAXIMAL_WIDTH, self.width + 10), self.rect.x)

    def diminish(self):
        self.__create_bar(max(MINIMAL_WIDTH, self.width - 10), self.rect.x)

    def __create_bar(self, width, previous_x):
        self.width = width
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = previous_x
        self.rect.y = self.screen_height - self.height - 10
