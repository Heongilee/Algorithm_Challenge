import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 끝에 공기청정기로 들어간 미세먼지는 정화된다.
def rotateClockwise(t):
    global amount
    x, y = t, 0
    # 9시
    while x > 0:
        board[x][y] = board[x - 1][y]
        if x == t and y == 0:
            amount -= board[x - 1][y]
            board[x][y] = -1
        x -= 1
    # 12시
    while y < c - 1:
        board[x][y] = board[x][y + 1]
        y += 1
    # 3시
    while x < t:
        board[x][y] = board[x + 1][y]
        x += 1
    # 6시
    while y > 1:
        board[x][y] = board[x][y - 1]
        y -= 1
    board[x][y] = 0

def rotateCounterClockwise(t):
    global amount
    x, y = t, 0
    # 9시
    while x < r - 1:
        board[x][y] = board[x + 1][y]
        if x == t and y == 0:
            amount -= board[x + 1][y]
            board[x][y] = -1
        x += 1
    # 6시
    while y < c - 1:
        board[x][y] = board[x][y + 1]
        y += 1
    # 3시
    while x > t:
        board[x][y] = board[x - 1][y]
        x -= 1
    # 12시
    while y > 1:
        board[x][y] = board[x][y - 1]
        y -= 1
    board[x][y] = 0

if __name__ == '__main__':
    # R행 C열 T초가 지남
    # 6 ≤ R, C ≤ 50 
    # 1 ≤ T ≤ 1,000
    r, c, t = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(r)]
    # 공기청정기는 2행을 차지한다. 하나는 (r1,0)에 또 하나는 (r2, 0)에 위치함.
    r1, r2 = tuple(i for i in range(r) for j in range(c) if board[i][j] == -1)
    amount = sum([board[i][j] for i in range(r) for j in range(c) if board[i][j] != -1])

    for _ in range(t):
        # 미세먼지 확산
        dq = deque([(i, j, board[i][j]) for i in range(r) for j in range(c) if board[i][j] > 0])
        board = list([0] * c for _ in range(r))
        board[r1][0], board[r2][0] = -1, -1

        while dq:
            x, y, w = dq.popleft()
            dirCnt = sum([1 for k in range(4) if 0 <= x + dx[k] < r and 0 <= y + dy[k] < c and board[x + dx[k]][y + dy[k]] != -1])
            t = w // 5
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= x + dx[k] < r and 0 <= y + dy[k] < c and board[x + dx[k]][y + dy[k]] != -1:
                    board[xx][yy] += t
            board[x][y] += w - t * dirCnt
        
        # 공기청정기 순환
        rotateClockwise(r1)
        rotateCounterClockwise(r2)

    print(amount)