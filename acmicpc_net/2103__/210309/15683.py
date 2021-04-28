# 백준 15683번
# https://www.acmicpc.net/problem/15683
import sys
from copy import deepcopy
sys.stdin = open("./acmicpc_net/input.txt", "rt")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10e9)

def DFS(L):
    global result, board
    if L == len(cctv):
        cnt = 0
        for e in board:
            cnt += e.count('0')
        result = min(result, cnt)
        return
    else:
        if cctv[L][2] == '1':
            for i in range(4):
                tmp = deepcopy(board)
                xx = int(cctv[L][0]) + dx[i]
                yy = int(cctv[L][1]) + dy[i]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i]
                    yy += dy[i]
                DFS(L + 1)
                board = deepcopy(tmp)
        elif cctv[L][2] == '2':
            for i in range(2):
                tmp = deepcopy(board)

                for j in range(i, i + 3, 2):
                    xx = int(cctv[L][0]) + dx[j]
                    yy = int(cctv[L][1]) + dy[j]

                    while 0 <= xx < n and 0 <= yy < m:
                        if board[xx][yy] == '6':
                            break
                        if board[xx][yy] == '0':
                            board[xx][yy] = '#'
                        xx += dx[j]
                        yy += dy[j]
                DFS(L + 1)
                board = deepcopy(tmp)
        elif cctv[L][2] == '3':
            for i in range(-1, 3):
                tmp = deepcopy(board)

                for j in range(i, i + 2):
                    xx = int(cctv[L][0]) + dx[j]
                    yy = int(cctv[L][1]) + dy[j]

                    while 0 <= xx < n and 0 <= yy < m:
                        if board[xx][yy] == '6':
                            break
                        if board[xx][yy] == '0':
                            board[xx][yy] = '#'
                        xx += dx[j]
                        yy += dy[j]
                DFS(L + 1)
                board = deepcopy(tmp)
        elif cctv[L][2] == '4':
            for i in range(-2, 2):
                tmp = deepcopy(board)

                for j in range(i, i + 3):
                    xx = int(cctv[L][0]) + dx[j]
                    yy = int(cctv[L][1]) + dy[j]

                    while 0 <= xx < n and 0 <= yy < m:
                        if board[xx][yy] == '6':
                            break
                        if board[xx][yy] == '0':
                            board[xx][yy] = '#'
                        xx += dx[j]
                        yy += dy[j]
                DFS(L + 1)
                board = deepcopy(tmp)
        else:
            for i in range(4):
                tmp = deepcopy(board)
                xx = int(cctv[L][0]) + dx[i]
                yy = int(cctv[L][1]) + dy[i]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i]
                    yy += dy[i]
            DFS(L + 1)
            board = deepcopy(tmp)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    cctv = []
    result = INF

    for i in range(n):
        t = list(input().split())
        for j in range(m):
            if '1' <= t[j] <= '5':
                cctv.append((i, j, t[j]))
        board.append(t)

    DFS(0)
    print(result)