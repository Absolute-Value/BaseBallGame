import pygame
import sys
from define import *
from field import Field

class Ball():
    def __init__(self, init_x, init_y, radius=4):
        self.init_x = init_x
        self.init_y = init_y
        self.x = init_x
        self.y = init_y
        self.dx = 0
        self.dy = 2
        self.radius = radius

    def move_and_draw(self, screen):
        self.x += self.dx
        self.y += self.dy
        if self.y > SCREEN_HEIGHT:
            self.y = self.init_y
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Baseball Game")
    clock = pygame.time.Clock()

    field = Field()
    ball = Ball(field.picher_mound.x, field.picher_mound.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 野球場の描画
        field.draw(screen)
        ball.move_and_draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()