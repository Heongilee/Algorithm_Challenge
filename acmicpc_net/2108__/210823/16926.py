import sys, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    for _ in range(r):
        cnt = 0
        i = j = cnt
        lx, rx = 0, n - 1
        ly, ry = 0, m - 1
        while True:
            tmp = board[i][j]
            # 12시
            while j < ry:
                board[i][j] = board[i][j + 1]
                j += 1
            while i < rx:
                board[i][j] = board[i + 1][j]
                i += 1
            while j > ly:
                board[i][j] = board[i][j - 1]
                j -= 1
            while i > lx + 1:
                board[i][j] = board[i - 1][j]
                i -= 1
            board[i][j] = tmp
            lx, rx = lx + 1, rx - 1
            ly, ry = ly + 1, ry - 1
            cnt += 1
            i = j = cnt
            if lx > rx or ly > ry:
                break
    for i in range(n):
        print(" ".join(map(str, board[i])))