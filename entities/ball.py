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
        self.dx = random.random() * 0.5 - 0.25
        self.dy = random.random() * 3 + 2
        self.alive = True
        self.dead_count = random.randint(60, 120)
        self.is_strike = False

    def move(self, base_home, counter, catcher, batter):
        self.x += self.dx
        self.y += self.dy
        if self.alive:
            # ベースをかすったかのブロードフェーズ判定
            if self.x>base_home.left-self.radius and self.x<base_home.right+self.radius and self.y>base_home.top-self.radius and self.y<base_home.center+self.radius:
                # ベースをかすったかのナローフェーズ判定 (https://ftvoid.com/blog/post/300)
                condition_a = self.x>base_home.left and self.x<base_home.right and self.y>base_home.top-self.radius and self.y<base_home.center+self.radius
                condition_b = self.x>base_home.left-self.radius and self.x<base_home.right+self.radius and self.y>base_home.top and self.y<base_home.center
                condition_c = (base_home.left-self.x)**2+(base_home.top-self.y)**2<(self.radius)**2
                condition_d = (base_home.right-self.x)**2+(base_home.top-self.y)**2<(self.radius)**2
                condition_e = (base_home.right-self.x)**2+(base_home.center-self.y)**2<(self.radius)**2
                condition_f = (base_home.left-self.x)**2+(base_home.center-self.y)**2<(self.radius)**2
                if condition_a or condition_b or condition_c or condition_d or condition_e or condition_f:
                    self.is_strike = True
            def reset():
                self.alive = False
                self.is_strike = False
                batter.hit = False
                catcher.reset()
            # キャッチャーが捕球した時
            if (catcher.x - self.x)**2 + (catcher.y - self.y)**2 <= (catcher.radius + self.radius)**2:
                # ホームベースをかすっていたらストライク
                if self.is_strike:
                    counter.strike(batter)
                else:
                    counter.ball()
                reset()
            # フェアゾーンの画面外ならヒット
            elif self.y < 0 or (self.x < 0 and self.y < SCREEN_HEIGHT // 6) or (self.x > SCREEN_WIDTH and self.y < SCREEN_HEIGHT // 6):
                reset()
                counter.reset()
                batter.is_change = True
            # ファウルゾーンの画面外ならファウル
            elif SCREEN_HEIGHT < self.y or self.x < 0 or SCREEN_WIDTH < self.x:
                reset()
                counter.foul()
                
        else:
            self.dead_count -= 1
            if self.dead_count == 0:
                self.reset()
    
    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)