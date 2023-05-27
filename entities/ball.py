import random
import pygame
from define import BALL_COLOR

class Ball():
    def __init__(self, init_x, init_y, radius=4):
        self.init_x = init_x
        self.init_y = init_y
        self.radius = radius
        self.reset()

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.dx = random.random() * 0.3 - 0.15
        self.dy = random.random() * 1.5 + 1.5
        self.alive = True
        self.dead_count = random.randint(60, 120)

    def move(self, counter, fielders):
        self.x += self.dx
        self.y += self.dy
        if self.alive:
            if self.y > fielders.catcher.y:
                self.alive = False
                counter.strike()
        else:
            self.dead_count -= 1
            if self.dead_count == 0:
                self.reset()
    
    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)