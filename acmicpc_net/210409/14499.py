import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 동서북남(인덱스0은 제외)
dx = [-1, 0, 0, -1, 1]
dy = [-1, 1, -1, 0, 0]

def moveDice(c):
    if c == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif c == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif c == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

if __name__ == '__main__':
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    command = list(map(int, input().split()))
    dice = [-1, 0, 0, 0, 0, 0, 0]   # [N/A, 위쪽, 북쪽, 동쪽, 서쪽, 남쪽, 아래]
    
    for c in command:
        if 0 <= x + dx[c] < n and 0 <= y + dy[c] < m:
            moveDice(c)

            x += dx[c]
            y += dy[c]
            # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            if board[x][y] == 0:    
                board[x][y] = dice[6]
            # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
            else:
                dice[6] = board[x][y]
                board[x][y] = 0
            print(dice[1])