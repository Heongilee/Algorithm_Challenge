# https://youtu.be/5Lu34WIx2Us?t=3206
# 금광
import sys
import numpy as np
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
'''
if __name__ == "__main__":
    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    T = int(input())
    
    for t in range(T):
        N, M = map(int, input().split())
        board = list(map(int, input().split()))
        board = np.reshape(board, (N, M))

        D = [0] * M
        r = 0   # row
        c = 0   # col
        mm = -1
        for i in range(N):
            if(board[i][0] > mm):
                mm = board[i][0]
                r = i
        D[0] = board[r][c]

        # DP
        for i in range(1, M):
            mm = -1 
            tx = -1
            ty = -1
            for j in range(3):
                xx = r + dx[j]
                yy = c + dy[j]
                if((0 <= xx < N) and (0 <= yy < M) and board[xx][yy] > mm):
                    mm = board[xx][yy]
                    tx = xx
                    ty = yy
            r = tx
            c = ty
            D[i] = D[i - 1] + mm
        print(D[M - 1])
'''
##################################################################################
if __name__ == "__main__":
    dx = [-1, 0, 1]
    dy = [-1, -1, -1]
    for t in range(int(input())):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))

        D = []
        idx = 0
        for i in range(n):
            D.append(arr[idx:idx + m])
            idx += m
        
        # DP 진행.
        for j in range(1, m):
            for i in range(n):
                brr = []
                for k in range(3):
                    xx = i + dx[k]
                    yy = j + dy[k]

                    if((0 <= xx < n) and (0 <= yy < m)):
                        brr.append(D[xx][yy])

                D[i][j] += max(brr)
        
        ans = D[0][m - 1]
        for a in range(1, n):
            if(D[a][m - 1] > ans):
                ans = D[a][m - 1]
        print(ans)