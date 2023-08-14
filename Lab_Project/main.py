import random
import tkinter as tk
from tkinter import *
import subprocess
import webbrowser

#게임 종류
random_wheel = "./game/준구/python/test.py" # 준구 - 돌림판
updown = "./game/준구/python/숫자맞추기.py" # 준구 - 숫자맞추기
Whack_a_Mole = "C:/Users/rhs97/Documents/tenten/Fake_TENTEN/game/사눅/두더지잡기/두더지 잡기.html" # 사눅 - 두더지잡기 #현재 절대경로로 실행해야 실행이 됨 상대경로로 할 수 있는지 찾기
Tic_Tac_Toe = "./game/사눅/tic tac toe with ai 2.py" # 사눅 - 틱택토
R_S_P = "./game/혜연/R.S.P.py" # 혜연 - 가위바위보
TabTab = "./game/혜연/TABTAB.py"# 혜연 - 탭탭 존나게 갈겨


window = tk.Tk()

#title
window.title("FAKE_TENTEN") 

#창 너비 ( x 높이 + x좌표 + y좌표 )
window.geometry("800x600") 

#창 크기 조절 가능 여부
window.resizable(False, False)

#이미지 리사이즈 함수



#뒷배경, 로고 이미지 작업
background = PhotoImage(file = "./main_image/bg_800-600.png")
logo = PhotoImage(file = "./main_image/건전.png")
logo2 = PhotoImage(file = "./main_image/logo.png")

L_background = tk.Label(window, image = background, width = 800, height = 600)
L_background.place(x = 0, y = 0)
L_logo = tk.Label(window, image = logo, width = 296, height = 71,bg='#00195c')
L_logo.place(x = 250, y = 20)
L_logo2 = tk.Label(window, image = logo2, width = 296, height = 71)
L_logo2.place(x = 250, y = 100)


rkdnlqkdnlqh = PhotoImage(file = "./main_image/가위바위보.png")
xlrxorxh = PhotoImage(file = "./main_image/틱택토.png")
enejwlwkqrl = PhotoImage(file = "./main_image/두더지잡기.png")
ehfflavks = PhotoImage(file = "./main_image/돌림판.png")
djqekdns = PhotoImage(file = "./main_image/업다운.png")
xoqxoq = PhotoImage(file = "./main_image/탭탭.png")
godqhrqjxms = PhotoImage(file = "./main_image/행복.png")
gustodtkfrl = PhotoImage(file = "./main_image/현생.png")




#게임 호출 함수
    
def call_R_S_O():
    subprocess.call(["python", R_S_P])
    #1 가위바위보

def call_Tic_Tac_Toe():
    subprocess.call(["python", Tic_Tac_Toe])
    #2 틱택토

def call_Whack_A_Mole():
    webbrowser.open(Whack_a_Mole)
    #3 두더지잡기

def call_random_wheel():
    subprocess.call(["python", random_wheel])
    #4 돌림판

def call_Up_Down():
    subprocess.call(["python", updown])
    #5 업다운

def call_Tap_Tap():
    subprocess.call(["python", TabTab])
    #6 탭탭


#랜덤 게임 호출 함수
def call_random_game():
    randomnumber =  random.randint(1,6)
    if(randomnumber == 1):
        call_R_S_O()#1
    elif(randomnumber ==2):
        call_Tic_Tac_Toe()#2
    elif(randomnumber ==3):
        call_Whack_A_Mole()#3
    elif(randomnumber ==4):
        call_random_wheel()#4
    elif(randomnumber ==5):
        call_Up_Down()#5
    elif(randomnumber ==6):
        call_Tap_Tap()#6
    
#게임 종료버튼 함수
def quit():
    window.destroy()
    window.quit()
    exit()


#게임 실행하는 버튼 생성
button = tk.Button(window, image = rkdnlqkdnlqh, text="가위바위보 실행", command = call_R_S_O, width = 300, height = 75)
button.place(x = 100, y = 190)

button = tk.Button(window, image = xlrxorxh, text="틱택토 실행", command = call_Tic_Tac_Toe, width = 300, height = 75)
button.place(x = 410, y = 190)

button = tk.Button(window, image = enejwlwkqrl, text="두더지잡기 실행", command = call_Whack_A_Mole, width = 300, height = 75)
button.place(x = 100, y = 280)

button = tk.Button(window, image = ehfflavks, text="돌림판 실행", command = call_random_wheel, width = 300, height = 75)
button.place(x = 410, y = 280)

button = tk.Button(window, image = djqekdns, text="업다운 실행", command = call_Up_Down, width = 300, height = 75)
button.place(x = 100, y = 370)

button = tk.Button(window, image = xoqxoq, text="탭탭 실행", command = call_Tap_Tap, width = 300, height = 75)
button.place(x = 410, y = 370)

button = tk.Button(window, image = godqhrqjxms, text="행복 버튼 실행", command = call_random_game, width = 300, height = 75)
button.place(x = 100, y = 460)

button = tk.Button(window, image = gustodtkfrl, text="현생살기 실행", command = quit, width = 300, height = 75)
button.place(x = 410, y = 460)


window.mainloop() #윈도우가 종료될 때까지 실행




