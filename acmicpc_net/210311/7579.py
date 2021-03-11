# 백준 7579번
# https://www.acmicpc.net/problem/7579
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n, m = map(int, input().split())
    Mem = list(map(int, input().split()))
    Cost = list(map(int, input().split()))
    D = [0] * (sum(Cost) + 1)

    for i in range(n):
        for j in range(sum(Cost), Cost[i] - 1, -1):
            D[j] = max(D[j - Cost[i]] + Mem[i], D[j])

    for i in range(1, sum(Cost) + 1):
        if D[i] >= m:
            print(i)
            break