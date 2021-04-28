# 백준 11047번
# https://www.acmicpc.net/problem/11047
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n, k = map(int, input().split())
    coin = list(int(input()) for _ in range(n))
    cnt = 0

    for i in range(n - 1, -1, -1):
        if(k // coin[i] == 0):
            continue
        else:
            cnt += k // coin[i]
            k %= coin[i]
            if(k == 0):
                break
    print(cnt)