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
    fielders = Fielders(field)
    batter = Batter(field.base_home_and_line.x - 30, field.base_home_and_line.y - 10)
    ball = Ball(fielders.pitcher.x, fielders.pitcher.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 野球場の描画
        field.draw(screen)
        ball.move()
        if ball.y > fielders.catcher.y:
            ball = Ball(fielders.pitcher.x, fielders.pitcher.y)
        ball.draw(screen)
        fielders.draw(screen)
        batter.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()