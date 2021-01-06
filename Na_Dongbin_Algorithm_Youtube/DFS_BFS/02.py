import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = list(list(map(int, input())) for _ in range(n))
    dis = list([0] * m for _ in range(n))
    dq = deque()
    dq.append((0, 0))   # 시작 위치
    board[0][0] = 0

    while(dq):
        x, y = dq.popleft()


        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1):
                board[xx][yy] = 0
                dis[xx][yy] = dis[x][y] + 1
                if(xx == n - 1 and yy == m - 1):
                    print(dis[xx][yy])
                    sys.exit(0)
                dq.append((xx, yy))

