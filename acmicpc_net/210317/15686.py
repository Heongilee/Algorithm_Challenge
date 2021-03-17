# 백준 13913번
# https://www.acmicpc.net/problem/13913
import sys
import itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
INF = int(10e9)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    chicken = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]
    house = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
    res = INF
    
    for mm in range(1, m + 1):
        for X in it.combinations(chicken, mm):
            cost = [INF] * len(house)
            for i in range(len(X)):
                for j in range(len(house)):
                    cost[j] = min(cost[j], abs(X[i][0] - house[j][0]) + abs(X[i][1] - house[j][1]))
            res = min(res, sum(cost))
    print(res)