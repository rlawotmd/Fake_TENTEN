#화면에 가위 바위 보 띄워놓고
#컴퓨터도 가위바위보 중 하나 고르게 하
#이기면 3점 비기면 1점 지면 0점 
#제한시간 10초  

import turtle as t
import time 
import random


t.bgcolor("yellow")
t.title("가위바위보")
t.ht()
t.up()

rock_gif = "game/혜연/images/rock.gif"
scissor_gif = "game/혜연/images/scissor.gif" 
paper_gif = "game/혜연/images/paper.gif"
t.addshape(rock_gif)
t.addshape(scissor_gif)
t.addshape(paper_gif)

t.shape(rock_gif)

#플레이어에게 입력받기 
#(가위 = 0, 바위 =1, 보=2)
player_choices = ['가위', '바위', '보']

#화면에 가위바위보 뜨게 

def get_choice():
    while True:
        a = input('가위 바위 보 :')    
=======
time.set


    #플레이어에게 입력받기 
    #(가위 = 0, 바위 =1, 보=2)
player_choices = ['가위', '바위', '보']

def get_choice():
        a = input('가위 바위 보! :')     

        if a in player_choices:
            return a
        print('잘못된 입력입니다. 다시 입력해주세요. ')

#플레이어가 가위바위보 중 하나 고르기
player_choice = get_choice()

#컴퓨터가 가위바위보 중 하나 고르기
computer_choice = random.choice(player_choices)



print(result)

