import pygame
import math

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 色
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# 初期化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 打者の位置とバットのパラメータ
batter_x = SCREEN_WIDTH // 2
batter_y = SCREEN_HEIGHT // 2
bat_length = 100
bat_width = 10
bat_angle = 0

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面を黒でクリア
    screen.fill(BLACK)

    # 青い円を描画
    pygame.draw.circle(screen, BLUE, (batter_x, batter_y), 50)

    # バットを描画
    bat_start_x = batter_x + math.cos(math.radians(bat_angle)) * 50
    bat_start_y = batter_y - math.sin(math.radians(bat_angle)) * 50
    bat_end_x = bat_start_x + math.cos(math.radians(bat_angle)) * bat_length
    bat_end_y = bat_start_y - math.sin(math.radians(bat_angle)) * bat_length
    pygame.draw.line(screen, WHITE, (bat_start_x, bat_start_y), (bat_end_x, bat_end_y), bat_width)

    # バットの角度を更新
    bat_angle += 1

    # 画面を更新
    pygame.display.flip()
    clock.tick(60)

# 終了
pygame.quit()
