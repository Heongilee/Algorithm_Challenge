# 백준 7576번
# https://www.acmicpc.net/problem/7576
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    global res
    while(dq):
        x, y = dq.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if(0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0):
                board[xx][yy] = 1
                dis[xx][yy] = dis[x][y] + 1
                res = dis[xx][yy]
                dq.append((xx, yy))

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    dis = [[0] * (n + 1) for _ in range(m)]
    dq = deque([])
    res = 0

    # input
    for i in range(m):
        l = list(map(int, input().split()))
        board.append(l)
    
    # find tomato
    for i in range(m):
        for j in range(n):
            if(board[i][j] == 1):
                dq.append((i, j))
    BFS()
    for b in board:
        if any (e == 0 for e in b):
            print(-1)
            break
    else:
        print(res)