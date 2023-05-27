import pygame
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
        self.width = 32
        self.height = 4

    def draw(self, screen):
        super().draw(screen, color=BLUE)
        pygame.draw.rect(screen, LIGHT_BROWN, (self.x + self.radius, self.y - self.height//2, self.width, self.height))

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