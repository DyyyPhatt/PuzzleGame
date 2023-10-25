import random

def move(board, move_direction):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if move_direction == 'left' and j < n-1:
                    board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                    return
                elif move_direction == 'right' and j > 0:
                    board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
                    return
                elif move_direction == 'up' and i < n-1:
                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                    return
                elif move_direction == 'down' and i > 0:
                    board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                    return
                
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def khoiTao(n):
    maTrix = [[None] * n for _ in range(n)]
    numbers = list(range(0, n*n))

    for i in range(n):
        for j in range(n):
            maTrix[i][j] = numbers.pop()

    diChuyen = random.randint(30, 50)
    for i in range(diChuyen):
        huongDiChuyen = ['left', 'right', 'up', 'down']
        random.shuffle(huongDiChuyen)
        move(maTrix, huongDiChuyen[0])
        print_board(maTrix)
        print('\n')
    return maTrix

#               CÁC HÀM KIỂM TRA ĐIỀU KIỆN

def check(maTrix):
    n = len(maTrix)
    goal = [[None] * n for _ in range(n)]

    number = 1  # Bắt đầu từ 1
    for i in range(n):
        for j in range(n):
            goal[i][j] = number
            number += 1

    goal[-1][-1] = 0  # Đặt ô trống vào vị trí cuối cùng

    return maTrix == goal
'''
def check(maTrix):
    n = len(maTrix)
    goal = [[None] * n for _ in range(n)]
    numbers = list(range(0, n*n))

    for i in range(n):
        for j in range(n):
            goal[i][j] = numbers.pop()

    return maTrix == goal
'''