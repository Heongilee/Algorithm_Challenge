# 백준 13913번
# https://www.acmicpc.net/problem/13913
import sys, copy
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
INF = int(10e9)

class Itertools:
    resultsSet = []

    def __init__(self, array, L, s, pick):
        self.array = array
        self.result = []

        self.combinations(L, s, pick)
    
    def combinations(self, L, s, pick):
        if L == pick:
            self.resultsSet.append(copy.deepcopy(self.result))
        else:
            for i in range(s, len(self.array)):
                self.result.append(self.array[i])
                self.combinations(L + 1, i + 1, pick)
                self.result.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    chicken = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]
    house = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
    res = INF
    
    for mm in range(1, m + 1):
        obj = Itertools(chicken, 0, 0, mm)
        for X in obj.resultsSet:
            cost = [INF] * len(house)
            for i in range(len(X)):
                for j in range(len(house)):
                    cost[j] = min(cost[j], abs(X[i][0] - house[j][0]) + abs(X[i][1] - house[j][1]))
            res = min(res, sum(cost))
    print(res)