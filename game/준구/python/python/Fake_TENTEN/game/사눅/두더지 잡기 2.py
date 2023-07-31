import random

print('게임의 사이즈는 10x10 입니다 ')

grid_size = 10
grid = [[' '] * grid-size for _ in range(grid_size)]

num_moles = 6
for _ in range(num_moles):
    x = random.randint(0, grid_size - 1)
    y = random.randint(0, grid_size - 1)
    grid[y][x] = 'M'

while True:
    print('\n'. join([' '.join(row) for row in grid]))
    print('두더지가 잡을 좌표 입력 (좌표는 두 숫자 입력 0~9)')

    x,y = map(int, input().split())

    if gird[y][x] == 'M':
        print('축하합니다! 두더지 잡았다')
        grid[y][x] = 'X'
    else:
        print('우와! 아쉽다 ㅠㅠㅠ')

    if all('M' not in row  for row in grid):
        print('축하합니다! 두더지를 다 잡았다!')
        break
    
