import pygame
from define import *

# 野球のスコアを管理するクラス
class ScoreCounter():
    def __init__(self, team1="D", team2="C"):
        self.x = SCORE_COUNTER_X
        self.y = SCORE_COUNTER_Y
        self.width = SCORE_COUNTER_WIDTH
        self.height = SCORE_COUNTER_HEIGHT
        self.inning = 1
        self.turn = 0
        self.turn_name = {0:"表", 1:"裏"}
        self.team_names = [team1, team2]
        self.scores = [0, 0]

    def draw(self, screen, font_size=FONT_SIZE):
        font = pygame.font.Font(FONT_PATH, font_size)
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        score_list = [f"{self.inning} {self.turn_name[self.turn]}", 
                      f"{self.team_names[0]} {self.scores[0]}", 
                      f"{self.team_names[1]} {self.scores[1]}"]
        for i, text in enumerate(score_list):
            text = font.render(text, True, WHITE)
            screen.blit(text, (self.x+self.width//8, self.y + i*self.height//3))
        pygame.draw.rect(screen, RED, (self.x, self.y + self.height//3*(1+self.turn), self.width//8, self.height//3))

# バッターのSBOカウントを管理するクラス
class SBOCounter():
    def __init__(self):
        self.x = SBO_COUNTER_X
        self.y = SBO_COUNTER_Y
        self.width = SBO_COUNTER_WIDTH
        self.height = SBO_COUNTER_HEIGHT
        self.counts = {"S":0, "B":0, "O":0} # S means Strike, B means Ball, O means Out
        self.colors = {"S":YELLOW, "B":GREEN, "O":RED}
        self.score_counter = ScoreCounter()

    def strike(self, batter):
        self.counts["S"] += 1
        if self.counts["S"] >= 3:
            self.out()
            batter.is_change = True

    def foul(self):
        if self.counts["S"] < 2:
            self.counts["S"] += 1

    def ball(self):
        self.counts["B"] += 1
        if self.counts["B"] >= 4:
            self.reset()

    def out(self):
        self.counts["O"] += 1
        self.reset()
        if self.counts["O"] >= 3:
            self.counts["O"] = 0
            if self.score_counter.turn == 0:
                self.score_counter.turn = 1
            else:
                self.score_counter.turn = 0
                self.score_counter.inning += 1

    def reset(self):
        self.counts["S"] = 0
        self.counts["B"] = 0

    def draw(self, screen, font_size=FONT_SIZE):
        self.score_counter.draw(screen) # スコアカウンターの描画
        font = pygame.font.Font(FONT_PATH, font_size)
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        for i, (key, num) in enumerate(self.counts.items()):
            text = font.render(key, True, WHITE)
            screen.blit(text, (self.x, self.y + i*self.height//3))
            for j in range(num):
                pygame.draw.circle(screen, self.colors[key], (self.x + self.width//4 * (j+1), self.y + self.height//5 + self.height//3*i), self.height//10)
