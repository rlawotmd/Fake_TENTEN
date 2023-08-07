import random as rd

num = rd.randint(1,100)
n = 0
bool = False


for i in range(7):
    answer = int(input('1~99사이의 정수를 입력해주세요: '))
    if 6-n == 0:
        print('끝')
        break
    print(6-n,'번남았습니다.')
    if answer > num:
        print('DOWN')
        n = n+1

    elif answer < num:
        print('UP')
        n = n+1

    else:
        n = n+1
        print(n, '번만에 맞추셨습니다. 정답은', num, '였습니다.')
        bool = True
        break

if bool == False:
    print('아쉽게도 못맞췄습니다.정답은',num , '였습니다.')

print('<아무키나 눌러서 게임종료.>')
input()