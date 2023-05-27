import pygame
from define import *

class Counter():
    def __init__(self, x=SCREEN_WIDTH-SCREEN_WIDTH//8, y=SCREEN_HEIGHT-SCREEN_HEIGHT//4):
        self.x = x
        self.y = y
        self.width = SCREEN_WIDTH//8
        self.height = SCREEN_HEIGHT//4
        self.strike_num = 0
        self.ball_num = 0
        self.out_num = 0

    def strike(self):
        self.strike_num += 1
        if self.strike_num >= 3:
            self.out()

    def ball(self):
        self.ball_num += 1
        if self.ball_num >= 4:
            self.reset()

    def out(self):
        self.out_num += 1
        self.reset()
        if self.out_num >= 3:
            self.out_num = 0

    def reset(self):
        self.strike_num = 0
        self.ball_num = 0

    def draw(self, screen, font_size=FONT_SIZE):
        font = pygame.font.Font(FONT_PATH, font_size)
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        for i, text in enumerate([f"S:{self.strike_num}",f"B:{self.ball_num}",f"O:{self.out_num}"]):
            text = font.render(text,  True, WHITE)
            screen.blit(text, (self.x, self.y + i*self.height//3))