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
    def __init__(self):
        pass