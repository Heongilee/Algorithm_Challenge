import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
from collections import deque

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = list(list(map(int, input())) for _ in range(n))
    cnt = 0
    dq = deque()
    
    for i in range(n):
        for j in range(m):
            if(board[i][j] != 1):
                cnt += 1
                dq.append((i, j))
                board[i][j] = 1
                while(dq):
                    x, y = dq.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if(0 <= xx < n and 0 <= yy < m and board[xx][yy] != 1):
                            dq.append((xx, yy))
                            board[xx][yy] = 1
    print(cnt)