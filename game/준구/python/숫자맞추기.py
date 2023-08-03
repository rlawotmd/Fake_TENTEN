import random as rd

num = rd.randint(1,100)
n = 0
bool = False
answer = int(input('1~99사이의 정수를 입력해주세요: '))

for i in range(7):
    if answer > num:
        print('DOWN')
        answer = int(input('1~99사이의 정수를 입력하세요: '))
        n = n+1

    elif answer < num:
        print('UP')
        answer = int(input('1~99사이의 정수를 입력하세요: '))
        n = n+1

    else:
        n = n+1
        print(n, '번만에 맞추셨습니다. 정답은', num, '였습니다.')
        bool = True
        break

if bool == False:
    print('아쉽게도 못맞췄습니다. 다음 기회에~~')
