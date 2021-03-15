import sys
sys.stdin = open("./input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(i, j):
    global key, box
    visited[i][j] = True

    if board[i][j] == 4:
        key = True
    if board[i][j] == 2:
        box = True

    for k in range(4):
        ii = i + dx[k]
        jj = j + dy[k]

        if(0 <= ii < m and 0 <= jj < n) and not visited[ii][jj] and board[ii][jj] != 1:
            DFS(ii, jj)

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        m, n = map(int, input().split())
        key = False
        box = False

        board = [list(map(int, input().split())) for _ in range(m)]
        visited = [[False] * n for _ in range(m)]

        # 소마 위치
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    DFS(i, j)
        
        print(1 if (key and box) else 0)