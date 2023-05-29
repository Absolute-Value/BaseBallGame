import pygame
from entities import *
from define import *
from field import Field
from counter import SBOCounter

def main():
    pygame.init() # pygameを初期化
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 画面を作成
    pygame.display.set_caption("Baseball Game") # タイトルバーに表示する文字
    clock = pygame.time.Clock() # フレームレートを管理するためのClockオブジェクトを生成

    field = Field() # フィールドを生成
    fielders = Fielders(field) # 野手を生成
    batter = create_batter(field.base_home.x, field.base_home.y) # バッターを生成
    ball = Ball(fielders['pitcher'].x, fielders['pitcher'].y) # ボールを生成
    sbo_counter = SBOCounter() # SBOカウンターを生成

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 閉じるボタンが押されたら終了
                pygame.quit()

        keys = pygame.key.get_pressed() # 押されているキーをチェック
        if keys[pygame.K_ESCAPE]: # ESCキーが押されたら終了
            pygame.quit()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            batter.move(dx=-1)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            batter.move(dx=1)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            batter.move(dy=-1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            batter.move(dy=1)
        if keys[pygame.K_n]: # Nキーが押されている場合
            batter.swing() # バットをスイング
        else: # Nキーが押されていない場合
            batter.swing_back() # バットを元の位置に戻す

        ball.move(field.base_home, sbo_counter, fielders, batter)
        if ball.alive and not batter.hit: fielders['catcher'].move(dx=ball.dx)
        if batter.is_change:
            batter = create_batter(field.base_home.x, field.base_home.y)

        batter.check_collision(ball) # バッターとボールの衝突判定

        field.draw(screen) # 野球場の描画
        ball.draw(screen) # ボールの描画
        fielders.draw(screen) # 野手の描画
        batter.draw(screen) # バッターの描画
        sbo_counter.draw(screen) # SBOカウンターの描画

        pygame.display.update() # 画面更新
        clock.tick(60) # 60fps

if __name__ == '__main__':
    main()