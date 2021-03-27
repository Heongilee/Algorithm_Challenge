import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
from collections import deque

dx = [0, 1]
dy = [1, 0]

'''
def BFS(x, y):
    dq = deque()
    dq.append((x, y))
    dis[x][y] = board[x][y]
    while dq:
        x, y = dq.popleft()

        for k in range(2):
            xx = x + dx[k]
            yy = y + dy[k]

            if (0 <= xx < m and 0 <= yy < n):
                dis[xx][yy] = max(dis[xx][yy], dis[x][y] + board[xx][yy])
                dq.append((xx, yy))
'''

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    dis = [[0] * n for _ in range(m)]

    dis[0][0] = board[0][0]
    for x in range(1, m):
        dis[x][0] = dis[x - 1][0] + board[x][0]

    for y in range(1, n):
        dis[0][y] = dis[0][y - 1] + board[0][y]
    
    for i in range(1, m):
        for j in range(1, n):
            dis[i][j] = max(dis[i - 1][j], dis[i][j - 1]) + board[i][j]

    print(dis[m - 1][n - 1])    