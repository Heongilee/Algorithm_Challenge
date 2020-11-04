from collections import deque

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
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N = int(input())
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
                    cnt += 1
                    dq.append((i, j))
                    BFS(h)
        ans = max(ans, cnt)
        if(cnt == 0):
            break
    print(ans)