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

    def strike(self, batter):
        self.strike_num += 1
        if self.strike_num >= 3:
            self.out()
            batter.is_out = True

    def foul(self):
        if self.strike_num < 2:
            self.strike_num += 1

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
        sbo_list = [["S",self.strike_num,YELLOW],["B",self.ball_num,GREEN],["O",self.out_num,RED]]
        for i, (text, num, color) in enumerate(sbo_list):
            text = font.render(text,  True, WHITE)
            screen.blit(text, (self.x, self.y + i*self.height//3))
            for j in range(num):
                pygame.draw.circle(screen, color, (self.x + self.width//4 * (j+1), self.y + self.height//8 + self.height//3*i), self.height//12)