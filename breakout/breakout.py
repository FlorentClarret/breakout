import pygame

from graphic.colors import WHITE
from graphic.player import Player

FPS = 60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


def main():
    pygame.init()
    pygame.display.set_caption("Awesome break out")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_sprites_group = pygame.sprite.Group()

    player = Player(pygame.display.get_surface().get_width(),
                    pygame.display.get_surface().get_height(),
                    pygame.mouse.get_pos()[0])
    clock = pygame.time.Clock()

    all_sprites_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(FPS)
        screen.fill(WHITE)
        all_sprites_group.update()

        player.move(pygame.mouse.get_pos()[0])

        all_sprites_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
