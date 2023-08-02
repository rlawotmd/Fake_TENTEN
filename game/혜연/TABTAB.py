import turtle as t
import random
import pygame
import time

def count_clicks_within_time_limit(time_limit):
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    click_count = 0
    start_time = time.time()

    while time.time() - start_time < time_limit:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_count += 1


        pygame.display.flip()

    pygame.quit()
    return click_count

if __name__ == "__main__":
    time_limit_seconds = 10

    print(f"터치 횟수 계산 중... (제한 시간: {time_limit_seconds}초)")
    click_count_result = count_clicks_within_time_limit(time_limit_seconds)
    #print(f"{time_count_result}")


#터치 횟수 안 뜸
#time_count_result 변수 쓰임 찾기
