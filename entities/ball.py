import random
import math
import pygame
from define import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_COLOR, BALL_RADIUS

class Ball():
    def __init__(self, field, init_x, init_y, radius=BALL_RADIUS):
        self.field = field
        self.init_x = init_x
        self.init_y = init_y
        self.radius = radius
        self.reset()
        self.alive = False

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.speed = random.random() * 3 + 3.5
        self.angle = random.random() * 10 - 5
        self.dx = self.speed * math.sin(math.radians(self.angle))
        self.dy = self.speed * math.cos(math.radians(self.angle))
        self.alive = True
        self.dead_count = random.randint(60, 120)
        self.is_strike = False
        self.is_swing = False

    def move(self, base_home, sbo_counter, fielders, batter):
        self.x += self.dx
        self.y += self.dy
        if self.alive:
            # スイングしたかの判定
            if (base_home.x - self.x)**2 + (base_home.y - self.y)**2 < (base_home.dirt_radius + self.radius)**2:
                if -45 < batter.angle < 45:
                    self.is_swing = True
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
                batter.reset()
                fielders.reset()
            # 野手が捕球した時
            for pos_name, fielder in fielders.items():
                if (fielder.x - self.x)**2 + (fielder.y - self.y)**2 <= (fielder.radius + self.radius)**2:
                    if pos_name == 'catcher' and not batter.is_hit: # からぶってキャッチャーが捕球した時
                        # ホームベースをかする、またはスイングしていたらストライク
                        if self.is_strike or self.is_swing:
                            sbo_counter.strike(batter)
                            reset()
                        else:
                            sbo_counter.ball()
                            reset()
                    elif pos_name == 'pitcher' and not batter.is_hit: # ピッチャーがボールを投げる前
                        continue
                    elif pos_name == 'first':
                        # もしバッターがファーストに到達していたらセーフ
                        if (batter.x - self.field['base_first'].x)**2 + (batter.y - self.field['base_first'].y)**2 <= (batter.radius + self.field['base_first'].width//2)**2:
                            reset()
                            sbo_counter.reset()
                            batter.is_change = True
                        else:
                            sbo_counter.out()
                    else:
                        # ファーストに送球
                        speed = 3
                        dx = self.field['base_first'].x - self.x
                        dy = self.field['base_first'].y - self.y
                        distance = math.sqrt(dx**2 + dy**2)
                        if distance > 1:
                            self.dx = (dx / distance) * speed
                            self.dy = (dy / distance) * speed
                    return
            # フェアゾーンの画面外ならヒット
            if self.y < 0 or (self.x < 0 and self.y < SCREEN_HEIGHT // 6) or (self.x > SCREEN_WIDTH and self.y < SCREEN_HEIGHT // 6):
                reset()
                sbo_counter.reset()
                batter.is_change = True
            # ファウルゾーンの画面外ならファウル
            elif SCREEN_HEIGHT < self.y or self.x < 0 or SCREEN_WIDTH < self.x:
                reset()
                sbo_counter.foul()
                
        else:
            self.dead_count -= 1
            if self.dead_count == 0:
                self.reset()
    
    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)