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
