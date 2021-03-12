# 백준 16234번
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque 
sys.stdin = open("./acmicpc_net/input.txt", "rt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, l, r = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    dq = deque()
    res = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        flag = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    ca = []
                    dq.append((i, j))
                    ca.append((i, j))
                    visited[i][j] = True

                    while dq:
                        x, y = dq.popleft()

                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]

                            if (0 <= xx < n and 0 <= yy < n) and (l <= abs(A[xx][yy] - A[x][y]) <= r) and not visited[xx][yy]:
                                visited[xx][yy] = True
                                dq.append((xx, yy))
                                ca.append((xx, yy))
                    
                    if len(ca) > 1:
                        flag = True
                        t = sum([A[z][w] for z, w in ca]) // len(ca)
                        for z, w in ca:
                            A[z][w] = t
        if not flag:
            break
        res += 1

    print(res)