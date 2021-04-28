import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
if __name__ == '__main__':
    m, n = map(int, input().split())
    board = [[0] * n for _ in range(m)]
    dir, cnt, x, y = 0, 0, 0, 0
    while True:
        board[x][y] = 1
        cnt += 1
        if cnt >= m * n: break
        while not 0 <= x + dx[dir % 4] < m or not 0 <= y + dy[dir % 4] < n or board[x + dx[dir % 4]][y + dy[dir % 4]] == 1:
            dir += 1
        x += dx[dir % 4]
        y += dy[dir % 4]

    print(dir)