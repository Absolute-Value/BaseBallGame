import pygame
from define import RED, PLAYER_RADIUS

class Player():
    def __init__(self, init_x, init_y, radius=PLAYER_RADIUS):
        self.init_x = init_x
        self.init_y = init_y
        self.reset()
        self.radius = radius

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
    def draw(self, screen, color=RED):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

class Fielders():
    def __init__(self, field):
        self.data = {
            'pitcher': Player(field.picher_mound.x, field.picher_mound.y + 4), # ピッチャーを生成
            'catcher': Player(field.base_home.x, field.base_home.y + 30), # キャッチャーを生成
            'first': Player(field.base_first.x, field.base_first.y - 50), # 一塁手を生成
            'second': Player(field.base_second.x + 120, field.base_second.y + 10), # 二塁手を生成
            'short': Player(field.base_second.x - 120, field.base_second.y + 10), # 遊撃手を生成
            'third': Player(field.base_third.x, field.base_third.y - 50) # 三塁手を生成
        }

    def __getitem__(self, key):
        return self.data[key]
    
    def items(self):
        return self.data.items()
    
    def reset(self):
        for fielder in self.data.values():
            fielder.reset()
    
    def draw(self, screen):
        for fielder in self.data.values():
            fielder.draw(screen)