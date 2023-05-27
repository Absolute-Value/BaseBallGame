import pygame
from entities import *
from define import *
from field import Field
from counter import Counter

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Baseball Game")
    clock = pygame.time.Clock()

    field = Field()
    fielders = Fielders(field)
    # batter = RightBatter(field.base_home_and_line.x - 30, field.base_home_and_line.y - 10)
    batter = LeftBatter(field.base_home_and_line.x + 30, field.base_home_and_line.y - 10)
    ball = Ball(fielders.pitcher.x, fielders.pitcher.y)
    counter = Counter()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # プレイヤーの入力処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            batter.rotate_left()
        else:
            batter.rotate_right()

        # 野球場の描画
        field.draw(screen)
        ball.move(counter, fielders)
        ball.draw(screen)
        fielders.draw(screen)
        batter.draw(screen)

        counter.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()