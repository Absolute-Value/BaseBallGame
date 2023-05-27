import pygame
import sys
from entities import *
from define import *
from field import Field

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Baseball Game")
    clock = pygame.time.Clock()

    field = Field()
    batter = Batter(field.base_home_and_line.x - 30, field.base_home_and_line.y - 10)
    pitcher = Player(field.picher_mound.x, field.picher_mound.y + 4)
    catcher = Player(field.base_home_and_line.x, field.base_home_and_line.y + 30)
    first = Player(field.base_first.x, field.base_first.y - 50)
    second = Player(field.base_second.x + 100, field.base_second.y)
    short = Player(field.base_second.x - 100, field.base_second.y)
    third = Player(field.base_third.x, field.base_third.y - 50)

    ball = Ball(pitcher.x, pitcher.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 野球場の描画
        field.draw(screen)
        ball.move()
        if ball.y > catcher.y:
            ball = Ball(pitcher.x, pitcher.y)
        ball.draw(screen)
        pitcher.draw(screen)
        batter.draw(screen)
        catcher.draw(screen)
        first.draw(screen)
        second.draw(screen)
        short.draw(screen)
        third.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()