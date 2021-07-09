import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    a, t, b = list(int(input()) for _ in range(3))
    n = 2   # n - 1회차 문장
    board = [0, 1, 0, 1] + [0] * n + [1] * n

    i = 0       # board를 순회하는 인덱스
    p = i % a   # 현재 board를 가리키는 인덱스 i에 대해 p는 몇번째 사람인지 나타냄
    cnt= 0      # b가 카운트된 횟수
    while True:
        if i >= len(board):
            n += 1
            board += [0, 1, 0, 1] + [0] * n + [1] * n
        if board[i] == b:
            cnt += 1
            if cnt == t: break
        i += 1
        p = i % a
    print(p)
