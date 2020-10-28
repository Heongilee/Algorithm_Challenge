from collections import deque


def BFS(x, y):
    global cnt
    cnt += 1
    dq = deque([])
    dq.append((x, y))
    while(dq):
        t = dq.popleft()
        board[t[0]][t[1]] = 0
        for tx, ty in zip(dx, dy):
            xx = t[0] + tx
            yy = t[1] + ty
            if(0 <= xx < N and 0 <= yy < N and board[xx][yy] == 1):
                dq.append((xx, yy))
    return


if __name__ == "__main__":
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if(board[i][j] == 1):
                BFS(i, j)
    print(cnt)