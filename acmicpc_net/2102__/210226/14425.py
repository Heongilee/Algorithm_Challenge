# 백준 14425번
# https://www.acmicpc.net/problem/14425
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n, m = map(int, input().split())
    W = {input() for _ in range(n)}
    cnt = 0

    for _ in range(m):
        ct = input()
        if ct in W:
            cnt += 1

    print(cnt)
