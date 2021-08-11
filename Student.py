# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 01:03:11 2021

@author: yourname
"""
import pygame


# 遊戲主要運行的流程
def main():
    # 設定運行狀態
    running = True
    while running:
        # 使用了pygame.event.get()來處理所有的事件
        for event in pygame.event.get():
            # 當按下視窗的 X 結束遊戲運行
            if event.type == pygame.QUIT:
                running = False
            # 首頁
            elif state == 0:
                welcome_screen()
        #         handle_welcome(event)
        #     # 遊玩中
        #     elif state == 1:
        #         handle_play(event)
        #     # 遊戲結束
        #     elif state == 2:
        #         handle_end(event)

        # # 遊玩中繪製遊戲畫面
        # if state == 1:
        #     play_screen()
        # # 結束時繪製結束畫面
        # if state == 2:
        #     end_screen()

        # 設定每秒至少 update 30 次 (對這個 while loop) 表示每秒最多應通過30幀
        # clock.tick(30)

        # 更新畫面
        pygame.display.update()

    # 當視窗關閉時 (running = false), 關閉視窗
    pygame.quit()

# 執行遊戲主要運行流程
main()

