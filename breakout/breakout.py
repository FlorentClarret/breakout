import pygame

from graphic.ball import Ball, BALL_HEIGHT, BALL_WIDTH
from graphic.brick import Brick, BRICK_WIDTH, BRICK_HEIGHT
from graphic.colors import WHITE
from graphic.player import Player

FPS = 30
SCREEN_WIDTH = 278
SCREEN_HEIGHT = 300


def main():
    pygame.init()
    pygame.display.set_caption("Awesome break out")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_sprites_group = pygame.sprite.Group()
    all_bricks_group = pygame.sprite.Group()
    all_balls_group = pygame.sprite.Group()

    player = Player(pygame.display.get_surface().get_width(),
                    pygame.display.get_surface().get_height(),
                    pygame.mouse.get_pos()[0])
    clock = pygame.time.Clock()

    all_sprites_group.add(player)

    ball = Ball(pygame.display.get_surface().get_width(),
                pygame.display.get_surface().get_height(),
                player.rect.x + player.width // 2 - (BALL_WIDTH // 2),
                player.rect.y - BALL_HEIGHT)

    all_balls_group.add(ball)
    all_sprites_group.add(ball)

    for i in range(9):
        for j in range(1):
            brick = Brick(pygame.display.get_surface().get_width(),
                          pygame.display.get_surface().get_height(),
                          i * BRICK_WIDTH + i,
                          10 + j + (j * BRICK_HEIGHT))
            all_sprites_group.add(brick)
            all_bricks_group.add(brick)

    while True:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if ball.is_out_of_screen():
            # TODO do not quit like that
            return

        player.move(pygame.mouse.get_pos()[0])
        ball.move()

        if pygame.sprite.spritecollide(player, all_balls_group, False):
            ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
            ball.bounce((player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2))

        bricks_hit = pygame.sprite.spritecollide(ball, all_bricks_group, False)

        if bricks_hit:
            brick = bricks_hit[0]
            brick.hit()
            ball.bounce(0)

            if brick.is_broken():
                brick.kill()

            if len(all_bricks_group) == 0:
                # TODO do not quit like that
                return

        all_sprites_group.update()

        all_sprites_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
