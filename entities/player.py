import pygame
import random
import math
from define import RED, BLUE, LIGHT_BROWN

class Player():
    def __init__(self, init_x, init_y, radius=6):
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

class RightBatter(Player):
    def __init__(self, x, y, radius=6):
        super().__init__(x, y, radius)
        self.bat_width = 6
        self.bat_length = 28
        self.angle = -135
        self.hit = False
        self.is_change = False

    def rotate_right(self):
        if self.angle > -135:
            self.angle -= 12
    
    def rotate_left(self):
        if self.angle < 135:
            self.angle += 6

    def draw(self, screen):
        pygame.draw.line(screen, LIGHT_BROWN, (self.x, self.y), (self.bat_end_x, self.bat_end_y), self.bat_width)
        super().draw(screen, color=BLUE)

    def check_collision(self, ball):
        # バットの先端の座標を計算
        self.bat_end_x = self.x + self.bat_length * math.cos(math.radians(self.angle))
        self.bat_end_y = self.y + self.bat_length * math.sin(math.radians(self.angle))
        # バットの線分(self.x, self.y), (self.bat_end_x, self.bat_end_y)とボールの中心点(ball.x, ball.y)との距離を計算
        distance = abs((self.bat_end_y - self.y) * ball.x - (self.bat_end_x - self.x) * ball.y + self.bat_end_x * self.y - self.bat_end_y * self.x) / math.sqrt((self.bat_end_y - self.y)**2 + (self.bat_end_x - self.x)**2)
        # バットの線分とボールの中心点との距離がバットの半径とボールの半径の和より小さい場合かつボールがバットの線分の上にある場合はヒットとする
        if distance < ball.radius + self.bat_width / 2 and min(self.x, self.bat_end_x) < ball.x < max(self.x, self.bat_end_x) and min(self.y, self.bat_end_y) < ball.y < max(self.y, self.bat_end_y) and not self.hit:
            # バットの角度に応じてボールの反射角度を計算
            speed = random.random() * 4 + 4
            ball.dx = speed * math.sin(math.radians(self.angle))
            ball.dy = -speed * math.cos(math.radians(self.angle))
            self.hit = True

class LeftBatter(RightBatter):
    def __init__(self, x, y, radius=6):
        super().__init__(x, y, radius)
        self.bat_length *= -1
        self.angle *= -1

    def rotate_right(self):
        if self.angle < 135:
            self.angle += 12
    
    def rotate_left(self):
        if self.angle > -135:
            self.angle -= 6

def create_batter(home_x, home_y):
    if random.random() < 0.5:
        return RightBatter(home_x - 24, home_y -8)
    else:
        return LeftBatter(home_x + 24, home_y -8)       
