import pygame
import math
from define import RED, BLUE, LIGHT_BROWN

class Player():
    def __init__(self, x, y, radius=6):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen, color=RED):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

class Batter(Player):
    def __init__(self, x, y, radius=6):
        super().__init__(x, y, radius)
        self.bat_width = 4
        self.bat_length = 36
        self.angle = -135

    def rotate_right(self):
        if self.angle > -135:
            self.angle -= 12
    
    def rotate_left(self):
        if self.angle < 135:
            self.angle += 6

    def draw(self, screen):
        bat_end_x = self.x + self.bat_length * math.cos(math.radians(self.angle))
        bat_end_y = self.y + self.bat_length * math.sin(math.radians(self.angle))
        pygame.draw.line(screen, LIGHT_BROWN, (self.x, self.y), (bat_end_x, bat_end_y), self.bat_width)
        super().draw(screen, color=BLUE)
        

# 守備プレイヤークラス
class Fielders():
    def __init__(self, field):
        self.pitcher = Player(field.picher_mound.x, field.picher_mound.y + 4)
        self.catcher = Player(field.base_home_and_line.x, field.base_home_and_line.y + 30)
        self.first = Player(field.base_first.x, field.base_first.y - 50)
        self.second = Player(field.base_second.x + 100, field.base_second.y)
        self.short = Player(field.base_second.x - 100, field.base_second.y)
        self.third = Player(field.base_third.x, field.base_third.y - 50)

    def draw(self, screen):
        self.pitcher.draw(screen)
        self.catcher.draw(screen)
        self.first.draw(screen)
        self.second.draw(screen)
        self.short.draw(screen)
        self.third.draw(screen)