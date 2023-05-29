import pygame
import math
from define import RED, PLAYER_RADIUS

class Player():
    def __init__(self, init_x, init_y, radius=PLAYER_RADIUS):
        self.init_x = init_x
        self.init_y = init_y
        self.reset()
        self.radius = radius

    def reset(self):
        self.x, self.y = self.init_x, self.init_y
        self.dx, self.dy = 0, 0
        self.speed = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dx, self.dy = 0, 0
    
    def draw(self, screen, color=RED):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

class Fielder(Player):
    def __init__(self, field, init_x, init_y, radius=PLAYER_RADIUS):
        self.field = field
        super().__init__(init_x, init_y, radius)

    def move(self, ball, batter):
        if batter.is_hit: # バッターがヒットしたら
            if self.speed < 2:
                self.speed += 0.05
            # ボールに向かって移動
            dx = ball.x-5 - self.x
            dy = ball.y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 1:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed

class Catcher(Fielder): # キャッチャー
    def move(self, ball, batter):
        if ball.alive and not batter.is_hit:
            self.x += ball.dx

class First(Fielder): # 一塁手
    def move(self, ball, batter):
        if batter.is_hit: # バッターがヒットしたら
            if self.speed < 2:
                self.speed += 0.05
            # 一塁ベースに向かって移動
            dx = self.field['base_first'].x-5 - self.x
            dy = self.field['base_first'].y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 1:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed


class Fielders():
    def __init__(self, field):
        self.data = {
            'pitcher': Fielder(field, field['pitcher_mound'].x, field['pitcher_mound'].y + 4), # ピッチャーを生成
            'catcher': Catcher(field, field['base_home'].x, field['base_home'].y + 30), # キャッチャーを生成
            'first': First(field, field['base_first'].x, field['base_first'].y - 50), # 一塁手を生成
            'second': Fielder(field, field['base_second'].x + 120, field['base_second'].y + 10), # 二塁手を生成
            'short': Fielder(field, field['base_second'].x - 120, field['base_second'].y + 10), # 遊撃手を生成
            'third': Fielder(field, field['base_third'].x, field['base_third'].y - 50) # 三塁手を生成
        }

    def __getitem__(self, key):
        return self.data[key]
    
    def items(self):
        return self.data.items()
    
    def reset(self):
        for fielder in self.data.values():
            fielder.reset()

    def move(self, ball, batter):
        for fielder in self.data.values():
            fielder.move(ball, batter)
    
    def draw(self, screen):
        for fielder in self.data.values():
            fielder.draw(screen)