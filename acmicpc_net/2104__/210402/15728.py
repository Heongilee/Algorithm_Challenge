import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
import itertools as it
input = sys.stdin.readline
INF = int(10e9)

if __name__ == '__main__':
    n, k = map(int, input().split())
    sCard = list(map(int, input().split()))
    tCard = list(map(int, input().split()))
    res = -INF

    for i in range(k + 1):
        idx = 0
        M = -INF
        for a in range(n):
            for b in range(n - i):
                if sCard[a] * tCard[b] > M:
                    M = sCard[a] * tCard[b]
                    idx = b
        
        if i == k:
            print(M)
            sys.exit(0)
        tCard[idx] = tCard[n - i - 1]