# 백준 12865번
# https://www.acmicpc.net/problem/12865
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n, k = map(int, input().split())
    D = [0] * (k + 1)

    for _ in range(n):
        w, v = map(int, input().split())

        for i in range(k, w - 1, -1):
            D[i] = max(D[i - w] + v, D[i])
    print(D[k])