import sys
import itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
if __name__ == '__main__':
    n = int(input())
    board = [[list(input().rstrip()) for _ in range(5)] for _ in range(n)]
    minV = INF
    res = None
    for i, j in it.combinations(range(n), 2):
        cnt = 0
        for k in range(5):
            for l in range(7):
                if board[i][k][l] == board[j][k][l]:
                    continue
                cnt += 1
        if cnt < minV:
            minV = cnt
            res = (i + 1, j + 1)
    print(" ".join(map(str, res)))
