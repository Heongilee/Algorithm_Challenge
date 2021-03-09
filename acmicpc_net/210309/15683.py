# 백준 15683번
# https://www.acmicpc.net/problem/15683
import sys
import copy as cp
sys.stdin = open("./acmicpc_net/input.txt", "rt")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10e9)

def DFS(L):
    global result
    global board
    if L == len(cctv):
        cnt = 0
        for e in board:
            cnt += e.count('0')
        result = min(result, cnt)
        return
    else:
        if cctv[L][2] == '1':
            for i in range(4):
                tmp = cp.deepcopy(board)
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
                board = cp.deepcopy(tmp)
        elif cctv[L][2] == '2':
            for i in range(2):
                tmp = cp.deepcopy(board)
                # i(↑)랑 i + 2(↓)
                # i + 1(→)이랑 i + 3(←)
                xx = int(cctv[L][0]) + dx[i]
                yy = int(cctv[L][1]) + dy[i]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i]
                    yy += dy[i]
                
                xx = int(cctv[L][0]) + dx[i + 2]
                yy = int(cctv[L][1]) + dy[i + 2]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i + 2]
                    yy += dy[i + 2]
                
                DFS(L + 1)
                board = cp.deepcopy(tmp)
        elif cctv[L][2] == '3':
            for i in range(-1, 3):
                # i - 1(←)이랑 i(↑)
                # i(↑)랑 i + 1(→)
                # i + 1(→)이랑 i + 2(↓)
                # i + 2(↓)랑 i + 3(←)
                tmp = cp.deepcopy(board)
                xx = int(cctv[L][0]) + dx[i]
                yy = int(cctv[L][1]) + dy[i]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i]
                    yy += dy[i]
                
                xx = int(cctv[L][0]) + dx[i + 1]
                yy = int(cctv[L][1]) + dy[i + 1]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i + 1]
                    yy += dy[i + 1]
                
                DFS(L + 1)
                board = cp.deepcopy(tmp)
        elif cctv[L][2] == '4':
            # i - 2(↓)랑 i - 1(←), 그리고 i(↑)
            # i - 1(←)랑 i(↑), 그리고 i + 1(→)
            # i(↑)랑 i + 1(→), 그리고 i + 2(↓)
            # i + 1(→)랑 i + 2(↓), 그리고 i + 3(←)
            for i in range(-2, 2):
                tmp = cp.deepcopy(board)
                xx = int(cctv[L][0]) + dx[i]
                yy = int(cctv[L][1]) + dy[i]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i]
                    yy += dy[i]
                
                xx = int(cctv[L][0]) + dx[i + 1]
                yy = int(cctv[L][1]) + dy[i + 1]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i + 1]
                    yy += dy[i + 1]

                xx = int(cctv[L][0]) + dx[i + 2]
                yy = int(cctv[L][1]) + dy[i + 2]

                while 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == '6':
                        break
                    if board[xx][yy] == '0':
                        board[xx][yy] = '#'
                    xx += dx[i + 2]
                    yy += dy[i + 2]
                
                DFS(L + 1)
                board = cp.deepcopy(tmp)
        else:   # cctv[L][2] == '5':
            for i in range(4):
                tmp = cp.deepcopy(board)
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
            board = cp.deepcopy(tmp)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    cctv = []
    result = INF

    # 입력
    for i in range(n):
        t = list(input().split())
        for j in range(m):
            if '1' <= t[j] <= '5':
                # (x 좌표, y 좌표, CCTV 유형(1 ~ 5))
                cctv.append((i, j, t[j]))
        board.append(t)

    DFS(0)
    print(result)