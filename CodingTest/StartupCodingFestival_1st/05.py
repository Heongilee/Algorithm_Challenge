import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
INF = int(10e9)
dx = [1, 0, 0]
dy = [0, 1, -1]

def DFS(x, y, lr):
    global cnt

    if x == m - 1:
        cnt = min(cnt, lr)
        return
    
    for k in range(3):
        xx = x + dx[k]
        yy = y + dy[k]

        if (0 <= xx < m and 0 <= yy < n) and board[xx][yy] == '.' and not visited[xx][yy]:
            visited[xx][yy] = True
            if k >= 1: lr += 1
            DFS(xx, yy, lr)
            if k >= 1: lr -= 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(m)]
    start = [(0, x) for x in range(n) if board[0][x] == 'c']
    res = INF

    for sx, sy in start:
        visited = [[False] * n for _ in range(m)]
        cnt = INF   # 좌우로 이동한 최소 횟수
        visited[sx][sy] = True
        DFS(sx, sy, 0)
        res = min(res, cnt)

    print(res if res != INF else -1)