#화면에 가위 바위 보 띄워놓고
#컴퓨터도 가위바위보 중 하나 고르게 하
#이기면 3점 비기면 1점 지면 0점 
#제한시간 10초  


import time 
import random

#플레이어에게 입력받기 
#(가위 = 0, 바위 =1, 보=2)
player_choices = ['가위', '바위', '보']

def get_choice():
    while True:
        a = input('가위 바위 보 :')    
        if a in player_choices:
            return a
        print('잘못된 입력입니다. 다시 입력해주세요. ')

#플레이어가 가위바위보 중 하나 고르기
player_choice = get_choice()

#컴퓨터가 가위바위보 중 하나 고르기
computer_choice = random.choice(player_choices)

#승패판정
if player_choice == computer_choice:
    print('tie')
elif (player_choice == '가위' and computer_choice == '보') or \
     (player_choice == '바위' and computer_choice = '가위')or \
     (player_choice == '보' and computer_choice == '바위'):
    print('win')
    result.append('win')
else:
    print('lose')
    result.append('lose')

print(result)


