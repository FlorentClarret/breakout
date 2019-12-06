import pygame


class GraphicalElement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()