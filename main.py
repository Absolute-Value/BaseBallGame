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
    fielders = {
        'pitcher': Player(field.picher_mound.x, field.picher_mound.y + 4),
        'catcher': Player(field.base_home.x, field.base_home.y + 30),
        'first': Player(field.base_first.x, field.base_first.y - 50),
        'second': Player(field.base_second.x + 100, field.base_second.y),
        'short': Player(field.base_second.x - 100, field.base_second.y),
        'third': Player(field.base_third.x, field.base_third.y - 50)
    }
    batter = create_batter(field.base_home.x, field.base_home.y)
    ball = Ball(fielders['pitcher'].x, fielders['pitcher'].y)
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
        ball.move(field.base_home, counter, fielders, batter)
        if ball.alive and not batter.hit: fielders['catcher'].move(dx=ball.dx)
        if batter.is_change:
            batter = create_batter(field.base_home.x, field.base_home.y)

        batter.check_collision(ball)

        field.draw(screen)
        ball.draw(screen)
        fielders['catcher'].draw(screen)
        for fielder in fielders.values():
            fielder.draw(screen)
        batter.draw(screen)

        counter.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()