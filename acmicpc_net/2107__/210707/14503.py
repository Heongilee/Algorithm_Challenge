import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
if __name__ == '__main__':
    n, m = map(int, input().split())    # 3 <= n, m <= 50
    r, c, d = map(int, input().split())    # (r, c), d: 
    board = [list(map(int, input().split())) for _ in range(n)] # 빈 칸은 0, 벽은 1, 청소는 2
    board[r][c] = 2
    cnt = 1

    while True:
        
        if all (board[r + dx[k]][c + dy[k]] for k in range(4)):
            if board[r + dx[(d + 2) % 4]][c + dy[(d + 2) % 4]] == 1:
                break
            r, c = r + dx[(d + 2) % 4], c + dy[(d + 2) % 4]
            continue

        dd = d - 1 if 0 <= d - 1 < 4 else 4 + (d - 1)
        # 왼쪽 방향이 벽이라면 회전만 하고 2번으로 돌아감
        if board[r + dx[dd]][c + dy[dd]] == 1:
            d = dd
            continue
        # 현재 방향에서 왼쪽 방향이 청소가 안됐다면...
        if board[r + dx[dd]][c + dy[dd]] == 0:
            d = dd
            r, c = r + dx[d], c + dy[d]
            board[r][c] = 2
            cnt += 1
            continue
        d = dd
    print(cnt)
