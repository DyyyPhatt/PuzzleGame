from collections import deque
from queue import PriorityQueue
import heapq
import random
import consoles 
import pygame
import drawing

def UCS(maTrix):
    soLan = 0
    print("\nPhương pháp UCS")
    drawing.print_solver()
    consoles.print_board(maTrix)
    path = UCS_solve(maTrix)
    if path:
        for diChuyen in path:
            soLan += 1
            consoles.move(maTrix, diChuyen)
            drawing.draw_board(maTrix,soLan)
            print("Di chuyển: " + diChuyen)
            consoles.print_board(maTrix)
            pygame.time.delay(200)
    else:
        drawing.no_solver()

def UCS_solve(maTrixBanDau):
    queue = PriorityQueue()
    queue.put((0, maTrixBanDau, []))
    visited = set()

    while not queue.empty():
        trongSo, maTrixHienTai, status = queue.get()
        visited.add(tuple(map(tuple, maTrixHienTai)))

        if consoles.check(maTrixHienTai):
            return status
        for diChuyen in ['left', 'right', 'up', 'down']:
            NewMatrix = [row[:] for row in maTrixHienTai]
            consoles.move(NewMatrix, diChuyen)

            if tuple(map(tuple, NewMatrix)) not in visited:
                newStatus = status + [diChuyen]
                newTrongSo = trongSo + 1
                queue.put((newTrongSo ,NewMatrix, newStatus))
                visited.add(tuple(map(tuple, NewMatrix)))
    return None

def BFS(game_board):
    print("Trò chơi dịch chuyển 8 số:")
    soLan =0
    consoles.print_board(game_board)
    drawing.draw_board(game_board,soLan)
    drawing.print_solver()
    if consoles.check(game_board):
        print("Trò chơi đã ở trạng thái sắp xếp.")
        return
    solution = BFS_solve(game_board)
    if solution:
        print("Lời giải:")
        for move_direction in solution:
            soLan +=1
            print("Di chuyển", move_direction)
            consoles.move(game_board, move_direction)
            consoles.print_board(game_board)
            drawing.draw_board(game_board, soLan)             
            pygame.time.delay(200)
    else:
        drawing.no_solver()

def BFS_solve(MatrixBanDau):
    queue = deque([(MatrixBanDau, [])])
    visited = set()  # Không chứa phần tử trùng lặp

    while queue:
        MatrixHienTai, path = queue.popleft() # Lấy ra trạng thái hiện tại và đường đi tương ứng từ phần tử đầu tiên của hàng đợi và gán chúng cho MatrixHienTai và path.
        visited.add(tuple(map(tuple, MatrixHienTai))) # chuyển thành một tuple lớn chứa các tuple con ,
                                                        #lưu trữ nhiều trạng thái mà những trạng thái này không thay đổi được
                                                        #map(tuple, max): chuyển ma trận hiện tại thành 1 tuple( vì trạng thái sẽ kh bị thay đổi)
        if consoles.check( MatrixHienTai ):
            return path

        for diChuyen in ['left', 'right', 'up', 'down']:
            NewMatrix= [row[:] for row in MatrixHienTai ]  # Sao chép ma trận hiện tại
            consoles.move(NewMatrix, diChuyen)
            if tuple(map(tuple, NewMatrix)) not in visited: #Kiểm tra trạng thái mới đã được duyệt chưa, nếu rồi thì kh thêm vào hàng đợi
                new_path = path + [diChuyen]
                queue.append((NewMatrix, new_path))
                visited.add(tuple(map(tuple, NewMatrix)))

    return None


def ID_solve(matrix, max_depth, maxSteps, depth=0, path=[]):
    print(path)
    if depth > max_depth or len(path) > maxSteps:
        return None

    if consoles.check(matrix):
        return path

    moves = ['left', 'right', 'up', 'down']
    for move in moves:
        new_matrix = [row[:] for row in matrix]
        consoles.move(new_matrix, move)

        if new_matrix != matrix:
            print("Di chuyen: " + move)
            consoles.print_board(new_matrix)

            new_path = path + [move]
            solution = ID_solve(new_matrix, max_depth, maxSteps, depth + 1, new_path)

            if solution is not None:
                return solution

    return None

def ID(maTrix, maxDepth, maxSteps):
    print("\nPhương pháp ID, độ sâu 10: ")
    path = ID_solve(maTrix, maxDepth, maxSteps)
    soLan = 0
    if path is not None:
        print("Tìm thấy đường đi")
        for diChuyen in path:
            soLan +=1
            print("Di chuyển", diChuyen)
            consoles.move(maTrix, diChuyen)
            consoles.print_board(maTrix) 
            drawing.draw_board(maTrix, soLan)
            pygame.time.delay(200)
    else:
        drawing.no_solver()

#           THUẬT TOÁN DFS
def DFS(maTrix):
    soLan = 0
    print("\nPhương pháp DFS, giới hạn 26000 bước")
    drawing.print_solver()
    path = []
    buocGiai = DFS_solve(maTrix, 0, 26000, path)
    if buocGiai:
        for diChuyen in range(buocGiai):
            soLan +=1
            print("Di chuyển", diChuyen)
            consoles.move(maTrix, diChuyen)
            drawing.draw_board(maTrix,soLan)
            pygame.time.delay(200)
    else:
        drawing.no_solver()

def DFS_solve(matrix, depth, maxDepth, path):
    print(path)
    if depth > maxDepth:
        return False  # Đã đạt đến giới hạn độ sâu

    if consoles.check(matrix):
        return path  # Trạng thái kết thúc, trả về đường đi
    diChuyenNgauNhien = ['left', 'right', 'up', 'down']
    random.shuffle(diChuyenNgauNhien)
    for diChuyen in diChuyenNgauNhien:
        newMatrix = [row[:] for row in matrix]
        consoles.move(newMatrix, diChuyen)
        if newMatrix == matrix:
            continue
        
        print("Di chuyen: " + diChuyen)
        consoles.print_board(matrix)
        new_path = path + [diChuyen]
        solution = DFS_solve(newMatrix, depth + 1, maxDepth, new_path)
        if solution is not None:
            return solution

    return False  # Không tìm thấy giải pháp

def Greedy(maTrix):
    soLan = 0
    print("\nPhương pháp Greedy")
    drawing.print_solver()
    consoles.print_board(maTrix)
    paths = Greedy_solve(maTrix)
    if paths:
        drawing.draw_board(maTrix,0)
        for diChuyen in paths:
            soLan +=1
            consoles.move(maTrix, diChuyen)
            drawing.draw_board(maTrix, soLan)
            pygame.time.delay(200)
            print("Di chuyển: " + diChuyen)
            consoles.print_board(maTrix)
    else:
        drawing.no_solver()

def Greedy_solve(maTrixBanDau):
    queue = []
    heapq.heappush(queue, (h_manhattan(maTrixBanDau), maTrixBanDau, []))
    visited = set()

    while queue:
        _, maTrixHienTai, status = heapq.heappop(queue)
        visited.add(tuple(map(tuple, maTrixHienTai)))

        if consoles.check(maTrixHienTai):
            return status

        for diChuyen in ['left', 'right', 'up', 'down']:
            NewMaTrix = [row[:] for row in maTrixHienTai]
            consoles.move(NewMaTrix, diChuyen)
            #drawing.draw_board(NewMaTrix,0)
            if tuple(map(tuple, NewMaTrix)) not in visited:
                new_status = status + [diChuyen]
                heapq.heappush(queue, (h_manhattan(NewMaTrix), NewMaTrix, new_status))

    return None

# Hàm A* để giải N-puzzle sử dụng hàm heuristic h_manhattan.
def A_star_solve(MatrixBanDau):
    n = len(MatrixBanDau)
    
    # Hàng đợi ưu tiên với các phần tử (state, cost, path).
    # cost: tổng chi phí thực tế từ trạng thái ban đầu đến trạng thái hiện tại.
    # path: dãy các bước để đạt được trạng thái hiện tại.
    pq = [(0 + h_manhattan(MatrixBanDau), 0, MatrixBanDau, [])]
    visited = set()

    while pq:
        _, cost, current_state, path = heapq.heappop(pq)
        visited.add(tuple(map(tuple, current_state)))

        if consoles.check(current_state):
            return path

        for diChuyen in ['left', 'right', 'up', 'down']:
            new_state = [row[:] for row in current_state]
            consoles.move(new_state, diChuyen)
            if tuple(map(tuple, new_state)) not in visited:
                new_cost = cost + 1 + h_manhattan(new_state)  # Sử dụng hàm heuristic h_manhattan
                new_path = path + [diChuyen]
                heapq.heappush(pq, (new_cost, new_cost, new_state, new_path))

    return None

# Sử dụng hàm A* để giải trò chơi N-puzzle.
def A_star(game_board):
    print("Trò chơi dịch chuyển 8 số:")
    soLan = 0
    consoles.print_board(game_board)
    drawing.draw_board(game_board, soLan)
    drawing.print_solver()
    if consoles.check(game_board):
        print("Trò chơi đã ở trạng thái sắp xếp.")
        return
    solution = A_star_solve(game_board)
    if solution:
        print("Lời giải:")
        for move_direction in solution:
            soLan += 1
            print("Di chuyển", move_direction)
            consoles.move(game_board, move_direction)
            consoles.print_board(game_board)
            drawing.draw_board(game_board, soLan)
            pygame.time.delay(200)
    else:
        drawing.no_solver()

def h_manhattan(matrix):
    # Hàm tính khoảng cách Manhattan từ trạng thái hiện tại đến trạng thái đích
    n = len(matrix)
    h = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:  # Loại trừ ô trống
                value = matrix[i][j] - 1
                goal_row = value // n
                goal_col = value % n
                h += abs(i - goal_row) + abs(j - goal_col)
    return h