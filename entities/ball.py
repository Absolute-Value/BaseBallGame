import random
import math
import pygame
from define import *

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
        self.hold_time = FIELDER_HOLD_TIME

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
                        self.dx, self.dy = 0, 0
                        # もしバッターがファーストに到達していたらセーフ
                        batter_distance = math.sqrt((batter.x - self.field['base_first'].x)**2 + (batter.y - self.field['base_first'].y)**2)
                        if batter_distance >= 1:
                            sbo_counter.out()
                        batter.is_change = True
                        reset()
                        sbo_counter.reset()
                    else:
                        if self.hold_time == 0:
                            # ファーストに送球
                            speed = 4
                            dx = self.field['base_first'].x-5 - self.x
                            dy = self.field['base_first'].y - self.y
                            distance = math.sqrt(dx**2 + dy**2)
                            if distance > 1:
                                self.dx = (dx / distance) * speed
                                self.dy = (dy / distance) * speed
                        else:
                            self.hold_time -= 1
                            self.dx, self.dy = 0, 0
                    return
            # センターの壁に当たったら反射
            if self.y - self.radius < CENTER_Y:
                self.y = CENTER_Y + self.radius
                self.dy = -self.dy * WALL_REBOUND
            elif self.y + self.radius > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT - self.radius
                self.dy = -self.dy * WALL_REBOUND
            # ライトの壁に当たったら反射（実装予定）
            elif self.y <= self.x - 800:
                self.dx = 0
                self.dy = 0
            # レフトの壁に当たったら反射（実装予定）
            elif self.y + self.x <= 400:
                self.dx = 0
                self.dy = 0
            # 右下の壁に当たったら（実装予定）
            elif self.y + self.x >= 1700:
                self.dx = 0
                self.dy = 0
            # 左下の壁に当たったら（実装予定）
            elif self.y >= self.x + 500:
                self.dx = 0
                self.dy = 0
            # ファウルゾーンに入ったらファウル（実装予定）
            #elif batter.is_hit:
                # reset()
                # sbo_counter.foul()
                
        else:
            self.dead_count -= 1
            if self.dead_count == 0:
                self.reset()
    
    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)