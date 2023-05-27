import random
import pygame
from define import BALL_COLOR

class Ball():
    def __init__(self, init_x, init_y, radius=4):
        self.init_x = init_x
        self.init_y = init_y
        self.x = init_x
        self.y = init_y
        self.dx = 0
        self.dy = random.random() + 1.5
        self.radius = radius

    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def draw(self, screen):
        pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)