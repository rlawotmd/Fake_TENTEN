import tkinter as tk
from tkinter import *
import subprocess
import webbrowser

#게임의 개수
MAX = 8

#게임 종류
python_turtle = "./Lab_Project/turtle_pen.py" # 예시용 터틀펜
random_wheel = "./game/준구/python/test.py" # 준구 - 돌림판
Whack_a_Mole = "./game/사눅/두더지잡기/두더지 잡기.html" # 사눅 - 두더지잡기
Tic_Tac_Toe = "./game/사눅/tic tac toe with ai 2.py" # 사눅 - 틱택토
R_S_P = "./game/혜연/R.S.P.py" # 혜연 - 가위바위보

window = tk.Tk()

#title
window.title("FAKE_TENTEN") 

#창 너비 ( x 높이 + x좌표 + y좌표 )
window.geometry("800x600+100+100") 

#창 크기 조절 가능 여부
window.resizable(False, False)



#이미지 삽입
logo = PhotoImage(file = "./image/sample_logo.png")
#원본 크기
ori_logo_width = logo.width()
ori_logo_height = logo.height()

#조정할 크기
new_logo_width = 300
new_logo_height = int(new_logo_width * ori_logo_height / ori_logo_width)

#이미지 크기 조정 / 메소드 사용
logo = logo.subsample(ori_logo_width // new_logo_width, ori_logo_height // new_logo_height)

#라벨 생성, 이미지 삽입
L_logo = tk.Label(window, image = logo, width = 400, height = 100) #
L_logo.place(x = 200, y = 25)


menu = PhotoImage(file = "./image/sample_menu.png")
ori_menu_width = menu.width()
ori_menu_height = menu.height()
new_menu_width = 300
new_menu_height = int(new_menu_width * ori_menu_height / ori_menu_width)
menu = menu.subsample(ori_menu_width // 300, ori_menu_height // 75) #ori_menu_width // new_menu_width, ori_menu_height // new_menu_height



#파이썬 게임 호출 함수
def call_turtle():
    subprocess.call(["python", python_turtle])
    
def call_Tic_Tac_Toe():
    subprocess.call(["python", Tic_Tac_Toe])

def call_random_wheel():
    subprocess.call(["python", random_wheel])


#게임 실행하는 버튼 생성
button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 50, y = 150)

button = tk.Button(window, image = menu, text="틱택토 실행", command = call_Tic_Tac_Toe, width = 340, height = 85)
button.place(x = 410, y = 150)

button = tk.Button(window, image = menu, text="돌려돌려 돌림판 실행", command = call_random_wheel, width = 340, height = 85)
button.place(x = 50, y = 255)

button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 410, y = 255)

button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 50, y = 360)

button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 410, y = 360)

button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 50, y = 465)

button = tk.Button(window, image = menu, text="터틀 실행", command = call_turtle, width = 340, height = 85)
button.place(x = 410, y = 465)


window.mainloop() #윈도우가 종료될 때까지 실행




