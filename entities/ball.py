import random
import pygame
from define import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_COLOR

class Ball():
    def __init__(self, init_x, init_y, radius=4):
        self.init_x = init_x
        self.init_y = init_y
        self.radius = radius
        self.reset()
        self.alive = False

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.dx = random.random() * 0.3 - 0.15
        self.dy = random.random() * 1.5 + 1.5
        self.alive = True
        self.dead_count = random.randint(60, 120)

    def move(self, counter, catcher, batter) -> bool:
        self.x += self.dx
        self.y += self.dy
        if self.alive:
            # キャッチャーが捕球したらストライク
            if catcher.y < self.y and catcher.x-catcher.radius//2 < self.x < catcher.x+catcher.radius//2:
                self.alive = False
                batter.hit = False
                catcher.reset()
                counter.strike(batter)
            # フェアゾーンの画面外ならヒット
            elif self.y < 0 or (self.x < 0 and self.y < SCREEN_HEIGHT // 6) or (self.x > SCREEN_WIDTH and self.y < SCREEN_HEIGHT // 6):
                self.alive = False
                batter.hit = False
                catcher.reset()
                counter.reset()
            # ファウルゾーンの画面外ならファウル
            elif SCREEN_HEIGHT < self.y or self.x < 0 or SCREEN_WIDTH < self.x:
                self.alive = False
                batter.hit = False
                catcher.reset()
                counter.foul()
                
        else:
            self.dead_count -= 1
            if self.dead_count == 0:
                self.reset()
        return False
    
    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)