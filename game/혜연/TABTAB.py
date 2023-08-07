import turtle as t
import pygame
from turtle import back
import time

pygame.init()

RED = (255, 0,0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

'''background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("text")

myFont = pygame.font.SysFont(None, 50)'''


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.fill((0,0,0))
    myText = myFont.render("10sec", True, WHITE)
    background.blit(myText, (100,100))
    pygame.display.update()


def count_clicks_within_time_limit(time_limit):
    screen_width = 500
    screen_height = 700 

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("TOTAL SCORE")

    click_count = 0
    start_time = time.time()

    while time.time() - start_time < time_limit:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_count += 1


        pygame.display.flip()
  
    #clickScore = 0
    tabtab_font = pygame.font.SysFont("arialrounded", 40, True, False)
    text_clickScore = tabtab_font.render("TOTAL SCORE", True, WHITE)
    text_Rect = text_clickScore.get_rect() 
    text_Rect.centerx = round(screen_width /2)
    text_Rect.y = 50
    #클릭 기록 창이 꺼져야 게임 결과창이 뜨나
    #터틀로 텍스트(


    '''screen.blit(text_clickScore, text_Rect)

    text_Total = tabtab_font.render("Total Score", True, WHITE)
    screen.blit(text_Total, [100, 400])'''

    pygame.display.flip()

    time.sleep(5)
    pygame.quit()
    return click_count

if __name__ == "__main__":
    time_limit_seconds = 10

    print(f"터치 횟수 계산 중... (제한 시간: {time_limit_seconds}초)")
    click_count_result = count_clicks_within_time_limit(time_limit_seconds)
    print(f"{click_count_result}")
