import turtle as t
import time 
import random

t.up()
t.goto(0 , 300)
t.write("a : 가위  s : 바위  d : 보", False, "center", ("", 30) )

t.goto(0, -300)
t.write("*작동이 안될 시 한영키를 눌러주세요*", False, "center", ("", 30) )

def com_choice():
    rand_choice = random.randint(0, 2)
    com.shape(images[rand_choice])
    return com_list[rand_choice]

def result_print(user_c, com_c):
    global user_score, com_score
    if user_score >= 5:
        t.goto(0, -350)
        t.write("플레이어 승!", False, "center", ("", 80))
        time.sleep(5)
        t.bye()
    elif com_score >= 5:
        t.goto(0, -350)
        t.write("플레이어 패!", False, "center", ("", 80))
        time.sleep(5)
        t.bye()
    

    t.clear()
    t.goto(0, -100)
    if user_c == com_c:
        t.write("무승부", False, "center", ("", 50))
    elif win_case[user_c] == com_c:
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False, "center", ("", 50))
        t.write("승", False, "center", ("", 50))
    else:
        com_score += 1
        com_pen.clear()
        com_pen.write(com_score, False, "center", ("", 50))
        t.write("패", False, "center", ("", 50))

    
        


#컴퓨터 선택 - 랜덤
#승부 결과 판정
def rock():
    user.shape(rock_gif)
    com = com_choice()
    result_print("rock", com)

def scissor():
    user.shape(scissor_gif)
    com = com_choice()
    result_print("scissor", com)

def paper():
    user.shape(paper_gif)
    com = com_choice()
    result_print("paper", com)

t.bgcolor("YELLOW")
t.title("가위바위보")
t.ht()
t.up()

rock_gif = "game/R_S_P/rock.gif"
scissor_gif = "game/R_S_P/scissor.gif" 
paper_gif = "game/R_S_P/paper.gif"
t.addshape(rock_gif)
t.addshape(scissor_gif)
t.addshape(paper_gif)

images = [rock_gif, scissor_gif, paper_gif]
com_list = ["rock", "scissor", "paper"]
win_case = {"rock":"scissor", "scissor":"paper", "paper":"rock"}
user_score = 0
com_score = 0


#나
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-200, 200)
user.write("나", False, "center", ("", 50))
user.goto(-200, -100)
user.shape(rock_gif)

#컴퓨터
com = t.Turtle()
com.up()
com.speed(0)
com.goto(200, 200)
com.write("컴퓨터", False, "center", ("", 50))
com.goto(200, -100)
com.shape(rock_gif)

#나의 점수
user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-200, 100)
user_pen.write(user_score, False, "center", ("", 50))

#컴퓨터 점수
com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(200, 100)
com_pen.write(com_score, False, "center", ("", 50))


player = t.Turtle()
screen = player.getscreen()

screen.onkeypress(rock, "a") #유저 A 키
screen.onkeypress(scissor, "s") #유저 S 키
screen.onkeypress(paper, "d") #유저 D 키

screen.listen()
t.done()
