import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
from collections import deque
INF = int(10e3) + 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y):
    dq = deque()
    dq.append((x, y))
    dist[0][0] = 0
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()
        if board[x][y] == 2:
            dist[n - 1][m - 1] = min(dist[n - 1][m - 1], dist[x][y] + (n - x - 1) + (m - y - 1))

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            if (0 <= xx < n and 0 <= yy < m) and not visited[xx][yy] and board[xx][yy] != 1:
                visited[xx][yy] = True
                dist[xx][yy] = min(dist[xx][yy], dist[x][y] + 1)
                dq.append((xx, yy))

if __name__ == '__main__':
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * m for _ in range(n)]

    BFS(0, 0)
    print(dist[n - 1][m - 1] if dist[n - 1][m - 1] <= t else "Fail")