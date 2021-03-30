import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
from collections import deque
INF = int(10e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dir = 1 # dx, dy 인덱스에 따라 정해질 방향. L을 만나면 -1 D를 만나면 +1 한다.
    pos = [0, 0]
    snakeQ = deque()    # (스네이크 몸체 위치 X, 스네이크 몸체 위치 Y)
    weight = 1  # 현재 스네이크 몸의 길이값
    board[0][0] = weight
    snakeQ.append((0, 0))

    k, apple = int(input()), []
    for _ in range(k):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = -1 # -1은 사과

    l, direction = int(input()), []
    for _ in range(l):
        t = input().split()
        direction.append((int(t[0]), t[1]))
    direction = deque(direction)
    
    for sec in range(1, INF):
        alpha, jumpFlag = 0, False
        if not 0 <= pos[0] + dx[dir] < n or not 0 <= pos[1] + dy[dir] < n or (board[pos[0] + dx[dir]][pos[1] + dy[dir]] > 0):
            print(sec)
            sys.exit(0)

        if board[pos[0] + dx[dir]][pos[1] + dy[dir]] == -1:
            alpha, jumpFlag = 1, True
        board[pos[0] + dx[dir]][pos[1] + dy[dir]] = board[pos[0]][pos[1]] + alpha
        
        if not jumpFlag:
            for _ in range(len(snakeQ)):
                x, y = snakeQ.pop()
                if board[x][y] != 0:
                    board[x][y] -= 1
                    if board[x][y] != 0:
                        snakeQ.appendleft((x , y))

        pos = [pos[0] + dx[dir], pos[1] + dy[dir]]
        snakeQ.append(pos)

        # 방향 수정
        if direction and direction[0][0] == sec:
            s, d = direction.popleft()
            if d == 'D':
                dir += 1
                dir %= 4
            else:   # d == 'L'
                dir -= 1
                if dir == -1: dir = 4 + dir