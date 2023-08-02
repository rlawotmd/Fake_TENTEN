import time
import threading
import os
import platform

board = [" " for _ in range(9)]

player = 'X'
ai = 'O'

time_limit = 20
time_up = False

def print_timer(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"Time left: {minutes:02d}:{seconds:02d}")

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def display_board():
    clear_screen()
    print("  ")
    print("╔═══╦═══╦═══╗")
    for i in range(0, 9, 3):
        print("║", board[i], "║", board[i + 1], "║", board[i + 2], "║")
        if i < 6:
            print("╠═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╝")

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

def minimax(depth, maximizing_player):
    if check_win(player):
        return -1
    elif check_win(ai):
        return 1
    elif check_draw():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                eval = minimax(depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                eval = minimax(depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

def ai_move():
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = ai

def reset_game():
    global board
    board = [" " for _ in range(9)]

def play_game():
    current_player = player

    # Countdown timer thread
    def timer_thread():
        global time_up
        for t in range(time_limit, 0, -1):
            if time_up:
                break
            print_timer(t)
            time.sleep(1)
        time_up = True

    countdown_thread = threading.Thread(target=timer_thread)
    countdown_thread.start()

    while True:
        if time_up:
            print("시간 끝났다! 게임 끝!!")
            break

        if current_player == player:
            display_board()
            position = input("Player " + current_player + ", 좌표를 입력 (1-9): ")
            position = int(position) - 1

            if board[position] == " ":
                board[position] = current_player

                if check_win(current_player):
                    display_board()
                    print("Player " + current_player + " 이겼다!")
                    break
                elif check_draw():
                    display_board()
                    print("무승부입니다")
                    break
                else:
                    current_player = ai
            else:
                print("무효! 다시 해보세요.")
        else:
            ai_move()

            if check_win(current_player):
                display_board()
                print("AI 이겼다!")
                break
            elif check_draw():
                display_board()
                print("무승부입니다")
                break
            else:
                current_player = player
while True:
    play_game()
    com = input("어땠습니까? (Good/No):")
    if com.lower() != 'Good':
        break
