import pygame
import sys

# 画面のサイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BASE_WIDTH = 16
BASE_HEIGHT = 16

# 色の定義
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BROWN = (139, 69, 19)

class Base():
    def __init__(self, x, y, width=BASE_WIDTH, height=BASE_HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dirt_width = width * 4
        self.dirt_height = height * 4

    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        pygame.draw.polygon(screen, dirt_color, [(self.x - self.dirt_width//2, self.y), # 左
                                            (self.x, self.y + self.dirt_height//2), # 下
                                            (self.x + self.dirt_width//2, self.y), # 右
                                            (self.x, self.y - self.dirt_height//2)]) # 上
        pygame.draw.polygon(screen, color, [(self.x - self.width//2, self.y), # 左
                                            (self.x, self.y + self.height//2), # 下
                                            (self.x + self.width//2, self.y), # 右
                                            (self.x, self.y - self.height//2)]) # 上
        
class HomeBase(Base):
    def __init__(self, x, y, width=BASE_WIDTH, height=BASE_HEIGHT):
        super().__init__(x, y, width, height)
        self.dirt_width = width * 8
        self.dirt_height = height * 8
        
    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        pygame.draw.ellipse(screen, dirt_color, (self.x - self.dirt_width//2, self.y - self.dirt_height//2, self.dirt_width, self.dirt_height))
        pygame.draw.polygon(screen, color, [(self.x - self.width//2, self.y - self.height), # 左上
                                            (self.x - self.width//2, self.y - self.height//2), # 左下
                                            (self.x, self.y), # 下
                                            (self.x + self.width//2, self.y - self.height//2), # 右下
                                            (self.x + self.width//2, self.y - self.height)]) # 右上
        
class PicherMound(Base):
    def __init__(self, x, y, width=BASE_WIDTH, height=BASE_HEIGHT//4):
        super().__init__(x, y, width, height)
        self.dirt_height = height * 16

    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        pygame.draw.ellipse(screen, dirt_color, (self.x - self.dirt_width//2, self.y - self.dirt_height//2, self.dirt_width, self.dirt_height))
        pygame.draw.rect(screen, color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))

class Field():
    def __init__(self):
        self.bias = SCREEN_HEIGHT // 6
        self.picher_mound = PicherMound(SCREEN_WIDTH // 2, self.bias + SCREEN_HEIGHT // 3)
        self.base_home = HomeBase(SCREEN_WIDTH // 2, self.bias + SCREEN_HEIGHT - SCREEN_HEIGHT // 3)
        self.base_first = Base(SCREEN_WIDTH - SCREEN_WIDTH // 4, self.bias +  SCREEN_HEIGHT // 3 - BASE_HEIGHT // 2)
        self.base_second = Base(SCREEN_WIDTH // 2, self.bias - BASE_HEIGHT // 2)
        self.base_third = Base(SCREEN_WIDTH // 4, self.bias +  SCREEN_HEIGHT // 3 - BASE_HEIGHT // 2)

    def draw(self, screen):
        screen.fill(GREEN) # 背景色の描画
        
        self.picher_mound.draw(screen) # ピッチャーマウンドの描画
        self.base_home.draw(screen) # ホームベースの描画
        self.base_first.draw(screen) # 一塁ベースの描画
        self.base_second.draw(screen) # 二塁ベースの描画
        self.base_third.draw(screen) # 三塁ベースの描画
        
        # ベースラインの描画
        pygame.draw.line(screen, WHITE, (self.base_home.x, self.base_home.y), (0, self.bias), width=3)
        pygame.draw.line(screen, WHITE, (self.base_home.x, self.base_home.y), (SCREEN_WIDTH, self.bias), width=3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Baseball Game")
    clock = pygame.time.Clock()

    field = Field()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 野球場の描画
        field.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()