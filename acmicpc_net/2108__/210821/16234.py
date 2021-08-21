import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
''' 
# TODO : BOJ 16234 예시 3번 (https://www.acmicpc.net/problem/16234)

output : 3
answer : 1
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
if __name__ == '__main__':
    # (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        f = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    dq = []
                    ptr = 0
                    dq.append((i, j))
                    visited[i][j] = True
                    while ptr < len(dq):
                        x, y = dq[ptr]
                        ptr += 1
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if (0 <= xx < n and 0 <= yy < n) and not visited[xx][yy] and (l <= abs(board[xx][yy] - board[x][y]) <= r):
                                f = True
                                dq.append((xx, yy))
                                visited[xx][yy] = True
                    avg = sum([board[x][y] for x, y in dq]) // len(dq)
                    for s, t in dq: board[s][t] = avg
        if not f:
            break
        res += 1
    print(res)