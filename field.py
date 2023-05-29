import pygame
from define import *

class Base(): # ベースクラス
    def __init__(self, x, y, width=BASE_WIDTH, height=BASE_HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dirt_width = width * 5
        self.dirt_height = height * 5

    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        # ベースの周りの土を描画
        pygame.draw.polygon(screen, dirt_color, [(self.x - self.dirt_width//2, self.y), # 左
                                            (self.x, self.y + self.dirt_height//2), # 下
                                            (self.x + self.dirt_width//2, self.y), # 右
                                            (self.x, self.y - self.dirt_height//2)]) # 上
        # ベースを白で描画
        pygame.draw.polygon(screen, color, [(self.x - self.width//2, self.y), # 左
                                            (self.x, self.y + self.height//2), # 下
                                            (self.x + self.width//2, self.y), # 右
                                            (self.x, self.y - self.height//2)]) # 上
        
class HomeBaseAndLine(Base): # ホームベースとベースラインクラス
    def __init__(self, x, y, width=HOME_BASE_WIDTH, height=HOME_BASE_HEIGHT):
        super().__init__(x, y, width, height)
        self.dirt_radius = width * 5
        self.batter_box_width = width * 2
        self.batter_box_height = height * 3
        
    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        # ベースの周りの土を描画
        pygame.draw.circle(screen, dirt_color, (self.x, self.y), self.dirt_radius)
        # ベースラインを白で描画
        pygame.draw.line(screen, color, (self.x, self.y), (SCREEN_WIDTH//2-500, 50+250), width=3)
        pygame.draw.line(screen, color, (self.x, self.y), (SCREEN_WIDTH//2+500, 50+250), width=3)

        # バッターボックスを土色で塗りつぶす
        pygame.draw.rect(screen, dirt_color, (self.x - self.width - self.batter_box_width, 
                                              self.y - self.batter_box_height//2 - self.height//2,
                                              self.batter_box_width * 3,
                                              self.batter_box_height)) 
        
        # バッターボックスの枠を白で描画
        pygame.draw.rect(screen, color, (self.x - self.width - self.batter_box_width, 
                                         self.y - self.batter_box_height//2 - self.height//2, 
                                         self.batter_box_width, 
                                         self.batter_box_height), width=2) # 左のバッターボックス
        pygame.draw.rect(screen, color, (self.x + self.width,
                                         self.y - self.batter_box_height//2 - self.height//2,
                                         self.batter_box_width,
                                         self.batter_box_height), width=2) # 右のバッターボックス
        
        # ホームベースを白で描画
        self.left = self.x - self.width//2
        self.right = self.x + self.width//2
        self.top = self.y - self.height
        self.center = self.y - self.height//2
        pygame.draw.polygon(screen, color, [(self.left, self.top), 
                                            (self.left, self.center), 
                                            (self.x, self.y), 
                                            (self.right, self.center), 
                                            (self.right, self.top)])
        
class PitcherMound(Base): # ピッチャーマウンドクラス
    def __init__(self, x, y, width=BASE_WIDTH, height=BASE_HEIGHT//4):
        super().__init__(x, y, width, height)
        self.dirt_radius = height * 8 # マウンドの半径

    def draw(self, screen, color=WHITE, dirt_color=BROWN):
        pygame.draw.circle(screen, dirt_color, (self.x, self.y), self.dirt_radius) # マウンドの土を描画
        pygame.draw.rect(screen, color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height)) # ピッチャープレートを白で描画

class Wall():
    def __init__(self, left_x, left_y, right_x, right_y, width=5):
        self.width = width
        self.left_x = left_x
        self.left_y = left_y
        self.right_x = right_x
        self.right_y = right_y

    def draw(self, screen):
        pygame.draw.line(screen, BLUE, (self.left_x, self.left_y), # 左
                                        (self.right_x, self.right_y), # 右
                                        width=self.width) # 壁の太さ

class Field(): # フィールドクラス
    def __init__(self):
        bias = 100
        self.data = {
            'left_wall': Wall(SCREEN_WIDTH//2-550, 350, SCREEN_WIDTH//2-CENTER_WIDTH, CENTER_Y), # レフトの壁を生成
            'center_wall': Wall(SCREEN_WIDTH//2-CENTER_WIDTH, CENTER_Y, SCREEN_WIDTH//2+CENTER_WIDTH, CENTER_Y), # センターの壁を生成
            'right_wall': Wall(SCREEN_WIDTH//2+CENTER_WIDTH, CENTER_Y, SCREEN_WIDTH//2+550, 350), # ライトの壁を生成
            'left_top_wall': Wall(SCREEN_WIDTH//2-550, 350, SCREEN_WIDTH//2-400 ,500), # 左上の壁を生成
            'left_middle_wall': Wall(SCREEN_WIDTH//2-400, 500, SCREEN_WIDTH//2-400, 700), # 左中の壁を生成
            'left_bottom_wall': Wall(SCREEN_WIDTH//2-400, 700, SCREEN_WIDTH//2-200, 900), # 左下の壁を生成
            'right_top_wall': Wall(SCREEN_WIDTH//2+400 ,500, SCREEN_WIDTH//2+550, 350), # 右上の壁を生成
            'right_middle_wall': Wall(SCREEN_WIDTH//2+400, 700, SCREEN_WIDTH//2+400, 500), # 右中の壁を生成
            'right_bottom_wall': Wall(SCREEN_WIDTH//2+200, 900, SCREEN_WIDTH//2+400, 700), # 右下の壁を生成
            'bottom_wall': Wall(SCREEN_WIDTH//2-200, 900, SCREEN_WIDTH//2+200, 900), # 下の壁を生成
            'pitcher_mound': PitcherMound(SCREEN_WIDTH // 2, SCREEN_HEIGHT - bias - 200), # ピッチャーマウンドを生成
            'base_home': HomeBaseAndLine(SCREEN_WIDTH // 2, SCREEN_HEIGHT - bias), # ホームベースとベースラインを生成
            'base_first': Base(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - bias - 200), # 一塁ベースを生成
            'base_second': Base(SCREEN_WIDTH // 2, SCREEN_HEIGHT - bias - 400), # 二塁ベースを生成
            'base_third': Base(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - bias - 200) # 三塁ベースを生成
        }

    def __getitem__(self, key):
        return self.data[key]

    def draw(self, screen):
        screen.fill(GREEN) # 背景色の描画
        for base in self.data.values():
            base.draw(screen)