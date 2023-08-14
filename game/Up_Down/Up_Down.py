import random as rd

num = rd.randint(1,100)
bool = False

for i in range(1, 8):
    answer = int(input('1~99사이의 정수를 입력해주세요: '))
    
    if answer > num:
        print('Down')
        print(7-i, '번 남았습니다.')
    elif answer < num:
        print('Up')
        print(7-i, '번 남았습니다.')
    elif answer == num:
        print(i, '번만에 맞추셨습니다. 정답은', num, '였습니다.')
        bool = True

if bool == False:
    print('아쉽게도 못맞췄습니다.정답은', num, '였습니다.')
    
print('<아무키나 눌러서 게임종료.>')
input()