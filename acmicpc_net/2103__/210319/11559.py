# 백준 1662번
# https://www.acmicpc.net/problem/1662
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
X, Y = 12, 6
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def findPuyoCount(i, j):
    global escape
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True
    item = board[i][j]
    pos = []
    cnt = 0
    while dq:
        i, j = dq.popleft()
        pos.append((i, j))
        cnt += 1
        for k in range(4):
            ii = i + dx[k]
            jj = j + dy[k]
            if (0 <= ii < X and 0 <= jj < Y) and not visited[ii][jj] and board[ii][jj] == item:
                visited[ii][jj] = True 
                dq.append((ii, jj))
    if cnt >= 4:
        escape = True
        for x, y in pos:
            board[x][y] = '.'

def slidingPuyo():
    flag = False
    for i in range(X - 1):
        for j in range(Y):
            if board[i][j] != '.' and board[i + 1][j] == '.':
                flag = True
                for r in range(i, -1, -1):
                    board[r + 1][j] = board[r][j]
                    if r == 0:
                        board[r][j] = '.'
    return flag

if __name__ == '__main__':
    board = [list(input()) for _ in range(12)]
    round = 0

    while True:
        escape = False
        visited = [[False] * 6 for _ in range(12)]
        blockQ = deque()
        for i in range(X):
            for j in range(Y):
                if board[i][j]  != '.' and not visited[i][j]:
                    findPuyoCount(i, j)

        if not escape: break
        while slidingPuyo(): pass
        round += 1

    print(round)
