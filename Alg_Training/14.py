from collections import deque
import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def BFS(h):
    while(dq):
        t = dq.popleft()
        chk[t[0]][t[1]] = 1

        for i in range(4):
            xx = t[0] + dx[i]
            yy = t[1] + dy[i]
            if(0 <= xx < N and 0 <= yy < N and board[xx][yy] > h and chk[xx][yy] == 0):
                dq.append((xx, yy))
    return

if __name__ == '__main__':
    N = int(input())
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ans = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    chk = list([0] * N for _ in range(N))
    dq = deque([])

    for h in range(100):
        cnt = 0
        chk = list([0] * N for _ in range(N))
        for i in range(N):
            for j in range(N):
                if(chk[i][j] == 0 and board[i][j] > h):
                    cnt += 1;
                    dq.append((i, j))
                    BFS(h)
        
        ans = max(ans, cnt)
        if(cnt == 0):
            break
    print(ans)

###################################################################################
'''
sys.setrecursionlimit(10**6)

def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h):
            DFS(xx, yy, h)

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = int(input())
    cnt = 0     # 해당 높이에서 영역의 개수를 구할 cnt.
    res = 0     # 영역 개수의 최대값을 저정할 res.
    board = [list(map(int, input().split())) for _ in range(n)]

    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if(ch[i][j] == 0 and board[i][j] > h):
                    cnt += 1;
                    DFS(i, j, h)
        res = max(res, cnt)
        if(cnt == 0):
            break
    print(res)
'''